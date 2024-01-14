import numpy as np
import pandas as pd
from scipy.stats import skewnorm


def generate_and_save_data(size=1000):
    """
    This function generates left-skewed, standard deviation, and right-skewed data,
    and saves them into a CSV file.

    Parameters:
    size (int): The size of the data to generate. Default is 1000.

    Returns:
    None
    """
    try:
        # Generate left-skewed data
        left_skewed_data = skewnorm.rvs(-10, size=size)

        # Generate standard deviation data
        std_dev_data = np.random.normal(0, 1, size)

        # Generate right-skewed data
        right_skewed_data = skewnorm.rvs(10, size=size)

        # Create a DataFrame
        df = pd.DataFrame(
            {
                "left_skewed_data": left_skewed_data,
                "std_dev_data": std_dev_data,
                "right_skewed_data": right_skewed_data,
            }
        )

        # Write the DataFrame to a CSV file
        df.to_csv("../datafiles/random_data.csv", index=False)

    except Exception as e:
        print(f"An error occurred: {e}")
        raise


def main():
    """
    The main function that generates the data, creates the DataFrame, and saves it to a CSV file.
    """
    try:
        generate_and_save_data()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

    # try:
    #     generate_and_save_data()
    # except Exception as e:
    #     print(f"An error occurred in the main function: {e}")
    #
