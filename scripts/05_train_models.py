# import joblib, os
# import sklearn.model_selection GridSearchCV
# import classifiers (RandomForestClassifier, LogisticRegression)
# load X_train_pca, y_train from 'outputs/engineered_data.joblib'
# define param_grids for each model
# for name, model, grid in models:
#     gs = GridSearchCV(model, grid, cv=5); gs.fit(X_train_pca, y_train)
#     joblib.dump(gs.best_estimator_, f'outputs/05_{name}_model.joblib')
#     pd.DataFrame(gs.cv_results_).to_csv(f'outputs/05_{name}_cv_results.csv', index=False)
