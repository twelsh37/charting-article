import plotly.express as px
import pandas as pd


def create_ecdf_chart(dataframe, column_name):
    """
    Create an ECDF chart using Plotly Express.

    Parameters:
    - dataframe: A pandas DataFrame containing the data.
    - column_name: The name of the column for which the ECDF will be calculated.

    Returns:
    - A Plotly Express ECDF chart object.
    """
    ecdf_chart = px.ecdf(
        dataframe, x=column_name, title="Chart depicting data under a normal distribution"
    )
    ecdf_chart.update_layout(width=800, height=800)
    return ecdf_chart


def main():
    """
    Main function to read data, create ECDF chart and display it.
    """
    try:
        # read in our dataset
        df2 = pd.read_csv("../datafiles/random_data.csv")
        # create ECDF chart
        ecdf = create_ecdf_chart(df2, "std_dev_data")
        # display the chart
        ecdf.show()
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except pd.errors.EmptyDataError as e:
        print(f"No data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
