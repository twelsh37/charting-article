import plotly.express as px


def create_scatter_plot(country):
    """
    This function creates a scatter plot for a given country using the gapminder dataset.
    The scatter plot depicts life expectancy vs GDP per capita.

    Parameters:
    country (str): The country for which the scatter plot is to be created.

    Returns:
    None
    """
    try:
        # Load the gapminder dataset
        gapminder = px.data.gapminder()

        # Check if the country exists in the dataset
        if country not in gapminder["country"].unique():
            raise ValueError(f"{country} not found in the dataset.")

        # Mask our data so we only get the specified country
        mask = gapminder["country"] == country

        # Create our Scatter plot
        fig = px.scatter(
            gapminder[mask],
            x="lifeExp",
            y="gdpPercap",
            # add in size as the third variable
            size="pop",
            # Set the maximum marker size
            size_max=60,
            # add better labels for the axis
            labels={
                "gdpPercap": "GDP Per Capita",
                "lifeExp": "Life Expectancy",
            },
            title=f"Bubble Chart depicting {country} Life expectancy vs GDP Per Capita",
        )

        # Display the figure
        fig.show()

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Execute the main workflow.
    """
    try:
        # Call the function with the country of interest
        create_scatter_plot("Afghanistan")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
