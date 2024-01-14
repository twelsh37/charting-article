import plotly.express as px
import pandas as pd


def create_ecdf_plot(dataframe):
    """
    Create an ECDF plot with a marginal histogram for a given DataFrame.

    Parameters:
    dataframe: The DataFrame containing the data to plot.

    Returns:
    plotly.graph_objs._figure.Figure: The ECDF plot figure.
    """
    fig = px.ecdf(
        dataframe,
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

    # Setup x Axis grid lines (verticals)
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor="grey")

    # Disable Y axis grid lines
    fig.update_yaxes(showgrid=False)

    return fig


def main():
    """
    Main function to create and display the ECDF plot.
    """
    try:
        df2 = pd.read_csv('../datafiles/random_data.csv')
        fig = create_ecdf_plot(df2)
        fig.show()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
