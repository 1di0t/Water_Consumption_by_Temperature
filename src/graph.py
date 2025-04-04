import pandas as pd
import matplotlib.pyplot as plt
import math

merged_df = pd.read_csv('data/merged_data.csv')


#전체 데이터의 온도와 수도 사용량 범위 구하기
temp_min = merged_df['최고기온'].min()
temp_max = merged_df['최고기온'].max()

usage_min = merged_df['상하수도사용량'].min()
usage_max = merged_df['상하수도사용량'].max()


#연도별 서브플롯을 한 화면에 표시하기 위한 설정
years = sorted(merged_df['연도'].unique())
n_years = len(years)
n_cols = 4 # 가로에 몇 개의 서브플롯을 배치할지 설정
n_rows = math.ceil(n_years / n_cols)

fig, axs = plt.subplots(n_rows, n_cols, figsize=(n_cols * 5, n_rows * 4))
axs = axs.flatten()

#그래프 생성
for i, year in enumerate(years):
    ax = axs[i]
    data = merged_df[merged_df['연도'] == year].sort_values('월')
    
    # 왼쪽 y축: 최고기온
    ax.plot(data['월'], data['최고기온'], marker='o', color='tab:red', label='high temperature')
    ax.set_title(f"{year}")
    ax.set_xlabel("month")
    ax.set_ylabel("temperature", color='tab:red')
    ax.tick_params(axis='y', labelcolor='tab:red')

    ax.set_ylim(temp_min, temp_max)
    
    # 오른쪽 y축: 상하수도 사용량
    ax2 = ax.twinx()
    ax2.plot(data['월'], data['상하수도사용량'], marker='s', color='tab:blue', label='water usage')
    ax2.set_ylabel("water usage", color='tab:blue')
    ax2.tick_params(axis='y', labelcolor='tab:blue')

    ax2.set_ylim(usage_min, usage_max)
    
    # 왼쪽 y축: 평균기온
    ax3 = ax.twinx()
    ax3.plot(data['월'], data['평균기온'], marker='o', color='tab:orange', label='mean temperature')
    ax3.tick_params(axis='y', labelcolor='None')

    ax3.set_ylim(temp_min, temp_max)

    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    lines3, labels3 = ax3.get_legend_handles_labels()
    ax3.legend(lines1 + lines2 + lines3, labels1 + labels2 + labels3, loc='upper left')


# 사용하지 않는 서브플롯 숨기기
for j in range(i+1, len(axs)):
    fig.delaxes(axs[j])

plt.tight_layout()
plt.show()