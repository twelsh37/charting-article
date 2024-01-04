# Import the libraries we need
import plotly.express as px


def load_and_process_data():
    """
    Load the gapminder dataset, group by 'continent' and calculate the mean of 'lifeExp'.
    Sort the results in ascending order and reset the index.
    """
    # Load the gapminder dataset
    gapminder = px.data.gapminder()

    # Group by 'continent' and calculate the mean of 'lifeExp'
    # Sort in ascending order and reset the index
    df_grouped1 = (
        gapminder.groupby("continent")["lifeExp"]
        .mean()
        .sort_values(ascending=True)
        .reset_index()
    )

    return df_grouped1


def create_bar_chart(df):
    """
    Create a bar chart with 'continent' on the x-axis and 'lifeExp' on the y-axis.
    """
    # Create the bar chart
    fig = px.bar(df, x="continent", y="lifeExp")

    # Show the figure
    fig.show()


def main():
    """
    Main function to run the data loading, processing and visualization.
    """
    try:
        # Load and process the data
        df_grouped1 = load_and_process_data()

        # Create the bar chart
        create_bar_chart(df_grouped1)

    except Exception as e:
        print(f"An error occurred: {e}")


# Run the main function
if __name__ == "__main__":
    main()
