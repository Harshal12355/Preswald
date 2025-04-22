from preswald import (
    text,
    plotly,
    table,
    connect,
    get_df,
    query,
    slider,
    topbar,
    checkbox,
    sidebar,
    separator
)
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import time
import numpy as np

topbar()
sidebar(defaultopen=True)

text("# Star Type Analysis and Prediction")
text(" ## 📊 Preswald and Star Type Analytics & Prediction")
text("### Introduction")
text("This app is designed to analyze and predict star types based on various features. It utilizes the Preswald library for data visualization and SQL queries for data manipulation.")
text("""
This CSV file contains a dataset of 240 stars of 6 classes:

- Brown Dwarf -> Star Type = 0

- Red Dwarf -> Star Type = 1

- White Dwarf-> Star Type = 2

- Main Sequence -> Star Type = 3

- Supergiant -> Star Type = 4

- Hypergiant -> Star Type = 5

The Luminosity and radius of each star is calculated w.r.t. that of the values of Sun.
Lo = 3.828 x 10^26 Watts
Ro = 6.9551 x 10^8 m
     """)

#Importing Dataset

# Load the CSV from data/cleaned_data/cleaned_star_data.csv
# df = load()

separator()

connect()
df = get_df('star_csv')

text("### Here is a glimpse of the dataset:")
table(df.head(), title="Star Data")

# # Data Preprocessing and Cleaning  
# EDA Data Visualizations
sql_query = """
    SELECT 
        Temperature, 
        Luminosity, 
        Radius,
        "Absolute Magnitude", 
        "Star color", 
        "Spectral Class"
    FROM star_csv
"""
filtered_df = query(sql_query, "star_csv")
cols = filtered_df.columns.tolist()

separator()
def create_hr_diagram():
    
    # Create the Hertzsprung-Russell diagram
    text("### Hertzsprung-Russell Diagram")
    text("The Hertzsprung-Russell diagram is a scatter plot of stars showing the relationship between" \
    "\n a star's temperature and its luminosity. This visualization helps astronomers classify stars" \
    "\n into different categories based on their position in the diagram."
    "\n\n" \
    "\n Note: In traditional H-R diagrams, temperature increases from right to left to match astronomical conventions.")
    
    # Create the figure with temperature on x-axis and luminosity on y-axis
    fig = px.scatter(
        df, 
        x='Temperature', 
        y='Luminosity',
        color='Star Type',
        hover_data=['Radius', 'Star color', 'Spectral Class'],
        labels={
            'Temperature': 'Temperature (K)',
            'Luminosity': 'Luminosity (L/Lo)',
            'Star Type': 'Star Classification'
        },
        title='Hertzsprung-Russell Diagram',
        log_y=True  # Use logarithmic scale for luminosity
    )
    
    # Customize the layout to match astronomical convention (temp decreases left to right)
    fig.update_xaxes(autorange="reversed")
    
    # Add additional customization to make the plot more readable
    fig.update_layout(
        height=700,
        width=900,
        legend_title='Star Classification',
        xaxis_title='Surface Temperature (K)',
        yaxis_title='Luminosity (relative to Sun)',
        template='plotly_white'
    )
    
    # Add annotations to highlight different regions
    fig.add_annotation(
        x=3000, y=100,
        text="Giants",
        showarrow=True,
        arrowhead=1
    )
    
    fig.add_annotation(
        x=10000, y=100,
        text="Supergiants",
        showarrow=True,
        arrowhead=1
    )
    
    fig.add_annotation(
        x=6000, y=100,
        text="Main Sequence",
        showarrow=True,
        arrowhead=1
    )
    
    fig.add_annotation(
        x=15000, y=100,
        text="White Dwarfs",
        showarrow=True,
        arrowhead=1
    )
    
    fig.add_annotation(
        x=3200, y=100,
        text="Brown/Red Dwarfs",
        showarrow=True,
        arrowhead=1
    )
    
    plotly(fig)
    
    # Add explanation of the diagram
    text("### Understanding the H-R Diagram")
    text("- **Main Sequence Stars**: Form a diagonal band from bottom-right to top-left. These are stars in the stable part of their lifecycle, including our Sun. " \
    "\n - **Giants and Supergiants**: Located at the upper-right of the diagram, these are large stars with high luminosity but relatively low surface temperature." \
    "\n - **Main Sequence**: Stars like the Sun are found along the diagonal band, where they fuse hydrogen into helium in their cores." \
    "\n - **White Dwarfs**: Found at the lower-left, these are remnants of stars that have exhausted their nuclear fuel and shed their outer layers." \
    "\n - **Red and Brown Dwarfs**: At the lower-right, these are small, cool stars with low luminosity." \
    "\nThe H-R diagram reveals important relationships between stellar properties and helps astronomers understand stellar evolution."
    )

