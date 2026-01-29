import pandas as pd

def get_data(filename='MentalHealthSurvey.csv'):
    try:
        df = pd.read_csv(filename)
        df.columns = df.columns.str.strip()
        
        # 1. Map text categories to numbers
        if 'average_sleep' in df.columns:
            df['average_sleep'] = df['average_sleep'].str.strip()
            sleep_mapping = {'2-4 hrs': 3.0, '4-6 hrs': 5.0, '7-8 hrs': 7.5}
            df['average_sleep'] = df['average_sleep'].map(sleep_mapping)
        
        # 2. Drop missing values in critical columns
        cols = ['depression', 'academic_pressure', 'average_sleep', 'anxiety', 'isolation']
        df = df.dropna(subset=cols)
        
        # 3. IQR Outlier Removal (Addresses instructor feedback)
        # This cleans the data for BOTH classical and ML analysis
        Q1 = df[cols].quantile(0.25)
        Q3 = df[cols].quantile(0.75)
        IQR = Q3 - Q1
        
        # Keep rows that are NOT outliers (within 1.5 * IQR)
        df = df[~((df[cols] < (Q1 - 1.5 * IQR)) | (df[cols] > (Q3 + 1.5 * IQR))).any(axis=1)]
        
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None