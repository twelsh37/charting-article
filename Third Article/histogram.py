import pandas as pd
import plotly.express as px


def read_dataset(file_path):
    """
    Reads a CSV file into a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pandas.DataFrame: The DataFrame containing the CSV data.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        raise
    except pd.errors.EmptyDataError:
        print("The file is empty.")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise


def create_histogram(df, column_name, bin_size, plot_title):
    """
    Creates a histogram using Plotly Express.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data to plot.
    column_name (str): The name of the DataFrame column to plot.
    bin_size (int): The number of bins for the histogram.
    plot_title (str): The title of the plot.

    Returns:
    plotly.graph_objs._figure.Figure: The Plotly figure object for the histogram.
    """
    try:
        fig = px.histogram(df, x=column_name, nbins=bin_size, title=plot_title)
        fig.update_xaxes(title_text='Value')
        fig.update_yaxes(title_text='Count')
        fig.update_layout(width=800, height=800)
        return fig
    except ValueError as e:
        print(f"ValueError: {e}")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise


def main():
    """
    Main function to read the dataset and create a histogram.
    """
    try:
        df = read_dataset('../datafiles/normal_distribution.csv')
        histogram_fig = create_histogram(df, 'Value', 50, 'Normal Distribution')
        histogram_fig.show()
    except Exception as e:
        print(f"An error occurred in the main function: {e}")


if __name__ == "__main__":
    main()