# Call the function to display the H-R diagram
create_hr_diagram()

separator()

# from src.box_plots import separate_box_plots <-- not sure why the imports are not working (No module named 'src')
def separate_box_plots():
    text("### Temperature Distribution by Star Type")
    fig1 = px.box(df, x='Star Type', y='Temperature', color='Star Type')
    fig1.update_layout(height=400, width=800, showlegend=False)
    plotly(fig1)
    
    text("### Luminosity Distribution by Star Type")
    fig2 = px.box(df, x='Star Type', y='Luminosity', color='Star Type')
    fig2.update_layout(height=400, width=800, showlegend=False)
    plotly(fig2)

# Call the function with separate plots instead
separate_box_plots()

separator()

def compare_star_types_individual():
    text("# Star Type Comparison Tool")
    
    # Define star type labels
    star_type_labels = {
        0: "Brown Dwarf",
        1: "Red Dwarf",
        2: "White Dwarf",
        3: "Main Sequence",
        4: "Supergiant",
        5: "Hypergiant"
    }
    
    text("### Select star types to compare:")
    
    # Individual checkboxes for each star type
    selected_types = []
    
    # Type 0 - Brown Dwarf
    if checkbox(f"{star_type_labels[0]} (Type 0)", default=True):
        selected_types.append(0)
    
    # Type 1 - Red Dwarf
    if checkbox(f"{star_type_labels[1]} (Type 1)", default=True):
        selected_types.append(1)
    
    # Type 2 - White Dwarf
    if checkbox(f"{star_type_labels[2]} (Type 2)", default=False):
        selected_types.append(2)
    
    # Type 3 - Main Sequence
    if checkbox(f"{star_type_labels[3]} (Type 3)", default=False):
        selected_types.append(3)
    
    # Type 4 - Supergiant
    if checkbox(f"{star_type_labels[4]} (Type 4)", default=False):
        selected_types.append(4)
    
    # Type 5 - Hypergiant
    if checkbox(f"{star_type_labels[5]} (Type 5)", default=False):
        selected_types.append(5)
    
    if not selected_types:
        text("⚠️ Please select at least one star type to analyze.")
        return
    
    # Filter data for selected types
    compare_df = df[df["Star Type"].isin(selected_types)].copy()
    
    # Convert Star Type to string for better categorical plotting
    compare_df["Star Type"] = compare_df["Star Type"].astype(str)
    
    # Add descriptive labels for display
    compare_df["Star Classification"] = compare_df["Star Type"].map(star_type_labels)
    
    text(f"### Comparing {len(selected_types)} star types with {len(compare_df)} total stars")
    
    # Temperature Distribution
    text("### Temperature Comparison")
    temp_fig = px.box(
        compare_df, 
        x="Star Type",  
        y="Temperature", 
        color="Star Type",
        title="Temperature Distribution by Star Type",
        points="all",  
        notched=True,  
        category_orders={"Star Type": [str(t) for t in sorted(selected_types)]}
    )
    
    temp_fig.update_traces(
        jitter=0.3, 
        pointpos=-1.8, 
        boxpoints='all',
        marker_size=4
    )
    
    temp_fig.update_layout(
        height=500,
        width=900,
        xaxis_title="Star Type",
        yaxis_title="Temperature (K)",
        showlegend=True,
        xaxis_type='category'
    )
    
    plotly(temp_fig)
    
    # Individual Temperature scatter plot
    text("### Individual Temperature Values by Star Type")
    temp_scatter_fig = px.strip(
        compare_df,
        x="Star Type",
        y="Temperature",
        color="Star Type",
        title="Individual Temperature Values by Star Type",
        category_orders={"Star Type": [str(t) for t in sorted(selected_types)]}
    )
    
    temp_scatter_fig.update_layout(
        height=400,
        width=900,
        xaxis_title="Star Type",
        yaxis_title="Temperature (K)",
        xaxis_type='category'
    )
    
    plotly(temp_scatter_fig)
    
    # Luminosity Distribution
    text("### Luminosity Comparison")
    lum_fig = px.box(
        compare_df, 
        x="Star Type",  
        y="Luminosity", 
        color="Star Type",
        title="Luminosity Distribution by Star Type",
        points="all",  
        notched=True,  
        category_orders={"Star Type": [str(t) for t in sorted(selected_types)]}
    )
    
    lum_fig.update_traces(
        jitter=0.3, 
        pointpos=-1.8, 
        boxpoints='all',
        marker_size=4
    )
    
    lum_fig.update_layout(
        height=500,
        width=900,
        xaxis_title="Star Type",
        yaxis_title="Luminosity (L/Lo)",
        showlegend=False,
        xaxis_type='category',
        yaxis_type="log"  # Logarithmic scale for luminosity
    )
    
    plotly(lum_fig)
    
    # Individual Luminosity scatter plot
    text("### Individual Luminosity Values by Star Type")
    lum_scatter_fig = px.strip(
        compare_df,
        x="Star Type",
        y="Luminosity",
        color="Star Type",
        title="Individual Luminosity Values by Star Type",
        category_orders={"Star Type": [str(t) for t in sorted(selected_types)]}
    )
    
    lum_scatter_fig.update_layout(
        height=400,
        width=900,
        xaxis_title="Star Type",
        yaxis_title="Luminosity (L/Lo)",
        xaxis_type='category',
        yaxis_type="log"  # Logarithmic scale for luminosity
    )
    
    plotly(lum_scatter_fig)
    
    # Radius Distribution
    text("### Radius Comparison")
    rad_fig = px.box(
        compare_df, 
        x="Star Type",  
        y="Radius", 
        color="Star Type",
        title="Radius Distribution by Star Type",
        points="all",  
        notched=True,  
        category_orders={"Star Type": [str(t) for t in sorted(selected_types)]}
    )
    
    rad_fig.update_traces(
        jitter=0.3, 
        pointpos=-1.8, 
        boxpoints='all',
        marker_size=4
    )
    
    rad_fig.update_layout(
        height=500,
        width=900,
        xaxis_title="Star Type",
        yaxis_title="Radius (R/Ro)",
        showlegend=False,
        xaxis_type='category'
    )
    
    plotly(rad_fig)
    
    # Statistics Tables
    text("### Statistical Comparison")
    
    # Temperature Statistics
    text("#### Temperature Statistics")
    temp_stats = compare_df.groupby("Star Type")["Temperature"].agg([
        ("Count", "count"),
        ("Minimum", "min"),
        ("Mean", "mean"),
        ("Median", "median"),
        ("Maximum", "max"),
        ("Std Dev", "std")
    ]).reset_index()
    
    # Round temperature stats
    for col in temp_stats.columns:
        if col != "Star Type":
            temp_stats[col] = temp_stats[col].round(2)
    
    # Add descriptive names for star types
    temp_stats["Star Classification"] = temp_stats["Star Type"].map(
        {str(k): v for k, v in star_type_labels.items()}
    )
    
    # Reorder columns for temperature
    temp_stats = temp_stats[["Star Type", "Star Classification", "Count", "Minimum", "Mean", "Median", "Maximum", "Std Dev"]]
    table(temp_stats)
    
    # Luminosity Statistics
    text("#### Luminosity Statistics")
    lum_stats = compare_df.groupby("Star Type")["Luminosity"].agg([
        ("Count", "count"),
        ("Minimum", "min"),
        ("Mean", "mean"),
        ("Median", "median"),
        ("Maximum", "max"),
        ("Std Dev", "std")
    ]).reset_index()
    
    # Round luminosity stats
    for col in lum_stats.columns:
        if col != "Star Type":
            lum_stats[col] = lum_stats[col].round(2)
    
    # Add descriptive names for star types
    lum_stats["Star Classification"] = lum_stats["Star Type"].map(
        {str(k): v for k, v in star_type_labels.items()}
    )
    
    # Reorder columns for luminosity
    lum_stats = lum_stats[["Star Type", "Star Classification", "Count", "Minimum", "Mean", "Median", "Maximum", "Std Dev"]]
    table(lum_stats)
    
    # Radius Statistics
    text("#### Radius Statistics")
    rad_stats = compare_df.groupby("Star Type")["Radius"].agg([
        ("Count", "count"),
        ("Minimum", "min"),
        ("Mean", "mean"),
        ("Median", "median"),
        ("Maximum", "max"),
        ("Std Dev", "std")
    ]).reset_index()
    
    # Round radius stats
    for col in rad_stats.columns:
        if col != "Star Type":
            rad_stats[col] = rad_stats[col].round(2)
    
    # Add descriptive names for star types
    rad_stats["Star Classification"] = rad_stats["Star Type"].map(
        {str(k): v for k, v in star_type_labels.items()}
    )
    
    # Reorder columns for radius
    rad_stats = rad_stats[["Star Type", "Star Classification", "Count", "Minimum", "Mean", "Median", "Maximum", "Std Dev"]]
    table(rad_stats)

# Run the individual comparison tool without loops
compare_star_types_individual()