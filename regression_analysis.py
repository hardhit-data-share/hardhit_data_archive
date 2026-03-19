import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# =========================
# 1. 데이터 로드
# =========================
df = pd.read_csv("dataset_era_ra9.csv")

# =========================
# 2. 변수 생성
# =========================
# Defense = RA9 - ERA
df["defense"] = df["ra9"] - df["era"]

# 종속변수 (경기당 실점)
y = df["r_g"]

# 독립변수
X = df[["era", "defense"]]

# =========================
# 3. 회귀 모델 학습
# =========================
model = LinearRegression()
model.fit(X, y)

# =========================
# 4. 예측 및 평가
# =========================
y_pred = model.predict(X)

r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

# =========================
# 5. 표준화 계수 계산
# =========================
X_std = (X - X.mean()) / X.std()
y_std = (y - y.mean()) / y.std()

model_std = LinearRegression()
model_std.fit(X_std, y_std)

beta_era_std = model_std.coef_[0]
beta_def_std = model_std.coef_[1]

# 비율 계산
total = abs(beta_era_std) + abs(beta_def_std)
era_ratio = abs(beta_era_std) / total
def_ratio = abs(beta_def_std) / total

# =========================
# 6. 결과 출력
# =========================
print("=== 회귀 결과 ===")
print(f"절편 (β₀): {model.intercept_:.4f}")
print(f"ERA 계수 (β₁): {model.coef_[0]:.4f}")
print(f"Defense 계수 (β₂): {model.coef_[1]:.4f}")

print("\n=== 모델 적합도 ===")
print(f"R²: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")

print("\n=== 표준화 계수 ===")
print(f"ERA: {beta_era_std:.4f}")
print(f"Defense: {beta_def_std:.4f}")

print("\n=== 영향력 비율 ===")
print(f"투수력 (ERA): {era_ratio*100:.2f}%")
print(f"수비력 (Defense): {def_ratio*100:.2f}%")