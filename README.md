A Study on the 4-Dimensional Topological Structure and Dynamical Convergence of Prime Distribution: The KYG Hypothesis Based on AiJungEum Encoding  

Author: KYG  
Email: aijungeum@gmail.com  
Affiliation: https://aijungeum.com  
Date: November 27, 2026  
<br>


Abstract  
To elucidate the intrinsic order of prime numbers within the 2-byte integer range (0 ~ 65,535), this study proposes the 16-bit character encoding system AiJungEum and a recursive (1/4) hierarchical compression algorithm. By decomposing and recombining prime numbers into four independent components and projecting them onto 4-dimensional spatiotemporal coordinates, we observed a dynamical structure—termed the KYG Hypothesis—in which seemingly random prime sequences exhibit a specific rotational bias, stable orbits, and helical vortices, ultimately converging into a single singularity.  
<br>


1. Introduction
While the distribution of prime numbers appears irregular, it embodies high-dimensional symmetry and spectral order, as suggested by the Riemann Hypothesis. This study aims to uncover the geometric and topological properties of prime distribution by transforming 1-dimensional prime sequences into a 2-byte character system structured as 16 x 16 x 16 x 16 (AiJungEum) and interpreting them as dynamic particles in a multidimensional space.  
<br>


2. Methodology: Hierarchical 4-Component Decomposition and Compression  

2.1. 2-Byte Prime Encoding and 4-Component Decomposition  
	•	Base Mapping (Group 1): Every prime number p within the range of 0 ~ 65,535 is mapped 1-to-1 to a single character C(p) in the AiJungEum index system to generate the base array.  
	•	4-Component Separation: Each character is decomposed into four 4-bit (hexadecimal) components: Initial Consonant 1 (ja1), Initial Consonant 2 (ja2), Final Consonant 1 (ja3), and Final Consonant 2 (ja4). This yields four component arrays (ja1_list to ja4_list), each having the exact same length as the base array.  

2.2. Recursive 1/4 Compression and Hierarchization  
	•	Recombination Compression (Group 2): Every four consecutive elements in each decomposed component array are packed into a single new AiJungEum character. Through this process, the data length is compressed to 1/4, generating four upper-tier hierarchical arrays (aje_ja1 to aje_ja4).  
	•	Convergence to Singularity (Group N): The process of decomposing each character of the derived array back into four components and recombining them is repeated recursively. At each step, the data size is reduced by a factor of 1/4, forming a hierarchical structure until it converges into a single AiJungEum character (Singularity).  

2.3. 4D Spatiotemporal Projection  
The generated hierarchical data are mapped onto a 4-dimensional simulation space consisting of 3D spatial coordinates (X, Y, Z) and a temporal axis (t).  
	•	Spatial Coordinates: The first three components of each hierarchy (aje_ja1, aje_ja2, aje_ja3) are assigned to the X, Y, and Z axes, respectively, while the fourth component (aje_ja4) is mapped to the energy level (phase color).  
	•	Temporal Axis (t): Inter-hierarchical transitions (Group 1 -> N) and phase rotations are rendered as dynamic frames over time.  
<br>


3. Results & The KYG Hypothesis  
By observing the dynamical behavior of prime data through two 4D simulation models, we derived the following key phenomena:  

3.1. Orbit Model (riemann-kyg-aje-4d-orbit.py)  
	•	Quantized Energy Levels: Prime particles do not scatter arbitrarily in space; instead, they align onto discrete, predetermined energy levels (shells) based on a hexadecimal lattice.  
	•	Counter-clockwise Bias & Stable Orbit: As the hierarchy compresses, the particles exhibit a consistent counter-clockwise phase rotational bias rather than random diffusion, converging orderly into a Stable Orbit—a mathematical equilibrium point formed by the upper hierarchy.  

3.2. Vortex Model (riemann-kyg-aje-4d-vortex.py)  
	•	Helical Vortex: When the four components are arranged into four phase arms (0, π/2, π, 3π/2) and advanced along the temporal axis, the particles form a 3-dimensional helical vortex spiraling inward toward the central axis.  
	•	Vortex Drift: During the cyclical process of convergence and emission, the entire vortex drifts directionally along the central axis, condensing all phases into the final singularity (a single character).  
