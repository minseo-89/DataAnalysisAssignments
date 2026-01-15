import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, Markdown
import parse_data as ps

def display_title(s, pref='Figure', num=1, center=False):
    ctag = 'center' if center else 'p'
    s = f'<{ctag}><span style="font-size: 1.2em;"><b>{pref} {num}</b>: {s}</span></{ctag}>'
    display(Markdown(s))

def central(x):
    if len(x) == 0: return None, None, None
    return x.mean(), x.median(), x.mode()[0]

def dispersion(x):
    if len(x) == 0: return None, None, None, None, None, None, None
    return x.std(), x.min(), x.max(), x.max()-x.min(), x.quantile(0.25), x.quantile(0.75), x.quantile(0.75)-x.quantile(0.25)

def check_data_quality(df):
    display_title('Data Quality and Missing Values Check', pref='Table', num=0)
    quality_df = pd.DataFrame({
        'Missing Values': df.isnull().sum(),
        'Data Type': df.dtypes
    })
    display(quality_df)

def display_summary_tables(df):
    cols = ['age', 'depression', 'academic_pressure', 'average_sleep', 'anxiety', 'isolation']
    
    display_title('Central Tendency Summary Statistics', pref='Table', num=1)
    df_central = df[cols].apply(central).apply(pd.Series)
    df_central.index = ['Mean', 'Median', 'Mode']
    display(df_central.round(2))
    
    display_title('Dispersion Summary Statistics', pref='Table', num=2)
    df_disp = df[cols].apply(dispersion).apply(pd.Series)
    df_disp.index = ['St.Dev', 'Min', 'Max', 'Range', '25%', '75%', 'IQR']
    display(df_disp.round(2))

def plot_distributions(df):
    cols = ['depression', 'academic_pressure', 'average_sleep', 'anxiety']
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    for ax, col in zip(axs.ravel(), cols):
        sns.histplot(df[col], kde=True, ax=ax, color='skyblue')
        ax.set_title(f'Distribution of {col.replace("_", " ").title()}')
    plt.tight_layout()
    display_title('Distribution Analysis of Key Variables', pref='Figure', num=1)
    plt.show()

if __name__ == "__main__":
    df = ps.get_data()
    if df is not None:
        check_data_quality(df)
        display_summary_tables(df)
        plot_distributions(df)