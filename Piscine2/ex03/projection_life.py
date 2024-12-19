import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from load_csv import load
from matplotlib.ticker import FuncFormatter


def millions_formatter(value, pos):
    """Convert a population integer to a string representation with appropriate suffix."""
    if value >= 1_000_000_000:
        return f'{int(value / 1_000_000_000)}B'
    elif value >= 1_000_000:
        return f'{int(value / 1_000_000)}M'
    elif value >= 1_000:
        return f'{int(value / 1_000)}k'
    return str(int(value))

def draw_projection(dgdp: pd.DataFrame, dlife: pd.DataFrame):
    """Draw a scatter plot of GDP vs Life Expectancy in 1900."""

    merged_data = pd.merge(
        dgdp[["country", "1900"]].rename(columns={"1900": "GDP"}),
        dlife[["country", "1900"]].rename(columns={"1900": "Life Expectancy"}),
        on="country"
    )

    filtered_data = merged_data.dropna()
    sns.scatterplot(
        data=filtered_data,
        x="GDP",
        y="Life Expectancy",
        hue=None,
        size=None
    )

    ax = plt.gca()
    ax.set_xscale("log")
    ax.xaxis.set_major_formatter(FuncFormatter(millions_formatter))
    plt.xticks([300, 1000, 10000])
    plt.title("1900")
    plt.xlabel("Gross Domestic Product")
    plt.ylabel("Life Expectancy")
    plt.show()

def main():
    draw_projection(
        load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv"), 
        load("life_expectancy_years.csv")
    )

if __name__ == "__main__":
    main()
