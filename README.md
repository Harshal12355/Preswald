# Star Type Analysis and Prediction Tool

## Project Overview

This project provides a comprehensive web-based tool for analyzing and visualizing stellar data, with a focus on star classification and attribute comparison. Built using the Preswald framework, it offers interactive visualizations and statistical analysis of star properties across different star types.

## Features

### 1. Data Exploration

The application begins with a basic overview of the dataset, displaying:
- A header table showing the first few rows of the star dataset
- Information about the 6 classes of stars in the dataset:
  - Brown Dwarf (Type 0)
  - Red Dwarf (Type 1) 
  - White Dwarf (Type 2)
  - Main Sequence (Type 3)
  - Supergiant (Type 4)
  - Hypergiant (Type 5)

### 2. Hertzsprung-Russell Diagram

The app features a comprehensive Hertzsprung-Russell (H-R) diagram, which is fundamental in stellar astronomy:
- Interactive scatter plot showing the relationship between temperature and luminosity
- Logarithmic scale for luminosity to better visualize the vast range of stellar brightness
- Color-coded points representing different star types
- Reversed x-axis (temperature) following astronomical convention
- Annotated regions highlighting key star groups (Giants, Supergiants, Main Sequence, White Dwarfs, Brown/Red Dwarfs)
- Hover functionality showing additional data (Radius, Star color, Spectral Class)
- Educational text explaining the significance of the H-R diagram in stellar classification

### 3. Distribution Analysis

The tool provides box plots for key stellar properties:
- Temperature distribution by star type
- Luminosity distribution by star type
- Simple visualizations with clear labeling and consistent formatting

### 4. Interactive Star Type Comparison Tool

A sophisticated interactive comparison tool allows users to:
- Select specific star types via checkboxes for detailed analysis
- View and compare distributions of Temperature, Luminosity, and Radius across selected star types
- Analyze both box plots (showing statistical distribution) and strip plots (showing individual data points)
- See clear visualizations with:
  - Jittered points for better visibility
  - Notched box plots showing confidence intervals
  - Logarithmic scaling for luminosity
  - Proper categorical axis handling

### 5. Statistical Analysis

For each selected star type, the tool generates detailed statistical tables for:
- Temperature statistics
- Luminosity statistics 
- Radius statistics

Each table includes:
- Count of stars
- Minimum values
- Mean values
- Median values
- Maximum values
- Standard deviation
- Both numerical type IDs and descriptive labels

## Technical Implementation

### Data Handling
- Utilizes SQL queries to filter and process stellar data
- Converts numerical star type values to descriptive labels for better readability
- Handles categorical data appropriately for visualization

### Visualization Techniques
- Uses Plotly Express for interactive visualizations
- Implements specialized astronomical conventions (reversed temperature axis)
- Applies appropriate scales (logarithmic for luminosity)
- Provides consistent styling and formatting across visualizations

### User Interface
- Interactive checkbox selection for customizing analysis
- Clear section headers and explanatory text
- Consistent layout and design elements

## Educational Value

The tool serves as both an analytical instrument and an educational resource:
- Explains key astronomical concepts (H-R diagram, stellar classification)
- Provides context for different star types and their characteristics
- Helps users understand the relationships between stellar properties
- Allows comparison of different star categories side-by-side

## Installation and Dependencies

The application relies on:
- Preswald framework for the web interface
- Pandas for data manipulation
- Plotly Express for interactive visualizations
- NumPy for numerical operations

## Usage

The application is designed to be intuitive and user-friendly:
1. View the general dataset overview
2. Explore the H-R diagram to understand stellar classification
3. Use the comparison tool to select specific star types
4. Analyze the resulting visualizations and statistics
5. Compare different properties across selected star types

This project offers a powerful way to explore stellar data, understand astronomical concepts, and visualize the diversity of stars in our universe.