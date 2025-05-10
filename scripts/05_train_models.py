import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

def main():
    os.makedirs('outputs', exist_ok=True)
    X_train, X_test, y_train, y_test = joblib.load('outputs/engineered_data.joblib')
    models = {
        'rf': (RandomForestClassifier(random_state=42), {
            'n_estimators': [100, 200],
            'max_depth': [None, 10]
        }),
        'lr': (LogisticRegression(max_iter=1000), {
            'C': [0.1, 1.0, 10.0]
        })
    }
    for name, (model, params) in models.items():
        gs = GridSearchCV(model, params, cv=5, n_jobs=-1)
        gs.fit(X_train, y_train)
        joblib.dump(gs.best_estimator_, f'outputs/05_{name}_model.joblib')
        pd.DataFrame(gs.cv_results_).to_csv(f'outputs/05_{name}_cv_results.csv', index=False)

if __name__ == "__main__":
    main()