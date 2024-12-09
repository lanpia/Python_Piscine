from load_csv import load
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def millions_formatter(value):
    """Convert a string representation of a population to an integer.
    Examples:
        - '3.25M' -> 3250000
        - '1.2B'  -> 1200000000
        - '400k'  -> 400000"""
    if "M" in value:
        return int(float(value.replace("M", "")) * 1_000_000)
    elif "B" in value:
        return int(float(value.replace("B", "")) * 1_000_000_000)
    elif "k" in value:
        return int(float(value.replace("k", "")) * 1_000)
    else:
        try:
            return int(value)
        except ValueError:
            raise ValueError(f"Invalid population format: {value}")


def compare_population(data: pd.DataFrame, country1: str, country2: str):
    """load the life expectancy dataset and,
    display the country information of your campus."""
    data = data.set_index("country")
    data = data.map(millions_formatter)
    country1_data = data.loc[country1].T
    country1_df = pd.DataFrame({
        "Year": country1_data.index.astype(int),
        "Population": country1_data.values,
        "Country": country1
    })

    country2_data = data.loc[country2].T
    country2_df = pd.DataFrame({
        "Year": country2_data.index.astype(int),
        "Population": country2_data.values,
        "Country": country2
    })

    combined_data = pd.concat([country1_df, country2_df])

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))

    sns.lineplot(
        data=combined_data,
        x="Year",
        y="Population",
        hue="Country",
        marker="o"
    )

    ax = plt.gca()
    ax.yaxis.set_major_formatter(FuncFormatter(millions_formatter))

    plt.title(f"Population Comparison: {country1} vs {country2}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(title="Country")
    plt.tight_layout()

    plt.show()

def main():
    compare_population(load("population_total.csv"), "Belgium", "France")

if __name__ == "__main__":
    main()
