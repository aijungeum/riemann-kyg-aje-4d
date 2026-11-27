"""
================================================================================
Project: riemann-kyg-aje-4d
Title:   A Study on the 4-Dimensional Topological Structure and Dynamical 
         Convergence of Prime Distribution: The KYG Hypothesis Based on 
         AiJungEum Encoding
         (소수 분포의 4차원 위상 구조 및 동역학적 수렴에 관한 연구)

Author:  KYG
Email:   aijungeum@gmail.com
Website: https://aijungeum.com
Date:    2026-11-27

Description:
  - Maps 2-byte prime numbers (0 ~ 65,535) to 16-bit AiJungEum PUA glyphs.
  - Recursively decomposes and compresses 4 components (16x16x16x16) by 1/4 
    until converging to a single singularity.
  - Simulates 4D spatiotemporal dynamics (Orbit & Helical Vortex models).

Requirements:
  - Python 3.9+
  - Packages: numpy, matplotlib, pillow, fonttools
  - Font File: AiJungEum_0.1.a2.ttc (in the same directory)
================================================================================
"""

import os
import glob
import math
import platform
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.animation import FuncAnimation
import itertools



# ==========================================
# PUA 출력 옵션 
# ==========================================
PUA_SHOW_FRAMES = 15  # 주기적 출력(False)일 때 화면에 글자를 유지할 프레임 수
MAX_PUA_LABELS = 80   # 3D 화면 성능 유지를 위한 최대 동시 표시 글자 수


# ==========================================
# AiJungEum 폰트 로더
# ==========================================
import tempfile
from fontTools.ttLib import TTCollection

def setup_aijungeum_ttc_fonts(target_filename="AiJungEum_0.1.a2.ttc"):
  sys_os = platform.system()
  fallback = (
      "Malgun Gothic"
      if sys_os == "Windows"
      else ("AppleGothic" if sys_os == "Darwin" else "NanumGothic")
  )

  ttc_path = None
  matches = glob.glob(
      os.path.join(os.getcwd(), "**", target_filename), recursive=True
  )
  if matches:
    ttc_path = matches[0]
  else:
    for fpath in glob.glob(
        os.path.join(os.getcwd(), "**", "*.ttc"), recursive=True
    ):
      if "aijungeum" in os.path.basename(fpath).lower():
        ttc_path = fpath
        break

  if ttc_path and os.path.exists(ttc_path):
    temp_dir = tempfile.gettempdir()
    extracted_paths = list()

    # TTC 컬렉션에서 개별 TTF 파일(part1, part2)을 임시 폴더에 분리 저장
    ttc = TTCollection(ttc_path)
    for idx, tt in enumerate(ttc.fonts):
      out_ttf = os.path.join(temp_dir, f"aijungeum_part{idx + 1}.ttf")
      tt.save(out_ttf)
      font_manager.fontManager.addfont(out_ttf)
      extracted_paths.append(out_ttf)

    part1_name = font_manager.FontProperties(
        fname=extracted_paths[0]
    ).get_name()
    part2_name = (
        font_manager.FontProperties(fname=extracted_paths[1]).get_name()
        if len(extracted_paths) > 1
        else part1_name
    )

    plt.rcParams["font.family"] = [
        fallback,
        part1_name,
        part2_name,
        "sans-serif",
    ]
    plt.rcParams["axes.unicode_minus"] = False

    # AiJungEum PUA 문자 이외의 언어 렌더링되도록 폰트 리스트 구성 
    prop_part1 = font_manager.FontProperties(
        family=[part1_name, fallback, part2_name]
    )
    prop_part2 = font_manager.FontProperties(
        family=[part2_name, fallback, part1_name]
    )
    prop_ui = font_manager.FontProperties(
        family=[fallback, part1_name, part2_name]
    )

    print(
        f"[폰트 분리 및 적용 완료] {part1_name}, {part2_name} (한글 보조:"
        f" {fallback})"
    )
    return prop_part1, prop_part2, prop_ui

  plt.rcParams["font.family"] = fallback
  plt.rcParams["axes.unicode_minus"] = False
  prop_fb = font_manager.FontProperties(family=fallback)
  print(f"[알림] {target_filename}을 찾지 못해 {fallback}만 적용합니다.")
  return prop_fb, prop_fb, prop_fb


