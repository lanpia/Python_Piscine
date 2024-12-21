from load_csv import load
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def millions_formatter(value, pos):
    """Convert a population integer to a string representation with appropriate suffix."""
    if value >= 1_000_000_000:
        return f'{value / 1_000_000_000:.1f}B'
    elif value >= 1_000_000:
        return f'{value / 1_000_000:.1f}M'
    elif value >= 1_000:
        return f'{value / 1_000:.1f}k'
    return str(value)

def population_to_int(value):
    """Convert a string representation of a population to an integer."""
    if pd.isna(value):
        return value
    if isinstance(value, str):
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
    return int(value)

def compare_population(data: pd.DataFrame, country1: str, country2: str):
    """Load the life expectancy dataset and display the country information of your campus."""
    data = data.set_index("country")
    data = data.applymap(population_to_int)

    country1_data = data.loc[country1].T
    country1_data = country1_data[(country1_data.index.astype(int) >= 1800) & (country1_data.index.astype(int) <= 2050)]
    country1_df = pd.DataFrame({
        "Year": country1_data.index.astype(int),
        "Population": country1_data.values,
        "Country": country1
    })

    country2_data = data.loc[country2].T
    country2_data = country2_data[(country2_data.index.astype(int) >= 1800) & (country2_data.index.astype(int) <= 2050)]
    country2_df = pd.DataFrame({
        "Year": country2_data.index.astype(int),
        "Population": country2_data.values,
        "Country": country2
    })

    combined_data = pd.concat([country1_df, country2_df])

    sns.lineplot(
        data=combined_data,
        x="Year",
        y="Population",
        hue="Country"
    )

    ax = plt.gca()
    ax.yaxis.set_major_formatter(FuncFormatter(millions_formatter))
    plt.xticks(range(1800, 2051, 40))

    plt.title("Population projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()

    plt.show()

def main():
    compare_population(load("population_total.csv"), "Belgium", "France")

if __name__ == "__main__":
    main()
