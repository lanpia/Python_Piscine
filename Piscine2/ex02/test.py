import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd


def load(path: str) -> object:
    """주어진 경로(path)의 CSV 파일을 읽어 데이터 크기를 출력하고, 데이터를 반환합니다.
    파일이 없거나 형식이 잘못된 경우 None을 반환합니다."""
    try:
        data = pd.read_csv(path)
        print(data.shape)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at path '{path}'.")
        return None
    except pd.errors.ParserError:
        print("Error: File is not a valid CSV format.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
def main():
    """load the life expectancy dataset and,
    display the country information of your campus."""
    try:
        df = load("population_total.csv")
        df_sub = (
            df[df.country.isin(["Belgium", "France"])]
            .melt(
                id_vars=["country"], var_name="year", value_name="population"
            )
            .rename(
                columns={
                    "country": "Country",
                    "year": "Year",
                    "population": "Population",
                }
            )
        )

        def convert_population(pop_str):
            if "M" in pop_str:
                return int(float(pop_str.replace("M", "")) * 1_000_000)
            return int(pop_str)

        df_sub["Year"] = df_sub["Year"].astype(int)
        df_sub["Population"] = df_sub["Population"].apply(convert_population)
        df_sub_pivot = df_sub.pivot_table(
            index="Year", columns="Country", values="Population"
        )

        def millions_formatter(x, pos):
            return f"{x / 1_000_000:.1f}M"

        ax = df_sub_pivot.plot(title="Population projections")
        plt.ylabel("Population")
        ax.yaxis.set_major_formatter(FuncFormatter(millions_formatter))
        plt.xlim(1800, 2050)

        plt.show()
    except (Exception, KeyboardInterrupt) as e:
        print(e)


if __name__ == "__main__":
    main()
