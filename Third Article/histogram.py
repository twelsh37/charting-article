import pandas as pd
import numpy as np
import plotly.express as px

# read in our dataset
df = pd.read_csv('../datafiles/age.csv')

# setup our colum renames'
nom = {'Lower tier local authorities Code': 'ltlac',
        'Lower tier local authorities': 'region',
        'Age (101 categories) Code': 'age_code',
        'Age (101 categories)': 'age',
        'Observation': 'number'
       }

# Rename our columns
df.rename(columns=nom, inplace=True)

# Function to generate bins and labels
def generate_bins_labels(bin_width):
    # np.inf ensures anything above 100 goes into the last bin
    bins = list(range(0, 101, bin_width)) + [np.inf]
    labels = [f'{i+1} - {i + bin_width}' for i in bins[:-2]] + [f'{bins[-2]+1}+']
    return bins, labels

# Define the bin width
bin_width = 10  # Adjusted to 10 items per bin

# Generate bins and labels
bins, labels = generate_bins_labels(bin_width)

# Create a new column for the binned ages
df['age_group'] = pd.cut(df['age_code'], bins=bins, labels=labels, include_lowest=True)

# Group by 'age_group' and sum 'number'
df_grouped = df.groupby('age_group', observed=True)['number'].sum().reset_index()

fig = px.histogram(df_grouped, x = 'age_group', y = 'number')
fig.update_layout(width=800, height=800)
fig.show()