import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

print("Đang đọc dữ liệu...")
# 1. Đọc dữ liệu
df = pd.read_csv('salinity_daily_reconstructed.csv')

# 2. Lọc dữ liệu cho 1 trạm duy nhất để train (Trạm An Hiệp)
station_name = 'An Hiệp' 
df_station = df[df['station'] == station_name].copy()

# Chuyển cột date sang dạng datetime và sắp xếp theo thời gian
df_station['date'] = pd.to_datetime(df_station['date'])
df_station = df_station.sort_values('date')

# 3. Tạo Features (Đặc trưng)
# Vì chưa có dữ liệu triều, tạm thời dùng baseline "Ngây thơ" (Naive): Dự báo mặn hôm nay dựa vào mặn hôm qua
df_station['sal_lag1'] = df_station['salinity_ppt'].shift(1) # Độ mặn ngày hôm qua
df_station['month'] = df_station['date'].dt.month # Tháng (để bắt mùa khô/mùa mưa)

# Xóa các dòng có giá trị NaN (do phép shift tạo ra ở dòng đầu tiên)
df_station = df_station.dropna()

# 4. Chuẩn bị dữ liệu Train/Test
X = df_station[['sal_lag1', 'month']] # Đầu vào: Mặn hôm qua, Tháng
y = df_station['salinity_ppt']        # Đầu ra: Mặn hôm nay

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Train mô hình Baseline (XGBoost)
print(f"Đang train mô hình Baseline XGBoost cho trạm {station_name}...")
model = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=3)
model.fit(X_train, y_train)

# 6. Đánh giá mô hình
preds = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, preds))

print("-" * 30)
print(f"KẾT QUẢ: RMSE của Baseline Model là: {rmse:.4f} ppt")
print("-" * 30)