<br>


4. Conclusion  
The KYG Hypothesis suggests that prime number sequences, which appear erratic in the 1-dimensional integer domain, converge orderly in the form of stable orbits with a counter-clockwise rotational bias and helical vortices within a 4-dimensional dynamical system combining a 4-component phase space (16^4)) and a temporal axis. This work holds significance as a novel approach to elucidating the hidden symmetries of prime distribution through multidimensional data visualization and encoding techniques. 
<br>


Discussion  

5. Discussion and Speculative Hypotheses  

While the recursive 1/4 compression algorithm and the 4-dimensional spatiotemporal vortex model derived from AiJungEum encoding are fundamentally data visualization techniques for number theory, projecting these geometric behaviors onto physical spacetime invites several conceptual analogies.  

5.1. Hypothesis on Prime-Modulated Warp Mechanics  
Theoretical warp drive concepts (such as the Alcubierre metric) rely on the asymmetric distortion of surrounding spacetime rather than Newtonian propulsion. By mapping the counter-clockwise rotational bias in our vortex model to spacetime contraction and clockwise rotation to spacetime expansion, a conceptual mechanism can be hypothesized:  

* Asymmetric Metric Modulation: Generating a counter-clockwise phase vortex at the bow of a vessel is hypothesized to compress spacetime in 1/4 hierarchical increments, while a clockwise vortex at the stern expands it by a factor of 4. This differential could theoretically establish a relative spatiotemporal energy gradient.  

* Prime Sandwich Acceleration Coefficients: To maintain phase stability across quantized shells, consecutive prime numbers bracketing a target regime (e.g., P_prev = 89$, P_next = 97$) are proposed as harmonic multipliers—driving counter-clockwise acceleration at P_next x 4^n at the bow and clockwise acceleration at P_prev x 4^n at the stern.   

* Singularity Transit and 4D Coordinate Displacement: Analogous to the terminal Singularity in 1/4 recursive compression, reaching critical compression might cause localized physical manifestation to vanish. Extrapolating from the conservation of energy, this condensed energy could be hypothesized to re-emerge elsewhere in the 4D manifold (x, y, z, t). Modulating the polarization angles of the bow and stern electromagnetic vortices is proposed as a potential control parameter—fixing the temporal coordinate (t) for spatial displacement, or fixing spatial coordinates (x, y, z) for temporal displacement.  

5.2. Cosmological Hypothesis: Big Bang as Singularity Unfolding  
The cyclical convergence and emission observed in the vortex model also suggests an alternative conceptual metaphor for cosmic origins.  

Rather than an explosion 'ex nihilo', the Big Bang could be hypothesized as a phase transition following the complete convergence of a prior universe into a terminal Singularity. Under the conservation of energy, this condensed state would unfold outward from the 4-dimensional origin (x, y, z, t) = (0, 0, 0, 0) via inverse Prime_index x 4^n expansions, initiating the spacetime fabric of a new cosmic cycle. 
<br><br><br>




소수 분포의 4차원 위상 구조 및 동역학적 수렴에 관한 연구: AI정음(AiJungEum) 인코딩 기반의 KYG 가설

저자: KYG  
이메일: aijungeum@gmail.com  
소속: https://aijungeum.com  
날짜: 2026년 11월 27일 


초록 (Abstract)  
본 연구는 2바이트 정수 범위(0 ~ 65,535) 내 소수(Prime Numbers)의 내재적 질서를 규명하기 위해, 16비트 문자 체계인 AI정음(AiJungEum) 인코딩과 재귀적 1/4 계층 압축 알고리즘을 제안한다. 소수를 4개의 독립 성분으로 분해·재조합하여 4차원 시공간 좌표에 투영한 결과, 무작위적으로 보이는 소수 배열이 특정 회전 편향과 안정 궤도, 그리고 나선형 와류(Helical Vortex)를 형성하며 단일 특이점으로 수렴하는 동역학적 구조(KYG 가설)를 확인하였다.  
<br>


