import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

def run_ml_analysis(df):
    X = df[['academic_pressure', 'average_sleep', 'anxiety', 'isolation']]
    y = df['depression']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    score = r2_score(y_test, y_pred)
    importance = pd.Series(model.feature_importances_, index=X.columns).sort_values()
    return (y_test, y_pred, score), importance

def plot_ml_results(val_data, importance):
    y_test, y_pred, r2 = val_data
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Result 1: Fig 3 (Validation)
    ax1.scatter(y_test, y_pred, alpha=0.5, color='teal')
    ax1.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    ax1.set_title(f"Fig. 3: ML Validation (R² = {r2:.2f})")
    
    # Result 2: Fig 4 (Importance)
    importance.plot(kind='barh', ax=ax2, color='coral')
    ax2.set_title("Fig. 4: Primary Drivers of Depression")
    plt.tight_layout()
    plt.show()