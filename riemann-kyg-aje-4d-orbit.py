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

import math
import os
import platform
from matplotlib.animation import FuncAnimation
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider
from mpl_toolkits.mplot3d import proj3d
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# ==========================================
# 기본 설정 및 AiJungEum 폰트 로더 
# ==========================================
FONT_PATH = "AiJungEum_0.1.a2.ttc"
DEFAULT_SPEED = 1.0  # 초기 재생 배속

PUA_A_START = 0xF0000
PUA_A_LIMIT = 0xF7FFF   # 32,768개 (aijungeum_part1)
PUA_B_START = 0x100000
PUA_B_LIMIT = 0x107FFF  # 32,768개 (aijungeum_part2)
JUMP_THRESHOLD = 0x8000
MAX_LINEAR_VAL = 65535.0


class AjeGlyphRenderer:
  """AiJungEum_0.1.a2.ttc 폰트 랜더링
  """

  def __init__(self, font_path: str):
    if not os.path.exists(font_path):
      raise FileNotFoundError(
          f"font err: '{font_path}' (스크립트와 같은 폴더에 위치시켜 주세요) \nFont Down: https://github.com/aijungeum/font-aijungeum/tree/main/_output/261126"
      )

    self.font_path = font_path
    self.part1_idx = 0
    self.part2_idx = 1

    try:
      from fontTools.ttLib import TTCollection

      ttc = TTCollection(font_path)
      for idx, f in enumerate(ttc.fonts):
        name_records = [
            r.toUnicode()
            for r in f["name"].names
            if r.nameID in (1, 4, 6)
        ]
        full_name = " ".join(name_records).lower()
        cmap = f.getBestCmap() or {}
        has_pua_a = any(PUA_A_START <= cp <= PUA_A_LIMIT for cp in cmap)
        has_pua_b = any(PUA_B_START <= cp <= PUA_B_LIMIT for cp in cmap)

        if "part1" in full_name or (has_pua_a and not has_pua_b):
          self.part1_idx = idx
        elif "part2" in full_name or (has_pua_b and not has_pua_a):
          self.part2_idx = idx

        print(
            f"  - TTC Face[{idx}]: {name_records if name_records else 'Unknown'} "
            f"(PUA_A={has_pua_a}, PUA_B={has_pua_b})"
        )
    except ImportError:
      for idx in (0, 1):
        try:
          f_test = ImageFont.truetype(font_path, size=16, index=idx)
          fam_name = " ".join(f_test.getname()).lower()
          if "part1" in fam_name:
            self.part1_idx = idx
          elif "part2" in fam_name:
            self.part2_idx = idx
        except Exception:
          pass

    print(
        f"[이중 폰트 매핑 완료] aijungeum_part1 -> index={self.part1_idx} | "
        f"aijungeum_part2 -> index={self.part2_idx}"
    )

    self._font_cache = {}
    self._glyph_cache = {}

  def _get_font_for_cp(self, cp: int, px_size: int):
    face_idx = (
        self.part1_idx if PUA_A_START <= cp <= PUA_A_LIMIT else self.part2_idx
    )
    key = (face_idx, px_size)
    if key not in self._font_cache:
      self._font_cache[key] = ImageFont.truetype(
          self.font_path, size=px_size, index=face_idx
      )
    return self._font_cache[key]

  def render_text_image(
      self, text: str, px_size: int = 28, color=(15, 15, 15, 255)
  ) -> np.ndarray:
    cache_key = (text, px_size, color)
    if cache_key in self._glyph_cache:
      return self._glyph_cache[cache_key]

    pad = max(4, px_size // 4)
    char_imgs = []

    for ch in text:
      cp = ord(ch)
      font = self._get_font_for_cp(cp, px_size)
      canvas = Image.new(
          "RGBA", (px_size * 2 + pad * 2, px_size * 2 + pad * 2), (0, 0, 0, 0)
      )
      draw = ImageDraw.Draw(canvas)
      draw.text((pad, pad), ch, font=font, fill=color)
      bbox = canvas.getbbox()
      if bbox:
        char_imgs.append(canvas.crop(bbox))

    if not char_imgs:
      empty = Image.new("RGBA", (8, 8), (0, 0, 0, 0))
      arr = np.asarray(empty)
      self._glyph_cache[cache_key] = arr
      return arr

    spacing = max(2, px_size // 8)
    total_w = sum(im.width for im in char_imgs) + spacing * (len(char_imgs) - 1)
    max_h = max(im.height for im in char_imgs)

    combined = Image.new("RGBA", (total_w, max_h), (0, 0, 0, 0))
    curr_x = 0
    for im in char_imgs:
      y_offset = (max_h - im.height) // 2
      combined.paste(im, (curr_x, y_offset), im)
      curr_x += im.width + spacing

    arr = np.asarray(combined)
    self._glyph_cache[cache_key] = arr
    return arr


def setup_fonts(pua_font_path: str) -> AjeGlyphRenderer:
  sys_name = platform.system()
  if sys_name == "Windows":
    plt.rcParams["font.family"] = "Malgun Gothic"
  elif sys_name == "Darwin":
    plt.rcParams["font.family"] = "AppleGothic"
  else:
    plt.rcParams["font.family"] = "NanumGothic"
  plt.rcParams["axes.unicode_minus"] = False

  return AjeGlyphRenderer(pua_font_path)


# ==========================================
# AiJungEum PUA 변환 함수 정의
# ==========================================
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
# 2바이트 범위(0 ~ 65535) 소수 생성, AiJungEum으로 변환 
# ==========================================
def generate_2byte_primes() -> list[int]:
  limit = 0xFFFF
  sieve = [True] * (limit + 1)
  sieve[0] = False
  sieve[1] = False
  for i in range(2, int(math.isqrt(limit)) + 1):
    if sieve[i]:
      sieve[i * i : limit + 1 : i] = [False] * len(range(i * i, limit + 1, i))
  return [i for i, is_p in enumerate(sieve) if is_p]


def decompose_to_4_components(aje_list: list[str]):
  ja1, ja2, ja3, ja4 = [], [], [], []
  for ch in aje_list:
    val = aje_to_index(ch)
    ja1.append((val >> 12) & 0xF)
    ja2.append((val >> 8) & 0xF)
    ja3.append((val >> 4) & 0xF)
    ja4.append(val & 0xF)
  return ja1, ja2, ja3, ja4


def pack_4_to_aje(ja_list: list[int]) -> list[str]:
  rem = len(ja_list) % 4
  if rem != 0:
    ja_list = ja_list + [0] * (4 - rem)

  aje_packed = []
  for i in range(0, len(ja_list), 4):
    c1, c2, c3, c4 = ja_list[i], ja_list[i + 1], ja_list[i + 2], ja_list[i + 3]
    combined_idx = (c1 << 12) | (c2 << 8) | (c3 << 4) | c4
    aje_packed.append(index_to_aje(combined_idx))
  return aje_packed


def build_hierarchy():
  primes = generate_2byte_primes()
  aje_base = [index_to_aje(p) for p in primes]

  groups = []
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
    })
    current_source = aje_ja1

  return primes, aje_base, groups




