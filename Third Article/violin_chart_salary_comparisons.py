import pandas as pd
import plotly.express as px


def read_and_filter_data():
    """
    Reads the dataset from the given file path and filters it based on the specified countries.

    Parameters:
    file_path (str): The path to the CSV file containing the dataset.
    countries (list): A list of country codes to filter the dataset.

    Returns:
    DataFrame: A pandas DataFrame containing the filtered data.
    """
    try:
        # Read in our datafile
        file_path = '../datafiles/ds_salaries.csv'
        salary_df = pd.read_csv(file_path)

        # Countries we are interested in
        countries = ['US', 'GB', 'IN']
        country_df = salary_df[salary_df['company_location'].isin(countries)].copy()
        return country_df
    except FileNotFoundError:
        print("The file was not found. Please check the file path.")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise


def plot_violin_chart(dataframe):
    """
    Plots a violin chart using the provided dataframe.

    Parameters:
    dataframe (DataFrame): A pandas DataFrame containing the data to plot.

    Returns:
    None: Displays the plot.
    """
    violin = px.violin(
        dataframe,
        x='company_location',
        y='salary_in_usd',
        labels={
            "salary_in_usd": "Salary (USD)",
            "company_location": "Country",
        },
        color='company_location',
        title='Salary comparison for Data Scientists from US, GB and IN'
    )
    violin.update_layout(showlegend=False, autosize=False, width=800, height=800)

    # Display our chart
    violin.show()


def main():
    """
    Main function to execute the data reading and plotting process.
    """
    try:
        country_df = read_and_filter_data()
        plot_violin_chart(country_df)
    except Exception as e:
        print(f"An error occurred in the main function: {e}")


if __name__ == "__main__":
    main()