PROP_PART1, PROP_PART2, ACTIVE_FONT_PROP = setup_aijungeum_ttc_fonts()


def get_aje_font_prop(char: str):
  if not char:
    return ACTIVE_FONT_PROP
  cp = ord(char)
  if 0xF0000 <= cp <= 0xF7FFF:
    return PROP_PART1
  elif 0x100000 <= cp <= 0x107FFF:
    return PROP_PART2
  return ACTIVE_FONT_PROP



# ==========================================
# AiJungEum 변환 
# ==========================================
PUA_A_START = 0xF0000
PUA_A_LIMIT = 0xF7FFF   # 32,768개 (0x0000 ~ 0x7FFF)
PUA_B_START = 0x100000
PUA_B_LIMIT = 0x107FFF  # 32,768개 (0x8000 ~ 0xFFFF)
JUMP_THRESHOLD = 0x8000

MAX_LINEAR_VAL = 65535.0

def index_to_aje(idx: int) -> str:
    if not (0 <= idx <= 0xFFFF):
        raise ValueError(f"인덱스 범위 초과 (0~65535): {idx}")
    if idx < JUMP_THRESHOLD:
        codepoint = PUA_A_START + idx
    else:
        codepoint = PUA_B_START + (idx - JUMP_THRESHOLD)
    return chr(codepoint)

def aje_to_index(char: str) -> int:
    cp = ord(char)
    if PUA_A_START <= cp <= PUA_A_LIMIT:
        return cp - PUA_A_START
    elif PUA_B_START <= cp <= PUA_B_LIMIT:
        return (cp - PUA_B_START) + JUMP_THRESHOLD
    else:
        raise ValueError(f"유효하지 않은 AiJungEum 코드포인트: {hex(cp)}")

# ==========================================
# 2바이트 범위(0 ~ 65535) 소수 생성기
# ==========================================
def generate_2byte_primes() -> list:
    limit = 0xFFFF
    sieve = [True] * (limit + 1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(math.isqrt(limit)) + 1):
        if sieve[i]:
            sieve[i*i : limit+1 : i] = [False] * len(range(i*i, limit+1, i))
    return [i for i, is_p in enumerate(sieve) if is_p]

# ==========================================
# 자음 4성분 분해(16x16x16x16) 및 1/4 재조합 
# ==========================================
def decompose_to_4_components(aje_list: list):
    ja1 = list()
    ja2 = list()
    ja3 = list()
    ja4 = list()
    for ch in aje_list:
        val = aje_to_index(ch)
        ja1.append((val >> 12) & 0xF)
        ja2.append((val >> 8)  & 0xF)
        ja3.append((val >> 4)  & 0xF)
        ja4.append(val & 0xF)
    return ja1, ja2, ja3, ja4

def pack_4_to_aje(ja_list: list) -> list:
    rem = len(ja_list) % 4
    if rem != 0:
        ja_list = list(ja_list) + ([0] * (4 - rem))
        
    aje_packed = list()
    for i in range(0, len(ja_list), 4):
        c1, c2, c3, c4 = ja_list[i], ja_list[i+1], ja_list[i+2], ja_list[i+3]
        combined_idx = (c1 << 12) | (c2 << 8) | (c3 << 4) | c4
        aje_packed.append(index_to_aje(combined_idx))
    return aje_packed

def build_hierarchy():
    primes = generate_2byte_primes()
    aje_base = [index_to_aje(p) for p in primes]
    
    groups = list()
    current_source = aje_base
    group_idx = 1
    
    while len(current_source) > 1:
        ja1, ja2, ja3, ja4 = decompose_to_4_components(current_source)
        aje_ja1 = pack_4_to_aje(ja1)
        aje_ja2 = pack_4_to_aje(ja2)
        aje_ja3 = pack_4_to_aje(ja3)
        aje_ja4 = pack_4_to_aje(ja4)
        
        group_idx += 1
        groups.append({
            "group_num": group_idx,
            "aje_ja1": aje_ja1,
            "aje_ja2": aje_ja2,
            "aje_ja3": aje_ja3,
            "aje_ja4": aje_ja4,
            "length": len(aje_ja1),
            "rep_char": next(iter(aje_ja1))
        })
        current_source = aje_ja1
        
    return primes, aje_base, groups


