A Study on the 4-Dimensional Topological Structure and Dynamical Convergence of Prime Distribution: The KYG Hypothesis Based on AiJungEum Encoding
Author: KYG
Email: aijungeum@gmail.com
Affiliation: https://aijungeum.com
Date: November 27, 2026



Abstract
To elucidate the intrinsic order of prime numbers within the 2-byte integer range (0 ~ 65,535), this study proposes the 16-bit character encoding system AiJungEum and a recursive (1/4) hierarchical compression algorithm. By decomposing and recombining prime numbers into four independent components and projecting them onto 4-dimensional spatiotemporal coordinates, we observed a dynamical structure—termed the KYG Hypothesis—in which seemingly random prime sequences exhibit a specific rotational bias, stable orbits, and helical vortices, ultimately converging into a single singularity.



1. Introduction
While the distribution of prime numbers appears irregular, it embodies high-dimensional symmetry and spectral order, as suggested by the Riemann Hypothesis. This study aims to uncover the geometric and topological properties of prime distribution by transforming 1-dimensional prime sequences into a 2-byte character system structured as 16 x 16 x 16 x 16 (AiJungEum) and interpreting them as dynamic particles in a multidimensional space.



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



3. Results & The KYG Hypothesis
By observing the dynamical behavior of prime data through two 4D simulation models, we derived the following key phenomena:

3.1. Orbit Model (riemann-kyg-aje-4d-orbit.py)
	•	Quantized Energy Levels: Prime particles do not scatter arbitrarily in space; instead, they align onto discrete, predetermined energy levels (shells) based on a hexadecimal lattice.
	•	Counter-clockwise Bias & Stable Orbit: As the hierarchy compresses, the particles exhibit a consistent counter-clockwise phase rotational bias rather than random diffusion, converging orderly into a Stable Orbit—a mathematical equilibrium point formed by the upper hierarchy.

3.2. Vortex Model (riemann-kyg-aje-4d-vortex.py)
	•	Helical Vortex: When the four components are arranged into four phase arms (0, π/2, π, 3π/2) and advanced along the temporal axis, the particles form a 3-dimensional helical vortex spiraling inward toward the central axis.
	•	Vortex Drift: During the cyclical process of convergence and emission, the entire vortex drifts directionally along the central axis, condensing all phases into the final singularity (a single character).



4. Conclusion
The KYG Hypothesis suggests that prime number sequences, which appear erratic in the 1-dimensional integer domain, converge orderly in the form of stable orbits with a counter-clockwise rotational bias and helical vortices within a 4-dimensional dynamical system combining a 4-component phase space (16^4)) and a temporal axis. This work holds significance as a novel approach to elucidating the hidden symmetries of prime distribution through multidimensional data visualization and encoding techniques.





소수 분포의 4차원 위상 구조 및 동역학적 수렴에 관한 연구: AI정음(AiJungEum) 인코딩 기반의 KYG 가설

저자: KYG
이메일: aijungeum@gmail.com
소속: https://aijungeum.com 
날짜: 2026년 11월 27일 


초록 (Abstract)
본 연구는 2바이트 정수 범위(\(0 \sim 65,535\)) 내 소수(Prime Numbers)의 내재적 질서를 규명하기 위해, 16비트 문자 체계인 AI정음(AiJungEum) 인코딩과 재귀적 \(1/4\) 계층 압축 알고리즘을 제안한다. 소수를 4개의 독립 성분으로 분해·재조합하여 4차원 시공간 좌표에 투영한 결과, 무작위적으로 보이는 소수 배열이 특정 회전 편향과 안정 궤도, 그리고 나선형 와류(Helical Vortex)를 형성하며 단일 특이점으로 수렴하는 동역학적 구조(KYG 가설)를 확인하였다.



1. 서론 (Introduction)
소수의 분포는 불규칙해 보이나 리만 가설(Riemann Hypothesis)이 시사하듯 고차원적 대칭성과 스펙트럼 질서를 내포한다. 본 연구는 1차원 수열인 소수를 \(16 \times 16 \times 16 \times 16\) 구조의 2바이트 문자 체계(AI정음)로 변환하고, 이를 다차원 공간의 동적 입자로 해석함으로써 소수 분포의 기하학적·위상적 특성을 규명하고자 한다.

2. 연구 방법론: 계층적 4성분 분해 및 압축 (Methodology)

