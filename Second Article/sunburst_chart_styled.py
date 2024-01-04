import plotly.express as px
import pandas as pd

def read_data(file_path="../datafiles/taxonomy.csv"):
    """
    Function to read data from a csv file into a pandas DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def count_risks(df):
    """
    Function to count the occurrences of each combination of risks.
    """
    try:
        df_count = df.groupby(["L1 Risk", "L2 Risk", "L3 Risk"]).size().reset_index(name="counts")
        return df_count
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def create_sunburst_chart(df_count):
    """
    Function to create a sunburst chart from the data.
    """
    try:
        fig = px.sunburst(
            df_count,
            path=["L1 Risk", "L2 Risk", "L3 Risk"],
            values="counts",
            title="Risk Data Displayed on a Sunburst Chart",
        )

        fig.update_traces(
            textinfo="label+value",
            texttemplate="%{label}:<br> Risks: %{value:.0f}",
            insidetextorientation="radial",
        )

        fig.update_layout(showlegend=False, autosize=False, width=1000, height=1000)
        return fig
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    """
    Main function to orchestrate the reading of data, counting of risks, and creation of the sunburst chart.
    """
    try:
        df = read_data()
        if df is not None:
            df_count = count_risks(df)
            if df_count is not None:
                fig = create_sunburst_chart(df_count)
                if fig is not None:
                    fig.show()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()