# ==========================================
# Vortex: (좌표 + 정렬된 PUA 문자 매핑 반환)
# ==========================================
def compute_galactic_vortex_arms(
    arm_values_list,
    arm_chars_list,
    time_t,
    total_progress,
    is_cw_tornado=False,
):
  all_x = list()
  all_y = list()
  all_z = list()
  all_c = list()
  all_chars = list()

  arm_base_angles = (0.0, 0.5 * np.pi, np.pi, 1.5 * np.pi)

  if not is_cw_tornado:
    scale_envelope = max(0.0, 1.0 - total_progress)
    z_base = total_progress
  else:
    scale_envelope = total_progress
    z_base = 1.0 - total_progress

  for arm_idx, (vals, chars) in enumerate(zip(arm_values_list, arm_chars_list)):
    n = len(vals)
    if n == 0:
      continue

    sort_idx = np.argsort(vals)
    sorted_vals = vals[sort_idx]
    # 좌표 정렬 순서와 동일하게 PUA 문자 배열도 정렬
    sorted_chars = [chars[i] for i in sort_idx]

    radius = sorted_vals * scale_envelope
    delta_twist = sorted_vals * (2.0 * np.pi / max(1.0, float(n)))
    cumulative_wind = np.cumsum(delta_twist)

    if not is_cw_tornado:
      theta = arm_base_angles[arm_idx] + cumulative_wind - (time_t * 0.08)
    else:
      cw_spin = time_t * 0.16
      theta = arm_base_angles[arm_idx] + cumulative_wind - cw_spin

    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    z = np.full(n, z_base) + (
        (sorted_vals - 0.5) * 0.12 * (1.0 - abs(2.0 * z_base - 1.0))
    )
    color_val = (arm_idx * 0.25) + (sorted_vals * 0.25)

    all_x.append(x)
    all_y.append(y)
    all_z.append(z)
    all_c.append(color_val)
    all_chars.extend(sorted_chars)

  return (
      np.concatenate(all_x),
      np.concatenate(all_y),
      np.concatenate(all_z),
      np.concatenate(all_c),
      all_chars,
  )


