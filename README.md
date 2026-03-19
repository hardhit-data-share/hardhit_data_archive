# KBO 투수-수비 기여도 회귀분석

본 프로젝트는 KBO 리그 데이터를 기반으로  
팀 실점이 투수력과 수비력에 의해 어떻게 구성되는지를  
회귀분석을 통해 분해하는 것을 목표로 합니다.

---

## 📊 분석 개요

팀의 경기당 실점(R_G)을 다음과 같이 모델링합니다.

R_G = β₀ + β₁ × ERA + β₂ × Defense

- R_G: 경기당 실점 (Runs per Game)
- ERA: 9이닝당 자책점 (Earned Run Average)
- Defense: 수비 기여도 (RA9 - ERA)

---

## 🧩 수비력 정의

Defense = RA9 - ERA

- RA9: 9이닝당 평균 실점 (자책 + 비자책 포함)
- ERA: 투수 자책점
- Defense: 투수 책임으로 설명되지 않는 실점 (비자책점 등)

이 정의를 통해 실점을 다음과 같이 분해할 수 있습니다:

- ERA → 투수 책임
- Defense → 수비 및 기타 요인

---

## ⚙️ 분석 방법

- 선형 회귀 (Linear Regression) 사용
- 종속변수: R_G (경기당 실점)
- 독립변수: ERA, Defense
- 표준화 회귀계수를 통해 변수 간 상대적 영향력 비교

---

## 📈 주요 결과

- 투수력 (ERA): 약 85%
- 수비력 (Defense): 약 15%

즉, KBO에서 실점의 대부분은 투수력에 의해 결정되며,  
수비는 보조적인 역할을 하는 것으로 나타납니다.

---

## ⚠️ 해석에 대한 주의

본 분석은 자책점과 비자책점의 차이를 이용하여  
실점을 투수와 수비로 분해하는 방식입니다.

이는 엄밀한 인과 추정(causal inference)이 아니라,  
실점 구성 요소를 설명하기 위한 회귀 기반 분해 모델입니다.

또한 ERA와 Defense는 완전히 독립적인 변수가 아니므로  
표준화 계수의 절대값은 1을 초과할 수 있습니다.  
하지만 상대적 비율 비교에는 문제가 없습니다.

---

## 📁 파일 구성

- dataset_era_ra9.csv  
  KBO 시즌별 실점, 자책점, 이닝 등의 데이터

- regression_analysis.py  
  회귀 분석 수행 코드

---

## ▶️ 실행 방법

```bash
pip install pandas numpy scikit-learn
python regression_analysis.py"# hardhit_data_archive" 
