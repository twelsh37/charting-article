import plotly.express as px
import pandas as pd


def create_sunburst_chart():
    """
    This function reads a CSV file from the given file path and creates a sunburst chart
    based on the 'L1 Risk', 'L2 Risk', and 'L3 Risk' columns.

    """

    try:
        file_path = "../datafiles/taxonomy.csv"
        # Read in our data to our dataframe 'df'
        df = pd.read_csv(file_path)

        # Count the occurrences of each combination of risks
        df_count = (
            df.groupby(["L1 Risk", "L2 Risk", "L3 Risk"]).size().reset_index(name="counts")
        )

        # Create the sunburst chart
        fig = px.sunburst(
            df_count,
            path=["L1 Risk", "L2 Risk", "L3 Risk"],
            values="counts",
            title="Risk Data Displayed on a Sunburst Chart",
        )

        # Display the figure
        fig.show()

    except FileNotFoundError:
        print(f"File not found at {file_path}")
    except pd.errors.EmptyDataError:
        print("No data in the file")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function to run the program.

    Returns:
        None
    """
    try:
        create_sunburst_chart()
    except Exception as e:
        print(f"An error occurred in main: {e}")


if __name__ == "__main__":
    main()
