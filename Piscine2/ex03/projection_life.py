from load_csv import load
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_life_expectancy_vs_gdp():
    # Load the data
    gdp_data = load("in-come_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy_data = load("life_expectancy_years.csv")

    # Filter data for the year 1900
    gdp_1900 = gdp_data[["country", "1900"]].rename(columns={"1900": "GDP"})
    life_expectancy_1900 = life_expectancy_data[["country", "1900"]].rename(columns={"1900": "Life Expectancy"})

    # Merge the data on the country column
    merged_data = pd.merge(gdp_1900, life_expectancy_1900, on="country").dropna()

    # Plot the data
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=merged_data, x="GDP", y="Life Expectancy", hue="country")

    # Add titles and labels
    plt.title("Life Expectancy vs GDP in 1900")
    plt.xlabel("GDP per Person (PPP, Inflation Adjusted)")
    plt.ylabel("Life Expectancy (Years)")
    plt.legend(title="Country", bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout()
    plt.show()

def main():
    plot_life_expectancy_vs_gdp()

if __name__ == "__main__":
    main()
