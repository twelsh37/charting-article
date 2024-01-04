import plotly.express as px
import pandas as pd


def read_data(file_path):
    """
    Reads data from a CSV file into a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        df (DataFrame): The data from the CSV file as a pandas DataFrame.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If the file cannot be parsed.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError) as e:
        print(f"Error reading data: {e}")
        raise


def create_icicle_chart(df):
    """
    Creates an icicle chart from a DataFrame.

    Args:
        df (DataFrame): The DataFrame to create the chart from.

    Returns:
        fig (Figure): The created icicle chart.

    Raises:
        ValueError: If the DataFrame is empty or if necessary columns are missing.
    """
    try:
        df_count = df.groupby(["L1 Risk", "L2 Risk", "L3 Risk"]).size().reset_index(name="counts")
        fig = px.icicle(df_count,
                        path=["L1 Risk", "L2 Risk", "L3 Risk"],
                        values="counts",
                        title="Operational Risk Data")
        fig.update_traces(root_color="lightgrey")
        fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
        fig.update_traces(textinfo="label+value", texttemplate="%{label}:<br> Risks: %{value:.0f}")
        fig.update_layout(autosize=False, width=900, height=1250)

        # Display our chart
        fig.show()

    except ValueError as e:
        print(f"Error creating chart: {e}")
        raise


def main():
    """
    Main function to run the program.

    Returns:
        None
    """
    try:
        df = read_data("../datafiles/taxonomy.csv")
        create_icicle_chart(df)

    except Exception as e:
        print(f"Error in main: {e}")


if __name__ == "__main__":
    main()
