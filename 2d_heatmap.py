import numpy as np
import plotly.express as px

# Function to generate 2D Gaussian data
def generate_2d_gaussian(mean, cov, num_samples):
    """
    Generates 2D Gaussian data based on the mean, covariance matrix, and number of samples.

    :param mean: A tuple representing the mean of the distribution (mean_x, mean_y)
    :param cov: A 2x2 covariance matrix
    :param num_samples: The number of samples to generate
    :return: A tuple of numpy arrays (x, y) representing the generated samples
    """
    data = np.random.multivariate_normal(mean, cov, num_samples)
    return data[:, 0], data[:, 1]

# Generate data
mean = (0, 0)
cov = [[1, 0], [0, 1]]  # Diagonal covariance matrix for independence
num_samples = 1000
x, y = generate_2d_gaussian(mean, cov, num_samples)

# Create and show the heatmap
fig = px.density_heatmap(x=x, y=y, nbinsx=31, nbinsy=31)
fig.update_layout(
    title='2D Density Heatmap. Bin Size = 31',
    xaxis=dict(title='X Axis', showgrid=True, gridcolor='black'),
    yaxis=dict(title='Y Axis', showgrid=True, gridcolor='black'),
    coloraxis_colorbar=dict(title='Density')
)
fig.show()
