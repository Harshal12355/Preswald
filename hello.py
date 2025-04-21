import plotly.express as px
from preswald import (
    text, 
    plotly, 
    connect, 
    get_df, 
    table,
    query,
    slider,
)

# Set the title of the app
text("# Titanic Data Analysis") # Uses markdown syntax
# Add a subtitle
text("### This app looks into titanic data! 🎉")

# Load the CSV
connect()
df = get_df('titanic_csv')

#Filtering the data using SQL
sql = "SELECT * FROM titanic_csv WHERE Age > 20"
filtered_df = query(sql, "titanic_csv")
text(f"Filtered DataFrame shape: {filtered_df.shape}, this is the type of the data: {type(filtered_df)}")
print(filtered_df)

# Display the data

# Displaying without any filtering
text("### Displaying without any filtering")
# Create a scatter plot
fig = px.scatter(df, x='Age', y='Fare',
                 title='Age vs. Fare',
                 labels={'Age': 'Age', 'Fare': 'Fare'},
                 color="Sex")
# Add labels for each point
fig.update_traces(textposition='top center', marker=dict(size=12, color='lightblue'))
# Style the plot
fig.update_layout(template='plotly_white')
# Show the plot
plotly(fig)

# Show the data
text("### Dynamic Data View")
threshold = slider("Threshold", min_val=0, max_val=100, default=20)
table(df[df["Age"] > threshold], title="Dynamic Titanic Data View")

# # Show the data
# table(df, title="Titanic Data")


#Displaying with filtering 
text("### Displaying with filtering")
# Create a scatter plot
fig = px.scatter(filtered_df, x='Age', y='Fare',
                 title='Age vs. Fare (Filtered)',
                 labels={'Age': 'Age', 'Fare': 'Fare'})
# Add labels for each point 
fig.update_traces(textposition='top center', marker=dict(size=12, color='lightgreen'))
# Style the plot
fig.update_layout(template='plotly_white')
# Show the plot
plotly(fig)

# Show the data
table(filtered_df, title="Titanic Filtered Data")