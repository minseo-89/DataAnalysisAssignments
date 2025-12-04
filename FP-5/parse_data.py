import pandas as pd

def get_data(filename='MentalHealthSurvey.csv'):
    try:
        df = pd.read_csv(filename)
        df.columns = df.columns.str.strip()
        print(f"Successfully loaded '{filename}'")
        return df
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None