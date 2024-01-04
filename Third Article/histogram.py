import pandas as pd
import numpy as np
import plotly.express as px


def generate_bins_labels(bin_width):
    """
    Function to generate bins and labels for age groups.

    Parameters:
    bin_width (int): The width of each bin.

    Returns:
    bins (list): The list of bins.
    labels (list): The list of labels for each bin.
    """
    bins = list(range(0, 101, bin_width)) + [np.inf]
    labels = [f'{i+1} - {i + bin_width}' for i in bins[:-2]] + [f'{bins[-2]+1}+']
    return bins, labels


def histogram_chart():
    """
    Function to process the dataframe and plot a histogram.
    """

    try:
        df = pd.read_csv('../datafiles/age.csv')
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return

    # our list to rename the columns
    nom = {'Lower tier local authorities Code': 'ltlac',
           'Lower tier local authorities': 'region',
           'Age (101 categories) Code': 'age_code',
           'Age (101 categories)': 'age',
           'Observation': 'number'
           }

    # rename the columns
    df.rename(columns=nom, inplace=True)


    bin_width = 10
    bins, labels = generate_bins_labels(bin_width)

    # filter the dataframe
    df['age_group'] = pd.cut(df['age_code'], bins=bins, labels=labels, include_lowest=True)
    df_grouped = df.groupby('age_group', observed=True)['number'].sum().reset_index()

    fig = px.histogram(df_grouped, x='age_group', y='number')
    fig.update_layout(width=800, height=800)

    # Display the chart
    fig.show()


def main():
    """
    Main function to read the dataset and call the histogram_chart function.
    """
    try:
        histogram_chart()
    except Exception as e:
        print(f"Error in plotting: {e}")


if __name__ == "__main__":
    main()
