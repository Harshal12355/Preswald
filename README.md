# Star Type Analysis and Prediction Tool

## Project Overview
A web-based tool for analyzing stellar data, visualizing star classifications, and comparing star properties across different types. Built with Preswald framework for interactive astronomical data exploration.

## Key Features

### Data Exploration
- Quick overview of the star dataset with 6 classes (Brown Dwarf, Red Dwarf, White Dwarf, Main Sequence, Supergiant, Hypergiant)
- Visual representation of the dataset's structure

### Visualizations
- **Hertzsprung-Russell Diagram**: Interactive scatter plot showing temperature vs. luminosity relationships
  - Color-coded by star type with astronomical conventions (reversed temperature axis)
  - Annotated regions highlighting star classification groups
  
- **Distribution Analysis**: Box plots showing temperature and luminosity distributions by star type

- **Interactive Comparison Tool**: Checkbox-based selection to compare specific star types
  - Box plots and strip plots for Temperature, Luminosity, and Radius
  - Statistical tables with key metrics for selected star types

## Technical Features
- SQL queries for data filtering
- Plotly Express visualizations with specialized astronomical customizations
- Categorical data handling with proper labeling
- Statistical analysis with comprehensive metrics

## Dependencies
- Preswald framework
- Pandas, Plotly Express, NumPy

## Usage
1. View dataset overview
2. Explore the H-R diagram
3. Use the comparison tool to select star types
4. Analyze visualizations and statistics

## Issues I had
- Had trouble making visualisations using loops
- Had trouble making subplots
- Found the visualisations to be static, had trouble changing them using the slider
- Could not modularise the code, for some reason it would not recognise modules that were made, so all the code had to be in the same file 
- Tried to change the logo and the favicon, but it would not change
    - removed them but still kept the file path and it did not change anything, not even an error 
    - instead when I removed them from the images folder, did preswald run and then it reuploaded the icons and the favicon, so basically it was impossible to change them 
- Had trouble using the online code editor, the pointer was in a weird position and whenever I exited the code editor would wipe out all the code I wrote, so I downloaded the project 
