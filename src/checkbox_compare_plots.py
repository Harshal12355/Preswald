from preswald import text, plotly, checkbox, table

def compare_star_types_individual(df):
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
