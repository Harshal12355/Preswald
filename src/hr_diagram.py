from preswald import text, plotly
import pandas as pd
import plotly.express as px

def create_hr_diagram(df):
    
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
