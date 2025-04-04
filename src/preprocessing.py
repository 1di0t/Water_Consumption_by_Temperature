import pandas as pd


# 데이터 불러오기
water_df = pd.read_csv('data/한국소비자원_에너지 사용량 (수도)_20250228.csv')
temp_df = pd.read_csv('data/ta_20250401110349.csv')

# 수도 사용량 데이터 0이 포함된 연도 제거
water_df = water_df[water_df["연도"] > 2014 ]

# 25년 이후의 데이터는 측정하기엔 부족하므로 제거
water_df = water_df[water_df["연도"] != 2025]

# 기온 데이터 결측치 제거
temp_df = temp_df.dropna(subset=['평균기온', '최저기온', '최고기온'])

# 온도 데이터 전처리: '날짜' 열에서 공백 제거 후 datetime 변환
temp_df['날짜'] = temp_df['날짜'].str.strip()  
temp_df['날짜'] = pd.to_datetime(temp_df['날짜'], format='%Y-%m-%d')

# 연도와 월 추출 및 월별 평균 온도 계산
temp_df['연도'] = temp_df['날짜'].dt.year
temp_df['월'] = temp_df['날짜'].dt.month

# 월별(연도+월)로 그룹화하여 평균 계산
temp_grouped = temp_df.groupby(['연도', '월']).agg({
    '평균기온': 'mean',
    '최저기온': 'mean',
    '최고기온': 'mean'
}).reset_index()

# 4. 두 데이터프레임을 연도와 월을 기준으로 병합
merged_df = pd.merge(water_df, temp_grouped, on=['연도', '월'], how='left')

# 5. 결과 확인 및 저장
merged_df.to_csv('data/merged_data.csv', index=False)
print(f"{merged_df.head(3)}")