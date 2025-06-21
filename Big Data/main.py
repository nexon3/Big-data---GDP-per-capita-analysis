from data_handler import fetch_data, save_to_csv, save_to_mongodb, load_from_csv, load_from_mongodb
from analysis import calculate_average_gdp, find_max_gdp_in_year
from visualization import plot_gdp_trend, plot_gdp_comparison
import argparse

def main():
    parser = argparse.ArgumentParser(description='Open Data Project')
    parser.add_argument('--storage', choices=['csv', 'mongodb'], default='csv', help='Storage option: csv or mongodb')
    args = parser.parse_args()

    data = fetch_data()
    if args.storage == 'csv':
        save_to_csv(data)
        df = load_from_csv()
    elif args.storage == 'mongodb':
        save_to_mongodb(data)
        df = load_from_mongodb()
    else:
        raise ValueError("Invalid storage option. Choose 'csv' or 'mongodb'.")

    # Analiza
    average_gdp = calculate_average_gdp(df)
    print("Top 10 countries by average GDP per capita:")
    print(average_gdp.head(10))

    max_gdp_2020 = find_max_gdp_in_year(df, 2020)
    print("Country with highest GDP per capita in 2020:")
    print(max_gdp_2020)

    # Wizualizacja
    plot_gdp_trend(df, 'United States')
    plot_gdp_comparison(df, 2020, ['United States', 'China', 'Japan', 'Germany'])

if __name__ == "__main__":
    main()