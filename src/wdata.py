import pandas as pd

# Đọc file
df = pd.read_csv('salinity_daily_reconstructed.csv')

# 1. Chỉ lấy dữ liệu của trạm An Hiệp
df_an_hiep = df[df['station'] == 'An Hiệp']

# 2. Chọn các cột quan trọng để dễ nhìn
cot_quan_trong = ['date', 'salinity_ppt', 'type', 'lower90_ppt', 'upper90_ppt']
df_hien_thi = df_an_hiep[cot_quan_trong]

# 3. In ra 10 dòng đầu tiên dưới dạng bảng
print("--- 10 DÒNG DỮ LIỆU ĐẦU TIÊN CỦA TRẠM AN HIỆP ---")
print(df_hien_thi.head(10))

# 4. Xem thống kê cơ bản (mặn nhất, nhạt nhất, trung bình)
print("\n--- THỐNG KÊ ĐỘ MẶN TRẠM AN HIỆP ---")
print(df_an_hiep['salinity_ppt'].describe())