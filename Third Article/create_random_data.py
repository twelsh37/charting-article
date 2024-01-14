import numpy as np
import pandas as pd
from scipy.stats import skewnorm

# Set the size of the data
size = 1000

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
df.to_csv("random_data.csv", index=False)
