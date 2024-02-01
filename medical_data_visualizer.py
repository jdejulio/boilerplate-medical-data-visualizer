import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
csv_file = "medical_examination.csv"
df = pd.read_csv(csv_file)

# Add 'overweight' column
df['overweight'] = df.apply(lambda row: "1" if row["weight"]/(row["height"]/100*row["height"]/100) > 25 else "0", axis=1)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
def normalize(value):
    if value in [1]:
        return 0
    elif value in [2, 3]:
        return 1
    else:
        return None
    
df["cholesterol"] = df["cholesterol"].apply(normalize)
df["gluc"] = df["gluc"].apply(normalize)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    columns_of_interest = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke', 'cardio']
    df_filtered = df[columns_of_interest]
    df_filtered_str = df_filtered.astype('str')

# Convertir a formato "largo" usando melt
    df_long = df_filtered_str.melt(id_vars=['cardio'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    grouped_df = df_long.groupby(['cardio', 'variable', 'value']).size().reset_index(name='count')
    

    # Draw the catplot with 'sns.catplot()'
    sns.catplot(data=grouped_df, x="variable", y="count", col="cardio", hue="value", kind="bar")
    plt.show()



    # Get the figure for the output
    fig = plt.gcf()


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig



# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.loc[df['ap_lo'] <= df['ap_hi']]
    df_heat = df_heat.loc[df['height'] >= df['height'].quantile(0.025)]
    df_heat = df_heat.loc[df['height'] <= df['height'].quantile(0.975)]
    df_heat = df_heat.loc[df['weight'] >= df['weight'].quantile(0.025)]
    df_heat = df_heat.loc[df['weight'] <= df['weight'].quantile(0.975)]

    # Calculate the correlation matrix
    corr = df_heat.corr("pearson")
    
    # Generate a mask for the upper triangle
    mask_pattern = np.triu(np.ones(corr.shape), k=0).astype(bool)
    corr_masked = corr.mask(mask_pattern)


    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr_masked, annot=corr_masked.round(1))


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
