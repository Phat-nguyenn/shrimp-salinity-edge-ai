import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

print("Đang đọc dữ liệu...")

df = pd.read_csv('salinity_daily_reconstructed.csv')


station_name = 'An Hiệp' 
df_station = df[df['station'] == station_name].copy()


df_station['date'] = pd.to_datetime(df_station['date'])
df_station = df_station.sort_values('date')

df_station['sal_lag1'] = df_station['salinity_ppt'].shift(1) # Độ mặn ngày hôm qua
df_station['month'] = df_station['date'].dt.month # Tháng (để bắt mùa khô/mùa mưa)


df_station = df_station.dropna()

X = df_station[['sal_lag1', 'month']] # Đầu vào: Mặn hôm qua, Tháng
y = df_station['salinity_ppt']        # Đầu ra: Mặn hôm nay

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


print(f"Đang train mô hình Baseline XGBoost cho trạm {station_name}...")
model = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=3)
model.fit(X_train, y_train)

preds = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, preds))

print("-" * 30)
print(f"KẾT QUẢ: RMSE của Baseline Model là: {rmse:.4f} ppt")
print("-" * 30)
