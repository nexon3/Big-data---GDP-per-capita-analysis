import matplotlib.pyplot as plt

def plot_gdp_trend(df, country):
    """Tworzy wykres liniowy trendu GDP per capita dla wybranego kraju."""
    country_data = df[df['country'] == country]
    plt.figure(figsize=(10, 6))
    plt.plot(country_data['year'], country_data['gdp_per_capita'], marker='o')
    plt.title(f'GDP per Capita of {country} (2010-2020)')
    plt.xlabel('Year')
    plt.ylabel('GDP per Capita (current US$)')
    plt.grid(True)
    plt.show()

def plot_gdp_comparison(df, year, countries):
    """Tworzy wykres słupkowy porównujący GDP per capita wybranych krajów w danym roku."""
    df_year = df[df['year'] == year]
    df_selected = df_year[df_year['country'].isin(countries)]
    plt.figure(figsize=(10, 6))
    plt.bar(df_selected['country'], df_selected['gdp_per_capita'])
    plt.title(f'GDP per Capita Comparison in {year}')
    plt.xlabel('Country')
    plt.ylabel('GDP per Capita (current US$)')
    plt.show()