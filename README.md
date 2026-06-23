# Machine Learning Projects Collection

A hands-on collection of ML projects, Jupyter notebooks, and datasets covering supervised and unsupervised learning algorithms, dimensionality reduction, feature selection, and exploratory data analysis. Built as a learning archive and growing portfolio.

---

## Table of Contents

- [Repository Structure](#repository-structure)
- [Projects](#projects)
  - [Linear Regression](#linear-regression)
  - [Logistic Regression](#logistic-regression)
  - [K-Nearest Neighbours](#k-nearest-neighbours)
  - [K-Means Clustering](#k-means-clustering)
  - [Decision Trees](#decision-trees)
  - [Hyperparameter Tuning](#hyperparameter-tuning)
  - [Principal Component Analysis (PCA)](#principal-component-analysis-pca)
  - [Regularisation](#regularisation)
  - [Wrapper Methods (Feature Selection)](#wrapper-methods-feature-selection)
  - [Handwriting Recognition](#handwriting-recognition)
  - [Exploratory Data Analysis — GDP & Life Expectancy](#exploratory-data-analysis--gdp--life-expectancy)
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [Notes](#notes)
- [License](#license)

---

## Repository Structure

```
ML_Repo/
├── Algorithms/                        # Core algorithm implementations (notebooks + datasets)
│   ├── LinearRegression/
│   │   ├── AgevBP/
│   │   ├── HeartDisesase/
│   │   ├── HoneyProduction/
│   │   ├── StreetEasy_MLR/
│   │   ├── TennisAce_MLR/
│   │   ├── Linear_linregress.ipynb
│   │   ├── Linear_manula.ipynb
│   │   └── Linear_scikit.ipynb
│   ├── LogisticRegression/
│   │   ├── census+income/
│   │   ├── CreditCardFraud/
│   │   ├── Logistic_Regression_1/
│   │   └── Logistic_Regression_2/
│   ├── K-NearestNeighbour/
│   │   ├── Cancer_Classifier/
│   │   ├── movies.py
│   │   ├── movies.ipynb
│   │   ├── movies_classifier.ipynb
│   │   └── movies_regressor.ipynb
│   ├── K-Means Clustering/
│   │   ├── kmeans_manual.ipynb
│   │   └── kmeans_scikit.ipynb
│   └── DecisionTrees/
│       ├── Find_the_flag/
│       │   └── flag.ipynb
│       └── decision.ipynb                
├── EDA_GDP/                           # Exploratory Data Analysis project
│   ├── all_data.csv
│   └── life_expectancy_gdp.ipynb
├── Handwriting Recognition/           # End-to-end digit recognition app (Python + Web UI)
│   ├── script.py
│   ├── index.html
│   ├── JsCode.js
│   └── outputs/
├── HyperParameter Tuning/
│   ├── tuning.ipynb
│   └── Raisins_Classify/
│       └── notebook.ipynb
├── PCA/
│   ├── pca.ipynb
│   └── Telescope/
│       ├── telescope1.ipynb
│       └── telescope2.ipynb
├── Regularisation/
│   └── regularisation.ipynb
└── WrapperMethod/
    ├── wrapper.ipynb
    └── eating_habit/
        └── wrapper_method_solution.ipynb
```

---

## Projects

### Linear Regression

| Project | Description |
|---|---|
| `Linear_linregress.ipynb` | Simple linear regression using `scipy.stats.linregress` — covers slope, intercept, R², and t-statistics |
| `Linear_manula.ipynb` | Manual gradient descent — builds `step_gradient` and `gradient_descent` from first principles |
| `Linear_scikit.ipynb` | Scikit-learn `LinearRegression` on a temperature vs. ice cream sales toy dataset |
| `AgevBP/BPvAge.ipynb` | Predicts blood pressure from age using simulated data (n=200); includes hypothesis testing and user input prediction |
| `HoneyProduction/honey.ipynb` | Forecasts US honey production trends; aggregates yearly totals and projects 40 years into the future |
| `HeartDisesase/HeartAttack_Model.ipynb` | Cleveland heart disease dataset — EDA, feature correlation, Logistic Regression and Random Forest comparison, ROC-AUC evaluation, and risk prediction for new patients |
| `StreetEasy_MLR/streeteasy.ipynb` | Multiple linear regression on NYC rental listings (StreetEasy data) to predict rent |
| `TennisAce_MLR/TennisAce.ipynb` | Multiple linear regression on ATP tennis stats; explores single and two-feature models predicting winnings and wins |

---

### Logistic Regression

| Project | Description |
|---|---|
| `Logistic_Regression_1/logistic_scikit.ipynb` | Intro to logistic regression — models exam pass probability from study hours; extends to a multi-feature student dataset with scaling, accuracy, precision, and recall |
| `Logistic_Regression_2/data.ipynb` | Breast cancer malignancy classification (Wisconsin dataset); includes outlier removal, train/test split, threshold tuning, and ROC curve analysis |
| `census+income/census.ipynb` | Predicts whether income exceeds \$50K using UCI Adult Census data; features L1-regularised logistic regression, one-hot encoding, feature scaling, confusion matrix, and AUC scoring |
| `CreditCardFraud/detection.ipynb` | Fraud detection on transaction data; engineers features (payment type, account difference), fits logistic regression, and classifies new transactions |

---

### K-Nearest Neighbours

| Project | Description |
|---|---|
| `movies.py` | Shared data module — provides `movie_dataset`, `movie_labels`, `movie_ratings`, and `normalize_point` |
| `movies.ipynb` | KNN classification from scratch — implements Euclidean distance, a `classify` function, and `find_validation_accuracy`; also demonstrates `KNeighborsClassifier` |
| `movies_classifier.ipynb` | KNN movie classifier — predicts whether a movie has a high audience score; includes validation accuracy sweep over multiple k values |
| `movies_regressor.ipynb` | KNN movie regressor — predicts a continuous audience rating using weighted KNN |
| `Cancer_Classifier/classifier.ipynb` | KNN breast cancer classifier using sklearn's built-in dataset; sweeps k from 1–100, plots accuracy vs. k, and identifies the optimal k |

---

### K-Means Clustering

| Project | Description |
|---|---|
| `kmeans_manual.ipynb` | K-Means clustering implemented from scratch — covers centroid initialisation, assignment, and update steps |
| `kmeans_scikit.ipynb` | K-Means using scikit-learn `KMeans`; explores cluster count selection and inertia/elbow method |

---

### Decision Trees

| Project | Description |
|---|---|
| `decision.ipynb` | Decision tree classifier on the UCI Car Evaluation dataset; one-hot encodes categorical features, visualises the fitted tree, and manually computes Gini impurity and Information Gain per feature |
| `Find_the_flag/flag.ipynb` | Classifies country flags (Europe vs. Oceania) using the UCI Flags dataset; tunes `max_depth` and `ccp_alpha` (cost-complexity pruning) with accuracy plots, and visualises the final pruned tree |

---

### Hyperparameter Tuning

| Project | Description |
|---|---|
| `tuning.ipynb` | Intro to hyperparameter tuning concepts — grid search, random search, and cross-validation strategies |
| `Raisins_Classify/notebook.ipynb` | Raisin variety classification (Besni vs. Kecimen) using the Raisin Dataset; applies GridSearchCV and RandomizedSearchCV to optimise classifier performance |

---

### Principal Component Analysis (PCA)

| Project | Description |
|---|---|
| `pca.ipynb` | Core PCA concepts — variance explained, scree plots, and dimensionality reduction on sample data |
| `Telescope/telescope1.ipynb` | PCA applied to the MAGIC Gamma Telescope dataset; reduces high-dimensional sensor features and visualises principal components |
| `Telescope/telescope2.ipynb` | Extends telescope1 — rebuilds a classifier on PCA-reduced features and compares accuracy against the full feature set |

---

### Regularisation

| Project | Description |
|---|---|
| `regularisation.ipynb` | Demonstrates L1 (Lasso) and L2 (Ridge) regularisation on a student maths score dataset; compares coefficients and prediction error across regularisation strengths |

---

### Wrapper Methods (Feature Selection)

| Project | Description |
|---|---|
| `wrapper.ipynb` | Introduction to wrapper-based feature selection — Sequential Feature Selector (SFS) forward and backward variants |
| `eating_habit/wrapper_method_solution.ipynb` | Feature selection on an obesity/eating habits dataset; uses SFS to identify the most predictive features for BMI classification |

---

### Handwriting Recognition

An end-to-end digit recognition project combining a Python ML backend with a browser-based drawing interface.

| File | Description |
|---|---|
| `script.py` | Trains a K-Means clustering model on sklearn's digits dataset; generates output visualisations (`digits_overview.png`, `sample_digit.png`, `cluster_centers.png`) |
| `index.html` + `JsCode.js` | Web UI — canvas drawing pad that sends user-drawn digits to the model for classification |
| `test.html` | Standalone test page for the drawing interface |
| `outputs/` | Pre-generated visualisation outputs from the trained model |

---

### Exploratory Data Analysis — GDP & Life Expectancy

| Project | Description |
|---|---|
| `EDA_GDP/life_expectancy_gdp.ipynb` | EDA on GDP and life expectancy data across multiple countries and years; includes data cleaning, visualisation, and trend analysis |

---

## Getting Started

**Prerequisites:** Python 3.8+

```powershell
# Create and activate a virtual environment
python -m venv venv
venv\Scripts\Activate.ps1

# Install dependencies
pip install numpy pandas matplotlib scikit-learn scipy seaborn jupyter
```

**Launch notebooks:**

```powershell
jupyter lab
```

Open any `.ipynb` file from the Jupyter UI. Notebooks that depend on CSV files expect the data file to be in the same directory as the notebook. Notebooks that load data from UCI URLs require an internet connection.

---

## Dependencies

| Package | Used for |
|---|---|
| `numpy` | Array operations, numerical computing |
| `pandas` | Data loading and manipulation |
| `matplotlib` / `seaborn` | Visualisation |
| `scikit-learn` | Model training, evaluation, preprocessing |
| `scipy` | Statistical tests (`linregress`, `ttest_1samp`, `binomtest`) |
| `jupyter` | Running notebooks |

---

## Notes

- Large CSV files (e.g., `transactions_modified.csv`, `adult.data`) are stored locally alongside notebooks. Add them to `.gitignore` or use Git LFS if they exceed GitHub's 100 MB file size limit.
- `HeartAttack_Model.ipynb` uses both Logistic Regression and Random Forest — it lives under `LinearRegression/` for historical reasons but covers classification.
- The `Algorithms/` folder mirrors some standalone folders (e.g., `K-NearestNeighbour/`) — both are kept for compatibility with older notebook paths.
- New algorithm categories (neural networks, ensemble methods, etc.) can be added as top-level folders following the same pattern.

---

## License

Add a `LICENSE` file before publishing publicly. MIT or Apache-2.0 is recommended for open learning portfolios.
