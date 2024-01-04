# Import the necessary libraries
import plotly.express as px


# Define a function to create and display the area chart
def create_area_chart():
    try:
        # Load the gapminder dataset
        gapminder = px.data.gapminder()

        # Create an area chart using the gapminder dataset
        fig = px.area(
            gapminder,
            x="year",
            y="gdpPercap",
            # Different continents are represented by different colors
            color="continent",
            # Each line group represents a country
            line_group="country",
            labels={
                "gdpPercap": "GDP Per Capita",
                "year": "Year",
            },
            title="Rise in GDP Per Capita,  1952 - 2007",
        )

        # Update the background color of the plot to transparent
        fig.update_layout(plot_bgcolor="rgba(0, 0, 0, 0)")

        # Display the figure
        fig.show()

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Execute the main workflow.
    """
    try:
        create_area_chart()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
