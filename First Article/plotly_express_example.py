import plotly.express as px
import pandas as pd


def create_chart():
    """
    This function creates a bar chart using Plotly Express with "Continent" as the x-values,
    "Entities" as the y-values, and "City" as the color of the bars.
    """
    try:
        # Create our Pandas dataframe with some data to work with
        df = pd.DataFrame(
            {
                "Continent": [
                    "Africa",
                    "Antarctica",
                    "Asia",
                    "Australia",
                    "Europe",
                    "North America",
                    "South America",
                ],
                "City": [
                    "Nairobi",
                    "Haley",
                    "Shanghai",
                    "Sydney",
                    "London",
                    "Seattle",
                    "Caracas",
                ],
                "Entities": [24, 12, 76, 29, 62, 45, 57],
            }
        )

        # Create a bar chart using the DataFrame `df`, with "Continent" as the x-values,
        # "Entities" as the y-values, and "City" as the color of the bars.
        fig = px.bar(
            df,
            x="Continent",
            y="Entities",
            color="City",
            title="Chart created by plotly.express",
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
        create_chart()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
