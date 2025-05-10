# import joblib, sklearn.metrics, pandas, matplotlib.pyplot, os
# load X_test_pca, y_test, and each model from 'outputs'
# for each model:
#     y_pred = model.predict(X_test_pca)
#     report = classification_report(y_test, y_pred, output_dict=True)
#     pd.DataFrame(report).T.to_csv(f'outputs/06_{name}_report.csv')
#     cm = confusion_matrix(y_test, y_pred)
#     plt.imshow(cm, cmap='Blues'); plt.colorbar(); plt.savefig(f'outputs/06_{name}_confusion.png'); plt.clf()
