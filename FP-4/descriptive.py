import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, Markdown

def display_title(s, pref='Figure', num=1, center=False):
    ctag = 'center' if center else 'p'
    s = f'<{ctag}><span style="font-size: 1.2em;"><b>{pref} {num}</b>: {s}</span></{ctag}>'
    display(Markdown(s))

def corrcoeff(x, y):
    return np.corrcoef(x, y)[0, 1]

def plot_regression_line(ax, x, y, **kwargs):
    if len(x) > 1:
        a, b = np.polyfit(x, y, 1)
        ax.plot(x, a*x + b, **kwargs)

def central(x):
    if len(x) == 0: return None, None, None
    return x.mean(), x.median(), x.mode()[0]

def dispersion(x):
    if len(x) == 0: return None, None, None, None, None, None, None
    return x.std(), x.min(), x.max(), x.max()-x.min(), x.quantile(0.25), x.quantile(0.75), x.quantile(0.75)-x.quantile(0.25)

def display_central_tendency_table(df, num=1):
    display_title('Central tendency summary statistics.', pref='Table', num=num)
    target_df = df[['age', 'depression', 'academic_pressure', 'financial_concerns']]
    df_out = target_df.apply(central).apply(pd.Series)
    df_out.index = ['Mean', 'Median', 'Mode']
    display(df_out.round(2))

def display_dispersion_table(df, num=2):
    display_title('Dispersion summary statistics.', pref='Table', num=num)
    target_df = df[['age', 'depression', 'academic_pressure', 'financial_concerns']]
    df_out = target_df.apply(dispersion).apply(pd.Series)
    df_out.index = ['St.Dev', 'Min', 'Max', 'Range', '25%', '75%', 'IQR']
    display(df_out.round(2))

def plot_descriptive(df):
    y = df['depression']
    age = df['age']
    press = df['academic_pressure']
    money = df['financial_concerns']

    fig, axs = plt.subplots(2, 2, figsize=(10, 8), tight_layout=True)
    
    ivs = [age, press, money]
    colors = ['b', 'r', 'g']
    labels = ['Age', 'Academic Pressure', 'Financial Concerns']
    
    for ax, x, c, lbl in zip(axs.ravel()[:3], ivs, colors, labels):
        ax.scatter(x, y, alpha=0.5, color=c)
        plot_regression_line(ax, x, y, color='k', ls='-', lw=2)
        
        r_val = corrcoeff(x, y)
        ax.text(0.05, 0.9, f'r = {r_val:.3f}', color=c, transform=ax.transAxes, bbox=dict(color='0.9'))
        ax.set_xlabel(lbl)
        ax.set_ylabel('Depression')

    ax = axs[1, 1]
    i_low = y <= 3
    i_high = y > 3
    
    for i, c, lbl in zip([i_low, i_high], ['m', 'c'], ['Low Dep.', 'High Dep.']):
        if len(money[i]) > 0:
            ax.scatter(money[i], y[i], alpha=0.5, color=c, label=lbl)
            plot_regression_line(ax, money[i], y[i], color=c, ls='-', lw=2)

    ax.legend(fontsize='small')
    ax.set_xlabel('Financial Concerns')
    
    for ax, s in zip(axs.ravel(), ['a', 'b', 'c', 'd']):
        ax.text(0.02, 0.95, f'({s})', transform=ax.transAxes, fontweight='bold')

    plt.show()
    display_title('Correlations amongst main variables.', pref='Figure', num=1)