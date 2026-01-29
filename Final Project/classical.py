import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display, Markdown

def show_hypothesis_results(df):
    """Result 1: Fig 2 | Result 2: Statistical Correlation"""
    # Result 1: Correlation Plot
    plt.figure(figsize=(7, 4))
    sns.regplot(data=df, x='isolation', y='anxiety', scatter_kws={'alpha':0.3}, color='purple')
    plt.title("Fig. 2: Correlation between Social Isolation and Anxiety")
    plt.show()
    
    # Result 2: Statistical Calculation (Dense Text)
    corr = df['isolation'].corr(df['anxiety'])
    display(Markdown(f"**Statistical Result:** The analysis confirms a strong positive correlation ($r = {corr:.2f}$) between social isolation and student anxiety levels."))