import pandas as pd 
from preswald import get_df, connect

df = pd.read_csv('../data/raw_data/Star_Data.csv')

df.rename(columns={
    'Star type': 'Star Type',
    'Luminosity(L/Lo)': 'Luminosity',
    'Temperature (K)': 'Temperature',
    'Radius(R/Ro)': 'Radius',
    'Absolute magnitude(Mv)': 'Absolute Magnitude'
}, inplace=True)

df.to_csv('../data/cleaned_data/cleaned_star_data.csv', index=False)