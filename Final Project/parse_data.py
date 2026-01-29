import pandas as pd

def get_data(filename='MentalHealthSurvey.csv'):
    try:
        df = pd.read_csv(filename)
        df.columns = df.columns.str.strip()
        
        if 'average_sleep' in df.columns:
            df['average_sleep'] = df['average_sleep'].str.strip()
            sleep_mapping = {'2-4 hrs': 3.0, '4-6 hrs': 5.0, '7-8 hrs': 7.5}
            df['average_sleep'] = df['average_sleep'].map(sleep_mapping)
        
        # Keep only necessary rows for a dense analysis
        critical_cols = ['average_sleep', 'academic_pressure', 'depression', 'anxiety', 'isolation']
        df = df.dropna(subset=critical_cols)
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None