# ==========================================
# 원본 스케일 순수 4중 위상 회전 수렴 보간
# ==========================================
def structural_converge_interpolate(
    curr_x, curr_y, curr_z, next_x, next_y, next_z, alpha
):
  dx = curr_x - next_x
  dy = curr_y - next_y
  dz = curr_z - next_z

  decay = 1.0 - alpha
  theta = ((np.arange(len(curr_x)) % 4) + 1) * (np.pi / 2.0) * alpha

  cos_t = np.cos(theta)
  sin_t = np.sin(theta)

  rot_dx = (dx * cos_t - dy * sin_t) * decay
  rot_dy = (dx * sin_t + dy * cos_t) * decay
  rot_dz = dz * decay

  return next_x + rot_dx, next_y + rot_dy, next_z + rot_dz




# ==========================================
# 메인 시뮬레이션 및 실시간 속도 조절 UI
# ==========================================
def run_4d_pure_simulation(
    primes, aje_base, groups, glyph_renderer: AjeGlyphRenderer
):
  frames_data = []
  j1, j2, j3, j4 = decompose_to_4_components(aje_base)
  frames_data.append({
      "title": f"Group 1 (원본 소수 {len(primes)}개)",
      "x": np.array(j1, dtype=float) * 4369,
      "y": np.array(j2, dtype=float) * 4369,
      "z": np.array(j3, dtype=float) * 4369,
      "c": np.array(j4, dtype=float) * 4369,
      "chars": aje_base,
  })

  for g in groups:
    frames_data.append({
        "title": f"Group {g['group_num']} (1/4 압축 - 점 {g['length']}개)",
        "x": np.array([aje_to_index(ch) for ch in g["aje_ja1"]], dtype=float),
        "y": np.array([aje_to_index(ch) for ch in g["aje_ja2"]], dtype=float),
        "z": np.array([aje_to_index(ch) for ch in g["aje_ja3"]], dtype=float),
        "c": np.array([aje_to_index(ch) for ch in g["aje_ja4"]], dtype=float),
        "chars": g["aje_ja1"],
    })

  print("\n=== 계층별 AiJungEum PUA 코드포인트 요약 ===")
  for item in frames_data:
    hex_codes = " ".join(f"U+{ord(ch):X}" for ch in item["chars"][:4])
    suffix = " ..." if len(item["chars"]) > 4 else ""
    print(f"- {item['title']}: ({hex_codes}{suffix})")

  #fig = plt.figure(figsize=(10.5, 9.0))
  fig = plt.figure(num='AiJungEum', figsize=(10.5, 9.0))
  ax = fig.add_subplot(111, projection="3d")
  plt.subplots_adjust(bottom=0.16)

  scatter = ax.scatter(
      [], [], [], c=[], cmap="plasma", s=20, alpha=0.8, vmin=0, vmax=1
  )
  cbar = fig.colorbar(scatter, ax=ax, pad=0.1, shrink=0.68)
  cbar.set_label("4D Energy: aje_ja4 (Normalized)")

  interp_steps = 30
  hold_steps = 15
  total_frames = (len(frames_data) - 1) * interp_steps + hold_steps
  max_v = MAX_LINEAR_VAL

  state = {
      "v_frame": 0.0,
      "speed": DEFAULT_SPEED,
      "paused": False,
  }

  ax_speed = plt.axes([0.20, 0.05, 0.48, 0.03])
  speed_slider = Slider(
      ax=ax_speed,
      label="속도 (Speed) ",
      valmin=0.1,
      valmax=5.0,
      valinit=DEFAULT_SPEED,
      valstep=0.1,
      valfmt="%.1fx",
  )

  ax_btn = plt.axes([0.75, 0.045, 0.14, 0.04])
  pause_btn = Button(ax_btn, "일시정지 (Space)")

  def on_speed_change(val):
    state["speed"] = float(val)

  def toggle_pause(event=None):
    state["paused"] = not state["paused"]
    pause_btn.label.set_text("재생 (Space)" if state["paused"] else "일시정지 (Space)")
    fig.canvas.draw_idle()

  def on_key_press(event):
    if event.key == " ":
      toggle_pause()
    elif event.key == "up":
      speed_slider.set_val(min(5.0, round(state["speed"] + 0.2, 1)))
    elif event.key == "down":
      speed_slider.set_val(max(0.1, round(state["speed"] - 0.2, 1)))
    elif event.key == "right" and state["paused"]:
      state["v_frame"] = (state["v_frame"] + 1.0) % total_frames
      render_frame(state["v_frame"])
      fig.canvas.draw_idle()
    elif event.key == "left" and state["paused"]:
      state["v_frame"] = (state["v_frame"] - 1.0) % total_frames
      render_frame(state["v_frame"])
      fig.canvas.draw_idle()

  speed_slider.on_changed(on_speed_change)
  pause_btn.on_clicked(toggle_pause)
  fig.canvas.mpl_connect("key_press_event", on_key_press)

  def render_frame(v_frame):
    ax.cla()
    ax.set_xlim(0, max_v)
    ax.set_ylim(0, max_v)
    ax.set_zlim(0, max_v)
    ax.set_xlabel("X: aje_ja1 (0 ~ 65535)", fontweight="bold")
    ax.set_ylabel("Y: aje_ja2 (0 ~ 65535)", fontweight="bold")
    ax.set_zlabel("Z: aje_ja3 (0 ~ 65535)", fontweight="bold")

    stage = min(int(v_frame // interp_steps), len(frames_data) - 1)
    alpha = (
        (v_frame % interp_steps) / interp_steps
        if stage < len(frames_data) - 1
        else 0.0
    )

    curr_data = frames_data[stage]
    chars = curr_data["chars"]

    if stage < len(frames_data) - 1 and alpha > 0:
      next_data = frames_data[stage + 1]
      parent_idx = np.clip(
          np.arange(len(curr_data["x"])) // 4, 0, len(next_data["x"]) - 1
      )

      nx = next_data["x"][parent_idx]
      ny = next_data["y"][parent_idx]
      nz = next_data["z"][parent_idx]
      nc = next_data["c"][parent_idx]

      x, y, z = structural_converge_interpolate(
          curr_data["x"],
          curr_data["y"],
          curr_data["z"],
          nx,
          ny,
          nz,
          alpha,
      )
      c = (1 - alpha) * curr_data["c"] + alpha * nc
      stage_desc = f"4중 위상 수렴 중: {curr_data['title']} -> Group {stage+2}"
    else:
      x, y, z, c = (
          curr_data["x"],
          curr_data["y"],
          curr_data["z"],
          curr_data["c"],
      )
      stage_desc = curr_data["title"]

    ax.view_init(elev=26, azim=45 + v_frame * 0.9)

    point_size = max(15, min(320, 15000 / len(x)))
    ax.scatter(
        x,
        y,
        z,
        c=c / max_v,
        cmap="plasma",
        s=point_size,
        alpha=0.8,
        vmin=0,
        vmax=1,
        edgecolors="k",
        linewidths=0.2,
    )

    # [PUA 전용 비트맵 렌더링] part1 / part2 자동 선택 후 3D 투영 좌표에 부착
    if len(x) <= 64:
      px_size = 38 if len(x) == 1 else (24 if len(x) <= 16 else 18)
      x2d, y2d, _ = proj3d.proj_transform(x, y, z, ax.get_proj())
      for sx, sy, ch in zip(x2d, y2d, chars):
        glyph_img = glyph_renderer.render_text_image(ch, px_size=px_size)
        im = OffsetImage(glyph_img, zoom=0.75)
        ab = AnnotationBbox(
            im,
            (sx, sy),
            xybox=(0, 12),
            boxcoords="offset points",
            frameon=False,
        )
        ax.add_artist(ab)

    status_tag = "일시정지" if state["paused"] else f"{state['speed']:.1f}x"
    ax.set_title(
        f"AI정음(AiJungEum): 원본 스케일 순수 4중 위상 수렴 [{status_tag}]\nTime t={v_frame:.1f} | {stage_desc}",
        fontsize=11.5,
        pad=18,
    )

    # 좌측 상단 PUA 미리보기 박스 (part1 / part2 자동 합성 비트맵)
    preview_pua = "".join(chars[:10])
    preview_img = glyph_renderer.render_text_image(
        preview_pua, px_size=28, color=(0, 51, 153, 255)
    )
    im_preview = OffsetImage(preview_img, zoom=0.8)
    ab_preview = AnnotationBbox(
        im_preview,
        (0.03, 0.94),
        xycoords="axes fraction",
        box_alignment=(0.0, 0.5),
        bboxprops=dict(
            boxstyle="round,pad=0.35", facecolor="#F4F6FA", edgecolor="#CCCCCC"
        ),
    )
    ax.add_artist(ab_preview)

  def update(_tick):
    if not state["paused"]:
      state["v_frame"] = (state["v_frame"] + state["speed"]) % total_frames
      render_frame(state["v_frame"])

  render_frame(0.0)
  anim = FuncAnimation(
      fig, update, interval=40, blit=False, cache_frame_data=False
  )
  plt.title("AI정음")
  plt.show()
  return anim


if __name__ == "__main__":
  renderer = setup_fonts(FONT_PATH)
  primes_list, aje_base_list, hierarchy_groups = build_hierarchy()
  ani = run_4d_pure_simulation(
      primes_list, aje_base_list, hierarchy_groups, renderer
  )


