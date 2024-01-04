import plotly.express as px


def load_gapminder_data():
    """
    Load the Gapminder dataset using Plotly Express.

    Returns:
        A DataFrame containing the Gapminder dataset.
    """
    return px.data.gapminder()


def create_scatter_plot(data):
    """
    Create a scatter plot of GDP Per Capita vs. Life Expectancy.

    Args:
        data: A DataFrame containing the Gapminder dataset.
    """
    # Ensure the required columns are present in the data
    required_columns = {'continent', 'gdpPercap', 'lifeExp'}
    if not required_columns.issubset(data.columns):
        raise ValueError(f"Data must contain the required columns: {required_columns}")

    fig = px.scatter(
        data,
        x="lifeExp",
        y="gdpPercap",
        color="continent",
        labels={
            "gdpPercap": "GDP Per Capita",
            "lifeExp": "Life Expectancy",
        },
        title="Scatter Plot of GDP Per Capita and Life Expectancy",
    )
    fig.show()


def main():
    """
    Main function to load data and create a scatter plot.
    """
    try:
        gapminder_data = load_gapminder_data()
        create_scatter_plot(gapminder_data)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
