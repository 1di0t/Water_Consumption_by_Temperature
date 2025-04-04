import pandas as pd


# 1. 데이터 불러오기
water_df = pd.read_csv('data/한국소비자원_에너지 사용량 (수도)_20250228.csv')
temp_df = pd.read_csv('data/ta_20250401110349.csv')


print(f"\n\n수도 사용량 :\n{water_df.head(-1)}")
print(f"\n기온 데이터 :\n{temp_df.head(-1)}")

# 결측치 또는 0인 데이터 확인
print(f"\n\n수도 사용량 결측치 :\n{water_df.isnull().sum()}")
print(f"\n기온 데이터 결측치 :\n{temp_df.isnull().sum()}")

print(f"\n기온 데이터 결측 행 :\n{temp_df[temp_df.isnull().any(axis=1)]}")

print(f"\n\n수도 사용량 0인 데이터 :\n{water_df[water_df['상하수도사용량'] == 0]}")
