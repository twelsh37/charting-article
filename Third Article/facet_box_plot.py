import pandas as pd
import plotly.express as px


def read_and_filter_data():
    """
    Reads the dataset from the given file path and filters it based on the specified countries and job titles.

    Parameters:
    - file_path: str, the path to the CSV file containing the dataset.
    - countries: list, the list of countries to filter by.
    - job_titles: list, the list of job titles to filter by.

    Returns:
    - DataFrame, the filtered dataset.
    """
    try:
        # Read in the dataset
        file_path = '../datafiles/ds_salaries.csv'
        salary_df = pd.read_csv(file_path)

        # Countries we are interested in
        countries = ['US', 'GB', 'IN']

        # Job titles we are interested in
        job_titles = ['Data Scientist', 'Big Data Engineer']

        # Filter the dataframe based on the country and job title
        filtered_df = salary_df[(salary_df['company_location'].isin(countries)) &
                                (salary_df['job_title'].isin(job_titles))].copy()
        return filtered_df
    except Exception as e:
        print(f"An error occurred while reading and filtering the data: {e}")
        raise


def plot_salary_comparison(filtered_df):
    """
    Plots a box plot for the salary comparison based on the filtered dataset.

    Parameters:
    - filtered_df: DataFrame, the filtered dataset to plot.

    Returns:
    - The plotly figure object.
    """
    try:
        # Plot the box plot
        box = px.box(filtered_df,
                     x='company_location',
                     y='salary_in_usd',
                     color='company_location',
                     facet_col='job_title',
                     labels={
                         "salary_in_usd": "Salary (USD)",
                         "company_location": "Country",
                     },
                     title='Salary comparison for Big Data Engineer and Data Scientist from USA, GB, and India'
                     )

        # Remove "job_title=" from facet column titles
        box.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

        # Set the chart size and disable the legend
        box.update_layout(showlegend=False, autosize=False, width=1000, height=1000)

        return box
    except Exception as e:
        print(f"An error occurred while plotting the data: {e}")
        raise


def main():
    """
        Main function to run the program.

    Returns:
        None
    """
    try:

        # Read and filter the data
        filtered_df = read_and_filter_data()

        # Plot the data
        box_plot = plot_salary_comparison(filtered_df)

        # Display the plot
        box_plot.show()

    except Exception as e:
        print(f"An error occurred in the main function: {e}")


if __name__ == "__main__":
    main()
