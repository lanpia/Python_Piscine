import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from load_csv import load

def millions_formatter(x, _):
    """Chart y-axis formatter for population data."""
    return f"{int(x / 1_000_000)}M"

def compare_population(country1: str, country2: str):
    """Compare the population of two countries over time."""
    data = load("population_total.csv")
    data = data.set_index("country")
    france_data = data.loc[country1].T
    belgium_data = data.loc[country2].T
    df1 = pd.DataFrame({
        "Year": france_data.index.astype(int),
        "Population": france_data.values,
        "Country": country1
    })
    df2 = pd.DataFrame({
        "Year": belgium_data.index.astype(int),
        "Population": belgium_data.values,
        "Country": country2
    })
    combined_data = pd.concat([df1, df2])
    sns.set_theme(style="white")
    sns.lineplot(data=combined_data, x="Year", y="Population", hue="Country", marker="o")
    plt.title("Population Projecctions", fontsize=16)
    plt.xlim(1800, 2050)
    plt.show()

def main():
	compare_population("Belgium", "France")

if __name__ == "__main__":
	main()