import pandas as pd
import numpy as np


def generate_data(num_samples=1000):
    """
    Generate a right-skewed distribution and a categorical variable.
    Adjust the data so that 45% of the values are below the median.

    Args:
        num_samples (int): The number of samples to generate. Default is 1000.

    Returns:
        tuple: A tuple containing the adjusted data and the categorical variable.
    """
    # Generate a right-skewed distribution
    mu, sigma = 0, 0.4  # mean and standard deviation of the underlying normal distribution
    s = np.random.lognormal(mu, sigma, num_samples)

    # Calculate the actual median
    median_value = np.median(s)

    # Adjust the data so that 45% of the values are below the median
    adjusted_s = s * (median_value / np.percentile(s, 45))

    # Create a categorical variable with three categories
    categories = ['Category1', 'Category2', 'Category3']
    category_var = np.random.choice(categories, num_samples)

    return adjusted_s, category_var


def create_dataframe(adjusted_s, category_var):
    """
    Create a DataFrame from the adjusted data and the categorical variable.

    Args:
        adjusted_s (numpy.ndarray): The adjusted data.
        category_var (numpy.ndarray): The categorical variable.

    Returns:
        pandas.DataFrame: The created DataFrame.
    """
    df = pd.DataFrame({
        'Category': category_var,
        'Value': adjusted_s
    })

    return df


def save_dataframe(df, filename):
    """
    Save a DataFrame to a CSV file.

    Args:
        df (pandas.DataFrame): The DataFrame to save.
        filename (str): The name of the CSV file.
    """
    df.to_csv(filename, index=False)


def main():
    """
    The main function that generates the data, creates the DataFrame, and saves it to a CSV file.
    """
    try:
        adjusted_s, category_var = generate_data()
        df = create_dataframe(adjusted_s, category_var)
        save_dataframe(df, '../datafiles/violin_data.csv')
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()