# Import necessary libraries
import plotly.express as px


def load_and_prepare_data():
    """
    Load the gapminder dataset and preprocess it by grouping by 'continent' and calculating the mean of 'lifeExp'.
    Returns the prepared dataframe.
    """
    try:
        # Load the gapminder dataset
        gapminder = px.data.gapminder()

        # Group by 'continent' and calculate the mean of 'lifeExp' and sort in descending order
        df_grouped = (
            gapminder.groupby("continent")["lifeExp"]
            .mean()
            .sort_values(ascending=True)
            .reset_index()
        )
        return df_grouped
    except Exception as e:
        print("An error occurred while loading or preparing the data.")
        raise e


def create_bar_chart(df_grouped):
    """
    Create a bar chart using the provided dataframe.
    :param df_grouped: Dataframe with the necessary data for the bar chart.
    """
    try:
        # Create the bar chart with 'lifeExp' on the x-axis and 'continent' on the y-axis
        fig = px.bar(df_grouped, x="lifeExp", y="continent")

        # Display the figure
        fig.show()
    except Exception as e:
        print("An error occurred while creating the bar chart.")
        raise e


def main():
    """
    Execute the main workflow.
    """
    try:
        df_grouped = load_and_prepare_data()
        create_bar_chart(df_grouped)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
