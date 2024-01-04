import pandas as pd
import plotly.express as px


def read_data():
    """
    Function to read data from a csv file.
    :return: DataFrame, the loaded data
    """
    try:
        file_path = '../datafiles/ds_salaries.csv'
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None


def filter_data(df):
    """
    Function to filter data based on the company location.
    :param df: DataFrame, the data to be filtered
    :return: DataFrame, the filtered data
    """
    if df is not None:
        countries = ['US', 'GB', 'IN']
        return df[df['company_location'].isin(countries)].copy()
    else:
        return None


def plot_data(df):
    """
    Function to plot data using plotly.
    :param df: DataFrame, the data to be plotted
    """
    if df is not None:
        fig = px.strip(df,
                       x='salary_in_usd',
                       y='company_location',
                       labels={
                           "salary_in_usd": "Salary (USD)",
                           "company_location": "Country",
                       },
                       color='company_location',
                       title=' Salary comparison for Data Scientists from US, GB and IN')

        fig.update_layout(plot_bgcolor="rgba(0, 0, 0, 0)", width=800, height=800)
        fig.show()
    else:
        print("No data to plot.")


def main():
    """
    Main function to execute the program.
    """
    try:
        # read in our dataset
        salary_df = read_data()

        # filter the dataframe based on the country we want to plot
        country_df = filter_data(salary_df)

        # plot the data
        plot_data(country_df)

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
