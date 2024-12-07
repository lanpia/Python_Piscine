import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from load_csv import load


def draw_life(country: str) -> None:
    """특정 국가의 수명 데이터를 시각화합니다."""
    data = load("life_expectancy_years.csv")
    if data is None:
        print("Error: Failed to load the dataset.")
        return

    if country not in data["country"].values:
        print(f"Error: Country '{country}' not found in the dataset.")
        return

    country_data = data[data["country"] == country].iloc[:, 1:].T
    country_data.columns = ["Life Expectancy"]
    country_data.index = country_data.index.astype(int)  # 인덱스를 연도로 변환
    country_data.reset_index(inplace=True)  # 인덱스를 열로 변환
    country_data.rename(columns={"index": "Year"}, inplace=True)

    # 그래프 스타일 설정
    sns.set_style("white")  # 배경 스타일 설정

    # Seaborn으로 그래프 그리기
    sns.lineplot(data=country_data, x="Year", y="Life Expectancy")
    plt.title(f"{country} Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.legend()
    min_year = country_data["Year"].min()
    max_year = country_data["Year"].max()
    plt.xticks(ticks=range(min_year, max_year + 1, 40))
    plt.show()


def main() -> None:
    # draw_life("South Korea")
    draw_life("France")


if __name__ == "__main__":
    main()
