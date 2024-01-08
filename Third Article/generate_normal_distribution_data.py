import numpy as np
import pandas as pd


def generate_data(mean, standard_deviation, number_of_samples):
    """
    Generate normally distributed data.

    Parameters:
    mean (float): The mean of the normal distribution.
    standard_deviation (float): The standard deviation of the normal distribution.
    number_of_samples (int): The number of samples to generate.

    Returns:
    numpy.ndarray: The generated data.
    """
    return np.random.normal(mean, standard_deviation, number_of_samples)


def convert_to_dataframe(data):
    """
    Convert a numpy array to a pandas DataFrame.

    Parameters:
    data (numpy.ndarray): The data to convert.

    Returns:
    pandas.DataFrame: The converted data.
    """
    return pd.DataFrame(data, columns=['Value'])


def save_to_csv(df, filepath):
    """
    Save a DataFrame to a CSV file.

    Parameters:
    df (pandas.DataFrame): The DataFrame to save.
    filepath (str): The path to the file to save the DataFrame to.
    """
    df.to_csv(filepath, index=False)


def main():
    """
    The main function of the script.
    """
    try:
        # Define the parameters for the normal distribution
        mean = 0
        standard_deviation = 1
        number_of_samples = 1000

        # Generate the normally distributed dataset
        data = generate_data(mean, standard_deviation, number_of_samples)

        # Convert the numpy array to a pandas DataFrame
        df = convert_to_dataframe(data)

        # Save the DataFrame to a CSV file
        save_to_csv(df, '../datafiles/normal_distribution.csv')
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()