from preswald import connect, get_df

def load():
    """Load the star_csv dataset."""
    connect()
    return get_df('star_csv')
