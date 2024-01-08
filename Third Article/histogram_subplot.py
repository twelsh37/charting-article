import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def read_data(file_path):
    """
    Function to read data from a csv file using pandas.

    Args:
        file_path (str): The path to the csv file.

    Returns:
        DataFrame: A pandas DataFrame containing the data.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None


def create_histogram(df, bin_sizes):
    """
    Function to create a histogram with different bin sizes.

    Args:
        df (DataFrame): The pandas DataFrame containing the data.
        bin_sizes (list): A list of bin sizes.

    Returns:
        Figure: A plotly Figure containing the histograms.
    """
    subplot_titles = [f'Bin size: {bin_size}' for bin_size in bin_sizes]

    fig = make_subplots(rows=1, cols=3, subplot_titles=subplot_titles)

    for i, bin_size in enumerate(bin_sizes, start=1):
        hist = go.Histogram(x=df['Value'], nbinsx=bin_size, name=f'Bin size {bin_size}')
        fig.add_trace(hist, row=1, col=i)

    fig.update_layout(title_text='Normal Distribution with Different Bin Sizes', showlegend=False)
    fig.update_xaxes(title_text='Value')
    fig.update_yaxes(title_text='Count')

    return fig


def main():
    """
    Main function to read data and create histograms.
    """
    try:
        file_path = '../datafiles/normal_distribution.csv'
        bin_sizes = [100, 250, 400]

        df = read_data(file_path)

        if df is not None:
            fig = create_histogram(df, bin_sizes)
            fig.show()
        else:
            print("No data to plot.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