2.1. 2바이트 소수 인코딩 및 4성분 분해
	•	기본 매핑 (Group 1): \(0 \sim 65,535\) 범위의 모든 소수 \(p\)를 AI정음 인덱스 체계의 단일 문자 \(C(p)\)로 1:1 매핑하여 기초 배열을 생성한다.
	•	4성분 분리: 각 문자는 초성1(\(ja_{1}\)), 초성2(\(ja_{2}\)), 종성1(\(ja_{3}\)), 종성2(\(ja_{4}\))의 4비트(16진수) 성분으로 분해된다. 이를 통해 원본 배열과 동일한 길이를 갖는 4개의 성분 배열(ja1_list ~ ja4_list)을 도출한다.

2.2. 재귀적 \(1/4\) 압축 및 계층화
	•	재조합 압축 (Group 2): 분해된 각 성분 배열의 연속된 4개 요소를 하나의 새로운 AI정음 문자로 패킹(Packing)한다. 이 과정에서 데이터 길이는 \(1/4\)로 압축되며, 4개의 상위 계층 배열(aje_ja1 ~ aje_ja4)이 생성된다.
	•	특이점 수렴 (Group \(N\)): 도출된 배열의 각 문자를 다시 4성분으로 분해하고 재조합하는 과정을 반복한다. 매 단계마다 데이터 크기는 \(1/4\)로 축소되며, 최종적으로 단일 AI정음 문자(Singularity)에 도달할 때까지 계층 구조를 형성한다.

2.3. 4차원 시공간 매핑 (4D Spatiotemporal Projection)
생성된 계층별 데이터를 3차원 공간 좌표 \((X, Y, Z)\)와 시간 축 \((t)\)으로 구성된 4차원 시뮬레이션 공간에 대입한다.
	•	공간 좌표: 각 계층의 4개 성분(aje_ja1, aje_ja2, aje_ja3)을 \(X, Y, Z\) 축에 할당하고, 제4성분(aje_ja4)을 에너지 준위(위상 색상)로 매핑한다.
	•	시간 축 (\(t\)): 계층 간 전이(Group \(1 \rightarrow N\)) 및 위상 회전을 동적 프레임으로 구현한다.



3. 실험 결과 및 KYG 가설 (Results & The KYG Hypothesis)
두 가지 4차원 시뮬레이션 모델을 통해 소수 데이터의 동역학적 거동을 관측한 결과, 다음과 같은 핵심 현상을 도출하였다.

3.1. 궤도 모델 (riemann-kyg-aje-4d-orbit.py)
	•	양자화된 에너지 준위 (Quantized Energy Levels): 소수 입자들은 공간상에서 임의로 흩어지지 않고, 16진수 격자 기반의 불연속적이고 정해진 에너지 준위(껍질) 위에 정렬된다.
	•	반시계 편향 및 안정 궤도 (Counter-clockwise Bias & Stable Orbit): 계층이 압축됨에 따라 입자들은 무작위 확산이 아닌 일정한 반시계 방향의 위상 회전 편향을 보이며, 상위 계층이 형성하는 수학적 균형점인 안정된 궤도(Stable Orbit)로 질서 있게 수렴한다.

3.2. 와류 모델 (riemann-kyg-aje-4d-vortex.py)
	•	나선형 와류 (Helical Vortex): 4개의 성분을 4개의 위상 팔(\(0, \pi/2, \pi, 3\pi/2\))로 배치하여 시간 축을 따라 전진시킬 때, 입자들은 중심축을 향해 감겨 들어가는 3차원 나선형 와류를 형성한다.
	•	와류 드리프트 (Vortex Drift): 수렴과 방출의 순환 과정에서 소용돌이 전체가 중심축을 따라 일정한 방향성을 띠고 이동하며, 최종 특이점(단일 문자)에서 모든 위상이 응축되는 현상을 보인다.



4. 결론 (Conclusion)
KYG 가설은 1차원 정수 영역에서 불규칙하게 보이는 소수의 배열이, 4성분 위상 공간(\(16^{4}\))과 시간 축을 결합한 4차원 동역학계에서는 반시계 회전 편향을 지닌 안정 궤도 및 나선형 와류의 형태로 질서 정연하게 수렴한다는 것을 시사한다. 이는 소수 분포의 숨겨진 대칭성을 다차원 데이터 시각화 및 인코딩 기법으로 규명한 새로운 접근법으로서 의의를 갖는다.





 


