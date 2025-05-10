import os
import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split

def main():
    os.makedirs('outputs', exist_ok=True)
    df = pd.read_csv('data/Greenhouse Plant Growth Metrics.csv')
    X = df.drop('Class', axis=1)
    y = df['Class']
    categorical_cols = ['Random']
    numerical_cols = [c for c in X.columns if c not in categorical_cols]
    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(sparse=False, handle_unknown='ignore')
    preprocessor = ColumnTransformer([
        ('num', numeric_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])
    X_processed = preprocessor.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(
        X_processed, y, test_size=0.2, stratify=y, random_state=42
    )
    joblib.dump(preprocessor, 'outputs/preprocessor.joblib')
    joblib.dump((X_train, X_test, y_train, y_test), 'outputs/train_test_split.joblib')

if __name__ == "__main__":
    main()