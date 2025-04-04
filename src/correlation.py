import pandas as pd
import matplotlib.pyplot as plt


#한글 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

merged_df = pd.read_csv('data/merged_data.csv')

corr_matrix = merged_df.corr()

fig, ax = plt.subplots(figsize=(8, 6))
cax = ax.matshow(corr_matrix, cmap='coolwarm')
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
fig.colorbar(cax)
plt.title('Correlation Matrix', pad=20)
plt.show()
