import pandas as pd
import plotly.graph_objects as go
import numpy as np


def plot_salary_distribution():
    """
    This function reads a CSV file containing salary data, filters it based on specific criteria,
    and plots a histogram and ECDF of the salaries.
    """
    try:
        # read in our dataset
        file_path = '../datafiles/ds_salaries.csv'
        salary_df = pd.read_csv(file_path)

        # filter the dataframe based on the country and job title we want to plot
        country_job_df = salary_df[(salary_df['company_location'].isin(['US', 'GB', 'IN'])) &
                                   (salary_df['job_title'].isin(['Data Scientist', 'Big Data Engineer']))].copy()

        fig = go.Figure()

        # Add a trace for the histogram
        fig.add_trace(
            go.Histogram(x=country_job_df['salary_in_usd'],
                         name="Salary Histogram",
                         opacity=0.6)
        )

        # Calculate ECDF
        x = np.sort(country_job_df['salary_in_usd'])
        y = np.arange(1, len(x) + 1) / len(x)

        # Add a trace for the ECDF
        fig.add_trace(
            go.Scatter(x=x, y=y, mode='lines', name="ECDF", yaxis='y2')
        )

        # Update layout to include a title and axis labels
        fig.update_layout(
            title="ECDF and Histogram of Salaries",
            xaxis=dict(
                title="Salary (USD)"
            ),
            yaxis=dict(
                title="Count"
            ),
            yaxis2=dict(
                title="Probability",
                side="right",
                overlaying="y",
            ),
            barmode='overlay'  # Overlay the histogram on the ECDF
        )

        fig.update_layout(width=800, height=800)

        # The background color of the plot is updated to transparent
        fig.update_layout(plot_bgcolor="rgba(0, 0, 0, 0)", width=800, height=800)

        fig.show()

    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except pd.errors.EmptyDataError:
        print(f"No data in {file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function to run the program.

    Returns:
        None
    """
    try:
        plot_salary_distribution()
    except Exception as e:
        print(f"An error occurred in main: {e}")


if __name__ == "__main__":
    main()
