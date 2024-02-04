import numpy as np
import plotly.graph_objs as go

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
mean = (5000, 5000)
cov = [[1000000, 0], [0, 1000000]]  # Diagonal covariance matrix for independence
num_samples = 10000
x, y = generate_2d_gaussian(mean, cov, num_samples)

# Create a 2D histogram of the x and y data
histogram, x_edges, y_edges = np.histogram2d(x, y, bins=50, range=[[1, 10000], [1, 10000]])

# Create the contour plot
fig = go.Figure(data=go.Contour(z=histogram, x=x_edges, y=y_edges))
fig.update_layout(
    title='2D Gaussian Contour Plot',
    xaxis=dict(title='X Axis'),
    yaxis=dict(title='Y Axis')
)
fig.show()
