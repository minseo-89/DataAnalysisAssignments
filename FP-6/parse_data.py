import pandas as pd

def get_data(filename='MentalHealthSurvey.csv'):
    try:
        df = pd.read_csv(filename)
        df.columns = df.columns.str.strip()
        sleep_mapping = {
            '2-4 hrs': 3.0,
            '4-6 hrs': 5.0,
            '7-8 hrs': 7.5
        }
        
        if 'average_sleep' in df.columns:
            df['average_sleep'] = df['average_sleep'].map(sleep_mapping)
        df = df.dropna(subset=['average_sleep', 'academic_pressure', 'depression'])
        
        print(f"Successfully loaded and preprocessed '{filename}'")
        return df
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None