1. 서론 (Introduction)
소수의 분포는 불규칙해 보이나 리만 가설(Riemann Hypothesis)이 시사하듯 고차원적 대칭성과 스펙트럼 질서를 내포한다. 본 연구는 1차원 수열인 소수를 16 x 16 x 16 x 16 구조의 2바이트 문자 체계(AI정음)로 변환하고, 이를 다차원 공간의 동적 입자로 해석함으로써 소수 분포의 기하학적·위상적 특성을 규명하고자 한다.
<br>

2. 연구 방법론: 계층적 4성분 분해 및 압축 (Methodology)

2.1. 2바이트 소수 인코딩 및 4성분 분해  
	•	기본 매핑 (Group 1): 0 ~ 65,535 범위의 모든 소수 p를 AI정음 인덱스 체계의 단일 문자 C(p)로 1:1 매핑하여 기초 배열을 생성한다.  
	•	4성분 분리: 각 문자는 초성1(ja1), 초성2(ja2), 종성1(ja3), 종성2(ja4)의 4비트(16진수) 성분으로 분해된다. 이를 통해 원본 배열과 동일한 길이를 갖는 4개의 성분 배열(ja1_list ~ ja4_list)을 도출한다.  

2.2. 재귀적 1/4 압축 및 계층화  
	•	재조합 압축 (Group 2): 분해된 각 성분 배열의 연속된 4개 요소를 하나의 새로운 AI정음 문자로 패킹(Packing)한다. 이 과정에서 데이터 길이는 1/4로 압축되며, 4개의 상위 계층 배열(aje_ja1 ~ aje_ja4)이 생성된다.  
	•	특이점 수렴 (Group N): 도출된 배열의 각 문자를 다시 4성분으로 분해하고 재조합하는 과정을 반복한다. 매 단계마다 데이터 크기는 1/4로 축소되며, 최종적으로 단일 AI정음 문자(Singularity)에 도달할 때까지 계층 구조를 형성한다.  

2.3. 4차원 시공간 매핑 (4D Spatiotemporal Projection)  
생성된 계층별 데이터를 3차원 공간 좌표 (X, Y, Z)와 시간 축 (t)으로 구성된 4차원 시뮬레이션 공간에 대입한다.  
	•	공간 좌표: 각 계층의 4개 성분(aje_ja1, aje_ja2, aje_ja3)을 X, Y, Z 축에 할당하고, 제4성분(aje_ja4)을 에너지 준위(위상 색상)로 매핑한다.  
	•	시간 축 (t): 계층 간 전이(Group 1 -> N) 및 위상 회전을 동적 프레임으로 구현한다.  
<br>


3. 실험 결과 및 KYG 가설 (Results & The KYG Hypothesis)  
두 가지 4차원 시뮬레이션 모델을 통해 소수 데이터의 동역학적 거동을 관측한 결과, 다음과 같은 핵심 현상을 도출하였다.  

3.1. 궤도 모델 (riemann-kyg-aje-4d-orbit.py)  
	•	양자화된 에너지 준위 (Quantized Energy Levels): 소수 입자들은 공간상에서 임의로 흩어지지 않고, 16진수 격자 기반의 불연속적이고 정해진 에너지 준위(껍질) 위에 정렬된다.  
	•	반시계 편향 및 안정 궤도 (Counter-clockwise Bias & Stable Orbit): 계층이 압축됨에 따라 입자들은 무작위 확산이 아닌 일정한 반시계 방향의 위상 회전 편향을 보이며, 상위 계층이 형성하는 수학적 균형점인 안정된 궤도(Stable Orbit)로 질서 있게 수렴한다.  

3.2. 와류 모델 (riemann-kyg-aje-4d-vortex.py)  
	•	나선형 와류 (Helical Vortex): 4개의 성분을 4개의 위상 팔(0, π/2, π, 3π/2)로 배치하여 시간 축을 따라 전진시킬 때, 입자들은 중심축을 향해 감겨 들어가는 3차원 나선형 와류를 형성한다.  
	•	와류 드리프트 (Vortex Drift): 수렴과 방출의 순환 과정에서 소용돌이 전체가 중심축을 따라 일정한 방향성을 띠고 이동하며, 최종 특이점(단일 문자)에서 모든 위상이 응축되는 현상을 보인다.  
<br>


