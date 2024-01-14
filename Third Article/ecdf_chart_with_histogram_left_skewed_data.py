import plotly.express as px
import pandas as pd


def plot_ecdf(df, x_column):
    """
    This function plots an Empirical Cumulative Distribution Function (ECDF)
    with a marginal histogram for a given DataFrame and column.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    x_column (str): The column in the DataFrame to plot.

    Returns:
    plotly.graph_objects.Figure: The ECDF plot.
    """
    try:
        fig = px.ecdf(df,
                      x=x_column,
                      labels={x_column: "Left Skewed Data"},
                      markers=False,
                      lines=True,
                      marginal="histogram",
                      title='ECDF plot with a marginal histogram - left skewed distribution'
                     )

        fig.update_layout(plot_bgcolor="rgba(0, 0, 0, 0)", width=800, height=800, showlegend=False)
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor="grey")
        fig.update_yaxes(showgrid=False)

        return fig

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    try:
        # Assuming df2 is defined and 'right_skewed_data' is a column in df2
        df2 = pd.read_csv('../datafiles/random_data.csv')  # Replace with actual DataFrame
        plot = plot_ecdf(df2, 'left_skewed_data')
        plot.show()

    except Exception as e:
        print(f"An error occurred in main: {e}")
