# data-science-greenhouse-plant-growth

**Project Overview**

This project analyzes plant growth metrics from two greenhouse settings (IoT-enabled vs. traditional) using advanced data science and modeling techniques. It includes data ingestion, preprocessing, exploratory analysis, feature engineering, model training, evaluation, visualization, and prediction workflows to classify experimental groups based on physiological and morphological measurements.

---

**Folder Structure**

```
project-root/
├── data/
│   └── Greenhouse Plant Growth Metrics.csv   # Raw dataset
├── outputs/                                 # Generated results: CSV summaries, plots, models
├── scripts/                                 # Analysis and modeling scripts
│   ├── 01_data_ingestion.py
│   ├── 02_data_preprocessing.py
│   ├── 03_eda.py
│   ├── 04_feature_engineering.py
│   ├── 05_train_models.py
│   ├── 06_evaluate.py
│   ├── 07_visualize.py
│   └── 08_predict.py
├── requirements.txt                         # Python dependencies
└── README.md                                # Project documentation
```

---

**Usage**

1. **Setup the Project**:

   * Clone the repository.
   * Ensure you have Python installed.
   * Install required dependencies using the requirements.txt file.

     ```bash
     pip install -r requirements.txt
     ```

2. **Run Data Ingestion**:

   ```bash
   python scripts/01_data_ingestion.py
   ```

3. **Preprocess Data**:

   ```bash
   python scripts/02_data_preprocessing.py
   ```

4. **Exploratory Data Analysis (EDA)**:

   ```bash
   python scripts/03_eda.py
   ```

5. **Feature Engineering & PCA**:

   ```bash
   python scripts/04_feature_engineering.py
   ```

6. **Train Models**:

   ```bash
   python scripts/05_train_models.py
   ```

7. **Evaluate Models**:

   ```bash
   python scripts/06_evaluate.py
   ```

8. **Visualize Results**:

   ```bash
   python scripts/07_visualize.py
   ```

9. **Make Predictions on New Data**:

   ```bash
   python scripts/08_predict.py --input data/new_samples.csv --output outputs/predictions.csv
   ```

---

