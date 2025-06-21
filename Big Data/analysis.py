import pandas as pd

def calculate_average_gdp(df):
    """Oblicza średnią GDP per capita dla każdego kraju."""
    return df.groupby('country')['gdp_per_capita'].mean().sort_values(ascending=False)

def find_max_gdp_in_year(df, year):
    """Znajduje kraj z najwyższym GDP per capita w danym roku."""
    df_year = df[df['year'] == year]
    max_gdp_country = df_year.loc[df_year['gdp_per_capita'].idxmax()]
    return max_gdp_country