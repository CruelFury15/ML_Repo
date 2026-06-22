# Machine Learning Projects Collection

A hands-on collection of ML projects, Jupyter notebooks, and datasets covering supervised learning algorithms. Built as a learning archive and growing portfolio.

---

## Repository Structure

```
ML_Repo/
├── LinearRegression/
│   ├── AgevBP/
│   ├── HeartDisesase/
│   ├── HoneyProduction/
│   ├── StreetEasy_MLR/
│   ├── TennisAce_MLR/
│   ├── Linear_linregress.ipynb
│   ├── Linear_manula.ipynb
│   └── Linear_scikit.ipynb
├── LogisticRegression/
│   ├── census+income/
│   ├── CreditCardFraud/
│   ├── Logistic_Regression_1/
│   └── Logistic_Regression_2/
├── K-NearestNeighbour/
│   ├── Cancer_Classifier/
│   ├── movies.py
│   ├── movies.ipynb
│   ├── movies_classifier.ipynb
│   └── movies_regressor.ipynb
└── DecisionTrees/
    ├── Find_the_flag/
    │   └── flag.ipynb
    └── decision.ipynb
```

---

## Projects

### Linear Regression

| Project | Description |
|---|---|
| `Linear_linregress.ipynb` | Simple linear regression from scratch using `scipy.stats.linregress` — covers slope, intercept, R², and t-statistics |
| `Linear_manula.ipynb` | Manual gradient descent implementation — builds `step_gradient` and `gradient_descent` functions from first principles |
| `Linear_scikit.ipynb` | Scikit-learn `LinearRegression` on a temperature vs. ice cream sales toy dataset |
| `AgevBP/BPvAge.ipynb` | Predicts blood pressure from age using simulated data (n=200); includes hypothesis testing and user input prediction |
| `HoneyProduction/honey.ipynb` | Forecasts US honey production trends with scikit-learn; aggregates yearly totals and projects 40 years into the future |
| `HeartDisesase/HeartAttack_Model.ipynb` | Cleveland heart disease dataset — EDA, feature correlation, Logistic Regression and Random Forest comparison, ROC-AUC evaluation, and risk prediction for new patients |
| `StreetEasy_MLR/streeteasy.ipynb` | Multiple linear regression on NYC rental listings (StreetEasy data) to predict rent |
| `TennisAce_MLR/TennisAce.ipynb` | Multiple linear regression on ATP tennis stats; explores single and two-feature models predicting winnings and wins |

---

### Logistic Regression

| Project | Description |
|---|---|
| `Logistic_Regression_1/logistic_scikit.ipynb` | Intro to logistic regression with scikit-learn — models exam pass probability from study hours; extends to a multi-feature student dataset with scaling, accuracy, precision, and recall |
| `Logistic_Regression_2/data.ipynb` | Breast cancer malignancy classification (Wisconsin dataset); includes outlier removal, train/test split, threshold tuning, and ROC curve analysis |
| `census+income/census.ipynb` | Predicts whether income exceeds \$50K using UCI Adult Census data; features L1-regularised logistic regression, one-hot encoding, feature scaling, confusion matrix, and AUC scoring |
| `CreditCardFraud/detection.ipynb` | Fraud detection on transaction data; engineers features (payment type, account difference), fits logistic regression, and classifies new transactions |

---

### K-Nearest Neighbours

| Project | Description |
|---|---|
| `movies.py` | Shared data module — provides `movie_dataset` (normalised budget/runtime/audience score features), `movie_labels` (binary high/low audience score), `movie_ratings` (continuous audience score 0–10), and `normalize_point` |
| `movies.ipynb` | KNN classification from scratch — implements Euclidean distance, a `classify` function, and `find_validation_accuracy`; also demonstrates `KNeighborsClassifier` from scikit-learn |
| `movies_classifier.ipynb` | KNN movie classifier — predicts whether a movie has a high audience score; includes validation accuracy sweep over multiple k values |
| `movies_regressor.ipynb` | KNN movie regressor — predicts a continuous audience rating using weighted KNN; imports `movie_ratings` from `movies.py` |
| `Cancer_Classifier/classifier.ipynb` | KNN breast cancer classifier using sklearn's built-in dataset; sweeps k from 1–100, plots accuracy vs. k, and identifies the optimal k |

---

### Decision Trees

| Project | Description |
|---|---|
| `decision.ipynb` | Decision tree classifier on the UCI Car Evaluation dataset; one-hot encodes categorical features, visualises the fitted tree, and manually computes Gini impurity and Information Gain per feature to show how splits are chosen |
| `Find_the_flag/flag.ipynb` | Classifies country flags (Europe vs. Oceania) using the UCI Flags dataset; tunes `max_depth` and `ccp_alpha` (cost-complexity pruning) with accuracy plots, and visualises the final pruned tree |

---

## Getting Started

**Prerequisites:** Python 3.8+

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install numpy pandas matplotlib scikit-learn scipy seaborn jupyter
```

**Launch notebooks:**

```powershell
jupyter lab
```

Open any `.ipynb` file from the Jupyter UI. Notebooks that depend on CSV files expect the data file to be in the same directory as the notebook. Notebooks that load data directly from UCI URLs require an internet connection.

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

- Large CSV files (e.g., `transactions_modified.csv`, `adult.data`) are stored locally alongside notebooks. Add them to `.gitignore` or use Git LFS if they exceed GitHub's file size limits.
- The `HeartAttack_Model.ipynb` notebook uses both Logistic Regression and Random Forest — it lives under `LinearRegression/` for historical reasons but covers classification.
- New algorithm categories (clustering, neural networks, etc.) can be added as top-level folders following the same pattern.

---

## License

Add a `LICENSE` file before publishing publicly (MIT or Apache-2.0 recommended).
