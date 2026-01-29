import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display, Markdown

def show_descriptive_results(df):
    """Result 1: Table 1 | Result 2: Fig 1"""
    # Result 1: Key Statistics Table
    cols = ['depression', 'academic_pressure', 'average_sleep', 'anxiety']
    stats = df[cols].describe().loc[['mean', 'std']]
    stats.index = ['Average', 'Volatility (Std)']
    display(Markdown("**Table 1: Summary of Student Mental Health Metrics**"))
    display(stats.round(2))
    
    # Result 2: Scatter Plot with Regression Line
    plt.figure(figsize=(7, 4))
    sns.regplot(data=df, x='academic_pressure', y='depression', scatter_kws={'alpha':0.3}, color='teal')
    plt.title("Fig. 1: Impact of Academic Pressure on Depression Scores")
    plt.xlabel("Academic Pressure (Scale 1-5)")
    plt.ylabel("Depression Score")
    plt.show()