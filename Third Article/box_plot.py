import pandas as pd
import plotly.express as px


def plot_salary_comparison():
    """
    This function reads a CSV file containing salary data, filters it for specific countries,
    and plots a box plot comparing the salaries in these countries.

    """
    try:
        # read in our dataset
        file_path = '../datafiles/ds_salaries.csv'
        salary_df = pd.read_csv(file_path)

        # filter the dataframe based on the country we want to plot
        country_df = salary_df[salary_df['company_location'].isin(['US', 'GB', 'IN'])].copy()

        # plot our box plot
        box = px.box(country_df,
                     x='company_location',
                     y='salary_in_usd',
                     color='company_location',
                     labels={
                         "salary_in_usd": "Salary (USD)",
                         "company_location": "Country",
                     },
                     title=' Salary comparison for Data Scientists from US, GB and IN'
                    )

        # Set the chart size to 1000 x 1000 pixels and disable the legend
        box.update_layout(showlegend=False, autosize=False, width=1000, height=1000)

        # Display our chart
        box.show()

    except FileNotFoundError:
        print(f"File not found at path: {file_path}")
    except pd.errors.EmptyDataError:
        print("No data in file.")
    except pd.errors.ParserError:
        print("Error parsing the data file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    """
    Main function to run the program.

    Returns:
        None
    """
    try:
        plot_salary_comparison()
    except Exception as e:
        print(f"An error occurred in main: {e}")


if __name__ == "__main__":
    main()
