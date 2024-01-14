import plotly.express as px
import pandas as pd


def plot_ecdf():
    """
    This function reads a CSV file containing salary data, filters it based on the provided countries,
    and plots an Empirical Cumulative Distribution Function (ECDF) of the salaries.

    Parameters:
    file_path (str): The path to the CSV file.
    countries (list): A list of countries to filter the data.

    Returns:
    None
    """
    try:
        # read in our dataset
        file_path = '../datafiles/ds_salaries.csv'
        salary_df = pd.read_csv(file_path)

        # Countries we are interested in
        countries = ['US']

        # filter the dataframe based on the countries we want to plot
        country_df = salary_df[salary_df['company_location'].isin(countries)].copy()

        fig = px.ecdf(country_df,
                      x='salary_in_usd',
                      labels={
                          "salary_in_usd": "Salary (USD)",
                          "company_location": "Country",
                      },
                      markers=False,
                      lines=True,
                      marginal="histogram",
                      title="ECDF plot with a marginal histogram - US Salaries",
                      )

        # The background color of the plot is updated to transparent
        fig.update_layout(width=800, height=800)

        # Display our chart
        fig.show()

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function to run the program.

    Returns:
        None
    """
    try:
        plot_ecdf()
    except Exception as e:
        print(f"An error occurred in main: {e}")


if __name__ == "__main__":
    main()
