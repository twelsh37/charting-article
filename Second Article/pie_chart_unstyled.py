import plotly.express as px


def get_gapminder_data(country):
    """
    Get gapminder data for a specific country.

    Args:
        country (str): The name of the country.

    Returns:
        DataFrame: A DataFrame containing the gapminder data for the specified country.
    """
    # setup our gapminder dataset
    gapminder = px.data.gapminder()

    # Get data only for the specified country
    country_data = gapminder.query(f"country == '{country}'")

    return country_data


def plot_country_life_expectancy(country_data):
    """
    Plot the life expectancy data for a specific country.

    Args:
        country_data (DataFrame): A DataFrame containing the gapminder data for a specific country.

    Returns:
        None
    """
    # Create a pie chart with the life expectancy data
    fig = px.pie(country_data, values="lifeExp", names="lifeExp")

    # Show the figure
    fig.show()


def main():
    """
    Main function to run the program.

    Returns:
        None
    """
    try:
        # Get the gapminder data for Afghanistan
        afghanistan_2007 = get_gapminder_data('Afghanistan')

        # Plot the life expectancy data for Afghanistan
        plot_country_life_expectancy(afghanistan_2007)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
