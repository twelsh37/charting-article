# Import necessary libraries
import plotly.express as px
import pandas as pd


def create_funnel_chart():
    """
    This function creates a funnel chart for the number of people at each stage of the funnel for different offices.
    It uses Plotly Express to create the chart and pandas to handle the data.
    """
    try:
        # Define the stages of the funnel
        stages = [
            "Website visit",
            "Downloads",
            "Potential customers",
            "Requested price",
            "invoice sent",
        ]

        # Create a DataFrame for Montreal office with number of people at each stage
        df_mtl = pd.DataFrame({"number": [39, 27.4, 20.6, 11, 3], "stage": stages})
        df_mtl["office"] = "Montreal"

        # Create a DataFrame for Toronto office with number of people at each stage
        df_toronto = pd.DataFrame({"number": [52, 36, 18, 14, 5], "stage": stages})
        df_toronto["office"] = "Toronto"

        # Create a DataFrame for Ontario office with number of people at each stage
        df_ontario = pd.DataFrame({"number": [29, 22, 17, 12, 2], "stage": stages})
        df_ontario["office"] = "Ontario"

        # Create a DataFrame for Vancouver office with number of people at each stage
        df_vancouver = pd.DataFrame({"number": [29, 22, 17, 12, 2], "stage": stages})
        df_vancouver["office"] = "Vancouver"

        # Concatenate the four DataFrames along the row axis (axis=0)
        df = pd.concat([df_mtl, df_toronto, df_ontario, df_vancouver], axis=0)

        # Create a funnel chart with number of people on the x-axis, stages on the y-axis,
        # and office as the color dimension
        fig = px.funnel(
            df,
            x="number",
            y="stage",
            color="office",
            title="Website Onboarding Funnel",
        )

        # The background color of the plot is updated to transparent
        fig.update_layout(plot_bgcolor="rgba(0, 0, 0, 0)")

        # Display the figure
        fig.show()

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Execute the main workflow.
    """
    try:
        # Call the function to create the funnel chart
        create_funnel_chart()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