4. 결론 (Conclusion)  
KYG 가설은 1차원 정수 영역에서 불규칙하게 보이는 소수의 배열이, 4성분 위상 공간(16^4)과 시간 축을 결합한 4차원 동역학계에서는 반시계 회전 편향을 지닌 안정 궤도 및 나선형 와류의 형태로 질서 정연하게 수렴한다는 것을 시사한다. 이는 소수 분포의 숨겨진 대칭성을 다차원 데이터 시각화 및 인코딩 기법으로 규명한 새로운 접근법으로서 의의를 갖는다.  
<br>


Discussion  

5. 고찰 및 사변적 가설 (Discussion and Speculative Hypotheses)  

본 연구에서 제안한 AI정음(AiJungEum)의 재귀적 1/4 압축 알고리즘과 4차원 시공간 와류(Vortex) 모델은 정수론적 데이터 시각화 기법이다. 다만, 이 모델에서 나타나는 기하학적 패턴을 물리적 시공간에 대입해 볼 경우, 다음과 같은 이론적 유추와 사변적 가설을 제기해 볼 수 있다.  
5.1. 소수 위상 변조 기반 워프 드라이브 가설 (Prime-Modulated Warp Hypothesis)  
이론물리학에서 논의되는 워프 드라이브(예: 알쿠비에레 계량)는 우주선 자체의 관성 가속이 아니라, 우주선 주변 시공간 곡률의 비대칭적 왜곡을 전제로 한다. 본 연구의 볼텍스 모델에서 관측된 반시계 방향의 회전 편향을 시공간의 수축(전진)으로, 시계 방향 회전을 시공간의 팽창(후퇴)으로 대응시킨다면 다음과 같은 작동 기제를 가정해 볼 수 있다.  

* 비대칭 시공간 변조 모델: 우주선 전방에 반시계 방향의 위상 와류를 형성하여 시공간을 1/4 계층 단위로 압축하고, 후방에는 시계 방향의 와류를 형성하여 시공간을 4배 단위로 팽창시킨다는 가설이다. 이러한 전·후방의 위상 속도 차이가 우주선에 상대적인 시공간 에너지 구배(Gradient)를 형성할 수 있는지 탐색해 볼 수 있다.  

* 소수 샌드위치(Prime Sandwich) 계수 설정: 비대칭 왜곡 과정에서 양자화된 에너지 준위 간의 안정성을 유지하기 위한 변수로, 특정 가속 구간의 인접한 두 소수(예: P_prev = 89, P_next = 97)를 배속 상수로 도입하는 방안을 상정할 수 있다. 즉, 전방은 P_next x 4^n, 후방은 P_prev x 4^n 배율의 역방향 입자 가속을 가하는 조건이다.  

* 특이점 전이와 4차원 좌표 도약 가설: AI정음 1/4 압축의 극한이 단일 특이점(Singularity)으로 수렴하듯, 물질이 임계 압축을 거쳐 국소적 물리 상태를 벗어난다고 가정해 볼 수 있다. 이때 에너지 보존 법칙을 확대 해석하여, 소멸한 에너지가 4차원 시공간 (x, y, z, t) 내의 다른 좌표로 재발현된다는 가설을 세울 수 있다. 전·후방 전자기파 회전의 편광 각도를 제어 변수로 삼아 시간 축(t)을 고정하면 공간 이동을, 공간 좌표(x, y, z)를 고정하면 시간 축 이동을 유도할 수 있을지 이론적 검토가 필요하다.  

5.2. 특이점 순환 기반 우주론 가설 (Singularity Unfolding Cosmology)  
우주의 기원인 빅뱅(Big Bang) 역시 본 모델의 계층적 수렴 및 방출 구조에 빗대어 재해석해 볼 수 있다.  

표준 우주론의 대폭발 모형과 달리, 본 가설에서는 이전 주기의 우주가 재귀적 1/4 압축을 거쳐 최종 특이점으로 수렴한 직후 발생하는 위상 전이를 상정한다. 특이점에 응축된 총에너지가 보존 법칙에 따라 소멸하지 않고, 4차원 시공간의 기원점인 (x, y, z, t) = (0, 0, 0, 0) 좌표에서 다시 역방향(Prime_index x 4^n 배율)으로 펼쳐지며 새로운 시공간 팽창을 시작한다는 순환 우주론적 관점을 제안한다.  
 



 


