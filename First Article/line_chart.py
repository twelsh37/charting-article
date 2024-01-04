import plotly.express as px


def plot_life_expectancy():
    """
    This function plots the life expectancy in Afghanistan from 1952 to 2007.
    It uses the gapminder dataset from plotly and creates a line chart with 'year' on the x-axis and 'lifeExp'
     on the y-axis.
    The plot background color is set to transparent.
    """
    try:
        # Load the gapminder dataset
        gapminder = px.data.gapminder()

        # Mask our data so we only get Afghanistan
        mask = gapminder["country"] == "Afghanistan"

        # Create the line chart with 'year' on the x-axis and 'lifeExp' on the y-axis.
        # Add labels Dictionary to format the Axes labels
        # Add an update_layout to set the plot background colour to transparent
        fig = px.line(
            gapminder[mask],
            x="year",
            y="lifeExp",
            labels={
                "lifeExp": "Life Expectancy",
                "year": "Year",
            },
            title="Rise In Life Expectancy, Afghanistan 1952 - 2007",
        ).update_layout(plot_bgcolor="rgba(0, 0, 0, 0)")

        # Show the figure
        fig.show()

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    try:
        plot_life_expectancy()
    except Exception as e:
        print(f"An error occurred in main: {e}")


if __name__ == "__main__":
    main()
