import plotly.express as px


def plot_life_expectancy():
    """
    This function plots a bar chart of average life expectancy by continent.
    It uses the gapminder dataset from plotly express.
    """
    try:
        # Load the gapminder dataset
        gapminder = px.data.gapminder()

        # Group by 'continent' and calculate the mean of 'lifeExp' and sort in descending order
        df_grouped1 = (
            gapminder.groupby("continent")["lifeExp"]
            .mean()
            .sort_values(ascending=True)
            .reset_index()
        )

        # Create the bar chart with 'lifeExp' on the x-axis and 'continent' on the y-axis.
        # Add labels Dictionary to format the Axes labels
        fig = px.bar(
            df_grouped1,
            x="lifeExp",
            y="continent",
            labels={
                "lifeExp": "Life Expectancy (Average)",
                "continent": "Continent",
            },
            title="Average life expectancy by Continent",
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
        plot_life_expectancy()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
