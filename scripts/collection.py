import pandas as pd
import wbgapi as wb

def collect_data():
    print("🚀 데이터 수집 시작...")
    
    # 1. OWID 데이터 로드 (파일이 같은 경로에 있다고 가정)
    # 실제 경로에 맞춰 수정하세요.
    owid_url = "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv"
    energy_df = pd.read_csv(owid_url)
    
    # 필요한 변수만 추출
    energy_cols = ['country', 'year', 'renewables_share_energy', 'nuclear_share_energy']
    energy_df = energy_df[energy_cols]
    
    # 2. World Bank GDP 데이터 수집 (최근 20년)
    print("🌐 월드뱅크 API 연결 중...")
    gdp_df = wb.data.DataFrame('NY.GDP.MKTP.KD', mrv=20, labels=True).reset_index()
    gdp_df = gdp_df.melt(id_vars=['economy', 'Country'], var_name='year', value_name='gdp')
    gdp_df['year'] = gdp_df['year'].str.replace('YR', '').astype(int)
    
    # 3. 데이터 통합 (국가명과 연도 기준)
    combined_df = pd.merge(energy_df, gdp_df, left_on=['country', 'year'], right_on=['Country', 'year'])
    
    # 4. 결측치 제거 (우리가 정한 고순도 데이터셋 전략)
    clean_df = combined_df.dropna(subset=['renewables_share_energy', 'nuclear_share_energy', 'gdp'])
    
    # 5. 저장
    clean_df.to_excel("../data/Energy_Economic_Clean_Data.xlsx", index=False)
    print("✅ 데이터 수집 및 정제 완료! (data 폴더 확인)")

if __name__ == "__main__":
    collect_data()