# ==========================================
# 시뮬레이션 실행기 (PUA 없음 / PUA 항상 / 주기 + 재생 속도 반영)
# ==========================================
def run_galactic_vortex_simulation(
    primes,
    aje_base,
    groups,
    pua_mode="none",
    pua_interval=100,
    frame_interval_ms=45,
):
  stages = list()
  j1, j2, j3, j4 = decompose_to_4_components(aje_base)
  first_rep = next(iter(aje_base))
  stages.append({
      "title": f"Group 1 (원본 소수 {len(primes)}개 | 대표 PUA: {first_rep})",
      "rep_char": first_rep,
      "count": len(primes),
      "arms": [
          np.array(j1, dtype=float) / 15.0,
          np.array(j2, dtype=float) / 15.0,
          np.array(j3, dtype=float) / 15.0,
          np.array(j4, dtype=float) / 15.0,
      ],
      "arm_chars": [aje_base, aje_base, aje_base, aje_base],
  })

  for g in groups:
    rc = g["rep_char"]
    stages.append({
        "title": (
            f"Group {g['group_num']} (4가닥 입자 {g['length']*4}개 | 대표 PUA:"
            f" {rc} [{hex(ord(rc))}])"
        ),
        "rep_char": rc,
        "count": g["length"],
        "arms": [
            np.array([aje_to_index(ch) for ch in g["aje_ja1"]], dtype=float)
            / MAX_LINEAR_VAL,
            np.array([aje_to_index(ch) for ch in g["aje_ja2"]], dtype=float)
            / MAX_LINEAR_VAL,
            np.array([aje_to_index(ch) for ch in g["aje_ja3"]], dtype=float)
            / MAX_LINEAR_VAL,
            np.array([aje_to_index(ch) for ch in g["aje_ja4"]], dtype=float)
            / MAX_LINEAR_VAL,
        ],
        "arm_chars": [
            g["aje_ja1"],
            g["aje_ja2"],
            g["aje_ja3"],
            g["aje_ja4"],
        ],
    })

  #fig = plt.figure(figsize=(10.5, 8.8))
  fig = plt.figure(num='AiJungEum', figsize=(10.5, 8.8))
  ax = fig.add_subplot(111, projection="3d")

  fig.patch.set_facecolor("#0B0D17")
  ax.set_facecolor("#0B0D17")

  steps_per_stage = 28
  hold_frames = 20
  phase_frames = (len(stages) - 1) * steps_per_stage + hold_frames
  total_cycle_frames = phase_frames * 2

  def update(global_frame):
    cycle_frame = global_frame % total_cycle_frames

    ax.cla()
    ax.set_facecolor("#0B0D17")

    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.grid(True, color="#1E243B", linestyle="--", linewidth=0.5)
    ax.tick_params(colors="#8A94B8", labelsize=8)

    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-1.15, 1.15)
    ax.set_zlim(-0.1, 1.15)
    ax.set_xlabel(
        "Component Axis X (ja1 / ja3)",
        color="#B8C4E6",
        fontproperties=ACTIVE_FONT_PROP,
    )
    ax.set_ylabel(
        "Component Axis Y (ja2 / ja4)",
        color="#B8C4E6",
        fontproperties=ACTIVE_FONT_PROP,
    )
    ax.set_zlabel(
        "Hierarchy / Time Axis (t)",
        color="#FFD166",
        # fontweight="bold",
        fontproperties=ACTIVE_FONT_PROP,
    )

    ax.plot(
        (0, 0),
        (0, 0),
        (-0.1, 1.05),
        color="#FFD166",
        linestyle=":",
        linewidth=1.2,
        alpha=0.5,
    )

    active_span = (len(stages) - 1) * steps_per_stage

    if cycle_frame < phase_frames:
      local_t = cycle_frame
      stage_idx = min(local_t // steps_per_stage, len(stages) - 1)
      total_prog = min(1.0, local_t / max(1, active_span))
      curr_stage = stages[stage_idx]

      x, y, z, c, chars = compute_galactic_vortex_arms(
          curr_stage["arms"],
          curr_stage["arm_chars"],
          time_t=local_t,
          total_progress=total_prog,
          is_cw_tornado=False,
      )

      base_size = max(6, min(140, 8000 / max(1, len(x))))
      ax.scatter(
          x,
          y,
          z,
          c=c,
          cmap="twilight_shifted",
          s=base_size,
          alpha=0.85,
          vmin=0.0,
          vmax=1.0,
          edgecolors="none",
      )

      final_ch = stages[-1]["rep_char"]
      if total_prog >= 0.92:
        ax.scatter(
            (0,),
            (0,),
            (1.0,),
            color="#FFFFFF",
            s=280,
            alpha=0.95,
            edgecolors="#FFD166",
            linewidths=2,
        )
        singularity_font = get_aje_font_prop(final_ch)
        ax.text(
            0,
            0,
            1.08,
            f"특이점 도달: {final_ch} ({hex(ord(final_ch))})",
            fontproperties=singularity_font,
            fontsize=14,
            # fontweight="bold",
            color="#FFD166",
            ha="center",
        )

      mode_title = (
          f"> [1회차: 순방향 수렴] Frame {global_frame} (수렴률"
          f" {total_prog*100:.1f}%) | {curr_stage['title']}"
      )

    else:
      local_t = cycle_frame - phase_frames
      emit_prog = min(1.0, local_t / max(1, active_span))

      rev_stage_idx = max(0, (len(stages) - 1) - (local_t // steps_per_stage))
      curr_stage = stages[rev_stage_idx]

      x, y, z, c, chars = compute_galactic_vortex_arms(
          curr_stage["arms"],
          curr_stage["arm_chars"],
          time_t=local_t,
          total_progress=emit_prog,
          is_cw_tornado=True,
      )

      base_size = max(6, min(140, 8200 / max(1, len(x))))
      ax.scatter(
          x,
          y,
          z,
          c=c,
          cmap="viridis",
          s=base_size,
          alpha=0.88,
          vmin=0.0,
          vmax=1.0,
          edgecolors="none",
      )

      ax.scatter(
          (0,),
          (0,),
          (1.0,),
          color="#00F5D4",
          s=180,
          alpha=0.85,
          edgecolors="#FFFFFF",
          linewidths=1.5,
      )

      mode_title = (
          f"< [2회차: 시계방향 방출] Frame {global_frame} (확장률"
          f" {emit_prog*100:.1f}%) | {curr_stage['title']}"
      )

    # ==========================================
    # [stdin 입력 기반 PUA 출력 제어]
    # ==========================================
    if pua_mode != "none" and len(x) > 0:
      rem_frame = global_frame % pua_interval
      should_render_pua = (pua_mode == "always") or (
          rem_frame < PUA_SHOW_FRAMES
      )

      if should_render_pua:
        stride = max(1, len(x) // MAX_PUA_LABELS)
        sample_idxs = range(0, len(x), stride)

        if pua_mode == "always" or rem_frame == 0:
          sample_str = " ".join(chars[i] for i in list(sample_idxs)[:24])
          print(
              f"[Frame {global_frame} | PUA] {curr_stage['title']} ->"
              f" {sample_str}"
          )

        for idx in sample_idxs:
          ch = chars[idx]
          pua_font = get_aje_font_prop(ch)
          ax.text(
              x[idx],
              y[idx],
              z[idx],
              ch,
              fontproperties=pua_font,
              fontsize=11,
              color="#FFFFFF",
              alpha=0.95,
              ha="center",
              va="center",
          )

        status_tag = (
            "상시 출력 중"
            if pua_mode == "always"
            else f"{pua_interval}프레임 주기"
        )
        mode_title += f"  ★ [PUA {status_tag}]"

    elev_angle = 32 + 12 * np.sin(global_frame * 0.03)
    ax.view_init(elev=elev_angle, azim=global_frame * 1.1)

    title_font = get_aje_font_prop(curr_stage["rep_char"])
    ax.set_title(
        f"AiJungEum Vortex - Raw Prime Data\n{mode_title}",
        fontsize=11.5,
        pad=14,
        color="#FFFFFF",
        fontproperties=title_font,
    )

  anim = FuncAnimation(
      fig,
      update,
      frames=itertools.count(),
      interval=frame_interval_ms,
      repeat=False,
      cache_frame_data=False,
  )
  plt.tight_layout()
  plt.show()
  return anim


# ==========================================
# 6. 터미널 stdin 옵션 입력기
# ==========================================
def get_stdin_pua_options():
  print("\n" + "=" * 60)
  print(" [AI정음 은하수 소용돌이(AiJungEum Galactic Vortex) - 실행 옵션 설정]")
  print("  1. PUA 없이 그냥 실행 (입자 그래픽만 출력, Default)")
  print("  2. PUA 항상 출력 (매 프레임마다 계속 표시)")
  print("  3. PUA 주기적 출력 (지정)")
  print("=" * 60)

  mode_in = input("실행 모드를 선택하세요 [1, 2, 3 | 기본값=1]: ").strip()

  if mode_in == "2":
    pua_mode = "always"
    interval = 1
    mode_desc = "PUA 항상 출력"
  elif mode_in == "3":
    pua_mode = "periodic"
    int_in = input(
        "몇 프레임마다 PUA를 표시할까요? (예: 100 또는 1000, 기본값=100): "
    ).strip()
    interval = int(int_in) if int_in.isdigit() and int(int_in) > 0 else 100
    mode_desc = f"PUA 주기적 출력 ({interval}프레임마다)"
  else:
    pua_mode = "none"
    interval = 100
    mode_desc = "PUA 없이 그냥 실행"

  speed_in = input(
      "애니메이션 속도를 입력하세요 (프레임당 ms, 낮을수록 빠름 | 예: 10=빠름,"
      " 45=보통, 150=느림 | 기본값=45): "
  ).strip()
  frame_ms = int(speed_in) if speed_in.isdigit() and int(speed_in) > 0 else 45

  print(f"-> [설정 완료] {mode_desc} | 재생 속도: {frame_ms}ms/frame\n")
  return pua_mode, interval, frame_ms


if __name__ == "__main__":
  primes_list, aje_base_list, hierarchy_groups = build_hierarchy()
  opt_mode, opt_interval, opt_speed = get_stdin_pua_options()
  ani = run_galactic_vortex_simulation(
      primes_list,
      aje_base_list,
      hierarchy_groups,
      pua_mode=opt_mode,
      pua_interval=opt_interval,
      frame_interval_ms=opt_speed,
  )



