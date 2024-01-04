import pandas as pd
import plotly.express as px


def read_and_filter_data(file_path, countries):
    """
    Reads the dataset from the given file path and filters it based on the specified countries.

    Parameters:
    - file_path: str, the path to the CSV file containing the dataset.
    - countries: list, a list of country codes to filter the dataset by.

    Returns:
    - A pandas DataFrame containing the filtered data.
    """
    try:
        # read in our dataset
        df = pd.read_csv(file_path)
        # filter the dataframe based on the countries we want to plot
        filtered_df = df[df['company_location'].isin(countries)].copy()
        return filtered_df
    except Exception as e:
        print(f"An error occurred while reading or filtering the data: {e}")
        raise


def plot_ecdf():
    """
    Plots an ECDF chart for the given dataframe.

    Parameters:
    - dataframe: DataFrame, the pandas DataFrame to plot.

    Returns:
    - The ECDF plot.
    """
    try:
        # Data file
        file_path = '../datafiles/ds_salaries.csv'

        # Countries we are interested in
        countries = ['US', 'GB', 'IN']

        # Read in our data and filter it
        df = read_and_filter_data(file_path, countries)

        # create an ECDF plot
        ecdf_plot = px.ecdf(df, x='salary_in_usd')

        # Set the chart size to 800 x 800 pixels
        ecdf_plot.update_layout(width=800, height=800)

        # Display our chart
        ecdf_plot.show()
    except Exception as e:
        print(f"An error occurred while plotting the ECDF: {e}")
        raise


def main():
    """
    Main function to execute the program logic.
    """
    try:
        plot_ecdf()
    except Exception as e:
        print(f"An error occurred in the main function: {e}")


if __name__ == "__main__":
    main()
