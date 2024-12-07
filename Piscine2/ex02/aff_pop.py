import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from load_csv import load

def compare_population(country1: str, country2: str) -> None:
    """
    두 국가의 연도별 인구 데이터를 비교하여 시각화합니다.
    """
    # 데이터 로드
    data = load("population_total.csv")
    if data is None:
        print("Error: Failed to load the dataset.")
        return

    data = data.set_index("country")  # 국가를 인덱스로 설정
    france_data = data.loc[country1].T  # 프랑스 데이터
    belgium_data = data.loc[country2].T  # 벨기에 데이터

    # 데이터프레임 생성
    france_df = pd.DataFrame({
        "Year": france_data.index.astype(int),
        "Population": france_data.values,
        "Country": "France"
    })
    belgium_df = pd.DataFrame({
        "Year": belgium_data.index.astype(int),
        "Population": belgium_data.values,
        "Country": "Belgium"
    })

    # 데이터 병합
    combined_data = pd.concat([france_df, belgium_df])

    # 그래프 스타일 설정
    sns.set_theme(style="white")

    # Seaborn 라인플롯
    sns.lineplot(
        data=combined_data,
        x="Year",
        y="Population",
        hue="Country",
        marker="o"
    )

    # 그래프 제목과 레이블
    plt.title("Population Comparison: France vs Belgium", fontsize=16)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Population", fontsize=12)
    plt.legend(title="Country")
    plt.tight_layout()
    # 그래프 표시
    plt.show()

def main() -> None:
    compare_population("France", "Belgium")

if __name__ == "__main__":
    main()