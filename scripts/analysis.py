import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run_analysis():
    print("📈 데이터 분석 시작...")
    
    # 1. 정제된 데이터 불러오기
    df = pd.read_excel("../data/Energy_Economic_Clean_Data.xlsx")
    
    # 2. 기초 상관분석
    correlation = df[['renewables_share_energy', 'nuclear_share_energy', 'gdp']].corr()
    print("--- 상관계수 결과 ---")
    print(correlation)
    
    # 3. 비선형 관계 시각화 (신재생 비중 vs GDP)
    plt.figure(figsize=(10, 6))
    sns.regplot(data=df, x='renewables_share_energy', y='gdp', order=2, 
                line_kws={"color": "red"}, scatter_kws={'alpha':0.3})
    plt.title("Non-linear Relationship: Renewables Share vs GDP")
    plt.xlabel("Renewables Share (%)")
    plt.ylabel("Real GDP")
    
    # 결과 이미지 저장
    plt.savefig("../results/threshold_analysis_plot.png")
    print("✅ 분석 시각화 완료! (results 폴더 확인)")

if __name__ == "__main__":
    run_analysis()
