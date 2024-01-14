import plotly.express as px
import pandas as pd


def create_ecdf_plot(data_frame):
    """
    Create an ECDF plot with a marginal histogram using Plotly Express.

    Parameters:
    data_frame (pd.DataFrame): The data frame containing the data to plot.

    Returns:
    plotly.graph_objs._figure.Figure: The ECDF plot figure.
    """
    fig = px.ecdf(
        data_frame,
        x="std_dev_data",
        labels={
            "std_dev_data": "Normal Distribution",
        },
        markers=False,
        lines=True,
        marginal="histogram",
        title="ECDF plot with a marginal histogram - normal distribution",
    )

    # Update the background color of the plot to transparent
    fig.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)", width=800, height=800, showlegend=False
    )

    # Setup x-axis grid lines (verticals)
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor="grey")

    # Disable y-axis grid lines
    fig.update_yaxes(showgrid=False)

    return fig


def main():
    """
    Main function to create and display the ECDF plot.
    """
    try:
        # Assuming df2 is a predefined DataFrame with the necessary data
        df2 = pd.read_csv('../datafiles/random_data.csv')
        fig = create_ecdf_plot(df2)
        fig.show()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
