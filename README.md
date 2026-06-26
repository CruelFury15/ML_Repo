# Machine Learning Projects Collection

A hands-on collection of ML projects, Jupyter notebooks, and datasets covering supervised and unsupervised learning, neural networks, dimensionality reduction, feature selection, ensemble methods, and exploratory data analysis. This repository is maintained as a learning archive and growing portfolio.

---

## Table of Contents

- [Repository Structure](#repository-structure)
- [Projects](#projects)
  - [Algorithms](#algorithms)
    - [Linear Regression](#linear-regression)
    - [Logistic Regression](#logistic-regression)
    - [K-Nearest Neighbours](#k-nearest-neighbours)
    - [K-Means Clustering](#k-means-clustering)
    - [Decision Trees](#decision-trees)
    - [Naive Bayes Classifier](#naive-bayes-classifier)
    - [Support Vector Machines (SVM)](#support-vector-machines-svm)
  - [Additional Topics](#additional-topics)
    - [Ensembling Methods](#ensembling-methods)
    - [Hyperparameter Tuning](#hyperparameter-tuning)
    - [Principal Component Analysis (PCA)](#principal-component-analysis-pca)
    - [Perceptron](#perceptron)
    - [Regularisation](#regularisation)
    - [Wrapper Methods (Feature Selection)](#wrapper-methods-feature-selection)
    - [Handwriting Recognition](#handwriting-recognition)
    - [Recommender System](#recommender-system)
    - [Exploratory Data Analysis — GDP & Life Expectancy](#exploratory-data-analysis--gdp--life-expectancy)
    - [Pipeline](#pipeline)
    - [Neural Networks](#neural-networks)
    - [Classification with TensorFlow](#classification-with-tensorflow)
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [Notes](#notes)
- [License](#license)

---

## Repository Structure

```
ML_Repo/
├── Algorithms/
│   ├── DecisionTrees/
│   │   ├── Find_the_flag/
│   │   │   └── flag.ipynb
│   │   └── decision.ipynb
│   ├── K-Means Clustering/
│   │   ├── kmeans_manual.ipynb
│   │   └── kmeans_scikit.ipynb
│   ├── K-NearestNeighbour/
│   │   ├── Cancer_Classifier/
│   │   │   └── classifier.ipynb
│   │   ├── movies.py
│   │   ├── movies.ipynb
│   │   ├── movies_classifier.ipynb
│   │   └── movies_regressor.ipynb
│   ├── LinearRegression/
│   │   ├── AgevBP/
│   │   │   └── BPvAge.ipynb
│   │   ├── HeartDisesase/
│   │   │   └── HeartAttack_Model.ipynb
│   │   ├── HoneyProduction/
│   │   │   ├── honey.ipynb
│   │   │   └── honeyproduction.csv
│   │   ├── StreetEasy_MLR/
│   │   │   ├── streeteasy.ipynb
│   │   │   └── streeteasy.csv
│   │   ├── TennisAce_MLR/
│   │   │   ├── TennisAce.ipynb
│   │   │   └── tennis_stats.csv
│   │   ├── Linear_linregress.ipynb
│   │   ├── Linear_manula.ipynb
│   │   └── Linear_scikit.ipynb
│   ├── LogisticRegression/
│   │   ├── census+income/
│   │   │   ├── adult.data
│   │   │   ├── adult.names
│   │   │   ├── adult.test
│   │   │   └── census.ipynb
│   │   ├── CreditCardFraud/
│   │   │   ├── detection.ipynb
│   │   │   └── transactions_modified.csv
│   │   ├── Logistic_Regression_1/
│   │   │   ├── codecademyU.csv
│   │   │   ├── codecademyU_2.csv
│   │   │   └── logistic_scikit.ipynb
│   │   └── Logistic_Regression_2/
│   │       ├── breast_cancer_data.csv
│   │       └── data.ipynb
│   ├── Naive Bayes Classifier/
│   │   ├── bayes.ipynb
│   │   └── Email Similarity/
│   │       └── email.ipynb
│   └── SVM/
│       ├── graph.py
│   │       ├── svm.ipynb
│   │       └── svm_scikit.ipynb
├── Classification_Tensorflow/
│   ├── heart.ipynb
│   └── heart_failure.csv
├── EDA_GDP/
│   ├── all_data.csv
│   └── life_expectancy_gdp.ipynb
├── Ensembling Methods/
│   ├── boosting.ipynb
│   ├── ensemble_rforest.ipynb
│   ├── rforest_scikit.ipynb
│   ├── Boosting/
│   │   └── census.ipynb
│   └── Random_forest_Project/
│       ├── adult.data
│       └── adult.ipynb
├── Handwriting Recognition/
│   ├── index.html
│   ├── JsCode.js
│   ├── requirements.txt
│   ├── script.py
│   ├── test.html
│   └── outputs/
├── HyperParameter Tuning/
│   ├── tuning.ipynb
│   └── Raisins_Classify/
│       ├── Raisin_Dataset.csv
│       └── notebook.ipynb
├── Neural Networks/
│   ├── neural.ipynb
│   └── Life_Expectancy/
│       ├── life_expectancy.csv
│       └── life.ipynb
├── PCA/
│   ├── pca.ipynb
│   └── Telescope/
│       ├── classes.csv
│       ├── data_matrix.csv
│       ├── telescope_data.csv
│       ├── telescope1.ipynb
│       └── telescope2.ipynb
├── Perceptron/
│   ├── gates.ipynb
│   └── perceptron.ipynb
├── Pipeline/
│   ├── bone_marrow.ipynb
│   └── bone-marrow.arff
├── Recommender System/
│   ├── goodreads_ratings.csv
│   └── recommender.ipynb
├── Regularisation/
│   ├── regularisation.ipynb
│   └── students_maths.csv
└── WrapperMethod/
    ├── dataR2.csv
    ├── wrapper.ipynb
    └── eating_habit/
        ├── obesity.csv
        ├── wrapper_method_solution.ipynb
        └── wrapper_methods_project_v2/
```

---

## Projects

### Algorithms

#### Linear Regression

| Project | Description |
|---|---|
| `Algorithms/LinearRegression/Linear_linregress.ipynb` | Simple linear regression using `scipy.stats.linregress` — covers slope, intercept, R², and t-statistics |
| `Algorithms/LinearRegression/Linear_manula.ipynb` | Manual gradient descent explanation and implementation from first principles |
| `Algorithms/LinearRegression/Linear_scikit.ipynb` | Scikit-learn `LinearRegression` on a toy dataset |
| `Algorithms/LinearRegression/AgevBP/BPvAge.ipynb` | Predicts blood pressure from age using synthetic data |
| `Algorithms/LinearRegression/HoneyProduction/honey.ipynb` | Forecasts US honey production trends with time series aggregation |
| `Algorithms/LinearRegression/HeartDisesase/HeartAttack_Model.ipynb` | Heart disease risk modelling with EDA and classifier comparison |
| `Algorithms/LinearRegression/StreetEasy_MLR/streeteasy.ipynb` | Multiple linear regression on NYC rental listings |
| `Algorithms/LinearRegression/TennisAce_MLR/TennisAce.ipynb` | Tennis performance regression and model comparison |

#### Logistic Regression

| Project | Description |
|---|---|
| `Algorithms/LogisticRegression/Logistic_Regression_1/logistic_scikit.ipynb` | Logistic regression examples, scaling, and classification metrics |
| `Algorithms/LogisticRegression/Logistic_Regression_2/data.ipynb` | Breast cancer malignancy classification and ROC analysis |
| `Algorithms/LogisticRegression/census+income/census.ipynb` | UCI Adult dataset income prediction with feature engineering |
| `Algorithms/LogisticRegression/CreditCardFraud/detection.ipynb` | Fraud classification on transaction data |

#### K-Nearest Neighbours

| Project | Description |
|---|---|
| `K-NearestNeighbour/movies_manual.ipynb` | KNN from scratch with distance functions and validation accuracy |
| `Algorithms/K-NearestNeighbour/movies.ipynb` | Movie dataset KNN examples and helper dataset utilities |
| `Algorithms/K-NearestNeighbour/movies_classifier.ipynb` | KNN classification of movie audience score |
| `Algorithms/K-NearestNeighbour/movies_regressor.ipynb` | KNN regression for continuous movie rating prediction |
| `Algorithms/K-NearestNeighbour/Cancer_Classifier/classifier.ipynb` | Breast cancer KNN classification and k-tuning analysis |

#### K-Means Clustering

| Project | Description |
|---|---|
| `Algorithms/K-Means Clustering/kmeans_manual.ipynb` | K-Means clustering implemented from scratch |
| `Algorithms/K-Means Clustering/kmeans_scikit.ipynb` | Scikit-learn KMeans clustering and elbow-method analysis |

#### Decision Trees

| Project | Description |
|---|---|
| `Algorithms/DecisionTrees/decision.ipynb` | Decision tree classifier on a categorical dataset |
| `Algorithms/DecisionTrees/Find_the_flag/flag.ipynb` | Flag classification with tree pruning and visualisation |

#### Naive Bayes Classifier

| Project | Description |
|---|---|
| `Algorithms/Naive Bayes Classifier/bayes.ipynb` | Naive Bayes classification concepts and examples |
| `Algorithms/Naive Bayes Classifier/Email Similarity/email.ipynb` | Email similarity classification using naive Bayes techniques |

#### Support Vector Machines (SVM)

| Project | Description |
|---|---|
| `Algorithms/SVM/svm.ipynb` | SVM fundamentals and margin visualisation |
| `Algorithms/SVM/svm_scikit.ipynb` | Scikit-learn SVC examples with linear, polynomial, and RBF kernels |

### Additional Topics

#### Ensembling Methods

| Project | Description |
|---|---|
| `Ensembling Methods/boosting.ipynb` | Boosting and ensemble learning concepts |
| `Ensembling Methods/ensemble_rforest.ipynb` | Random forest ensemble exploration |
| `Ensembling Methods/rforest_scikit.ipynb` | Scikit-learn random forest examples |
| `Ensembling Methods/Random_forest_Project/adult.ipynb` | Adult income classification with Random Forest |
| `Ensembling Methods/Boosting/census.ipynb` | Boosting applied to the UCI Adult census dataset for income classification |

#### Hyperparameter Tuning

| Project | Description |
|---|---|
| `HyperParameter Tuning/tuning.ipynb` | Grid search, random search, and cross-validation techniques |
| `HyperParameter Tuning/Raisins_Classify/notebook.ipynb` | Raisin variety classification with hyperparameter optimisation |

#### Principal Component Analysis (PCA)

| Project | Description |
|---|---|
| `PCA/pca.ipynb` | PCA theory and sample data dimensionality reduction |
| `PCA/Telescope/telescope1.ipynb` | PCA on telescope sensor data |
| `PCA/Telescope/telescope2.ipynb` | Classifier evaluation on PCA-reduced telescope features |

#### Perceptron

| Project | Description |
|---|---|
| `Perceptron/gates.ipynb` | Logic gate implementation with perceptron models |
| `Perceptron/perceptron.ipynb` | Perceptron learning and decision boundary examples |

#### Regularisation

| Project | Description |
|---|---|
| `Regularisation/regularisation.ipynb` | L1 and L2 regularisation demonstration on student maths data |

#### Wrapper Methods (Feature Selection)

| Project | Description |
|---|---|
| `WrapperMethod/wrapper.ipynb` | Wrapper-based feature selection introduction |
| `WrapperMethod/eating_habit/wrapper_method_solution.ipynb` | Feature selection on eating habits and obesity data |

#### Handwriting Recognition

An end-to-end digit recognition project combining Python and a browser drawing interface.

- `Handwriting Recognition/script.py`
- `Handwriting Recognition/index.html`
- `Handwriting Recognition/JsCode.js`
- `Handwriting Recognition/requirements.txt`
- `Handwriting Recognition/test.html`
- `Handwriting Recognition/outputs/`

#### Recommender System

| Project | Description |
|---|---|
| `Recommender System/recommender.ipynb` | Goodreads rating-based recommender system notebook |

#### Exploratory Data Analysis — GDP & Life Expectancy

| Project | Description |
|---|---|
| `EDA_GDP/life_expectancy_gdp.ipynb` | GDP and life expectancy exploratory data analysis |

#### Pipeline

| Project | Description |
|---|---|
| `Pipeline/bone_marrow.ipynb` | End-to-end scikit-learn Pipeline for bone marrow transplant outcome prediction using `.arff` data — covers preprocessing, encoding, and model evaluation in a single pipeline |

#### Neural Networks

| Project | Description |
|---|---|
| `Neural Networks/neural.ipynb` | Neural network fundamentals — architecture, forward pass, activation functions, and training concepts |
| `Neural Networks/Life_Expectancy/life.ipynb` | Neural network regression on life expectancy data — feature preprocessing, model training, and evaluation |

#### Classification with TensorFlow

| Project | Description |
|---|---|
| `Classification_Tensorflow/heart.ipynb` | Binary classification of heart failure outcomes using TensorFlow/Keras — covers data preprocessing, model building, training, and evaluation on clinical data |

---

## Getting Started

1. Install Python 3.10 or newer.
2. Create and activate a virtual environment.
3. Install dependencies for notebook work using `pip install -r "Handwriting Recognition/requirements.txt"` or install packages used by your selected notebook(s).
4. Launch Jupyter Notebook or JupyterLab from the repository root.

## Dependencies

- Python 3.10+
- Jupyter Notebook / JupyterLab
- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn
- scipy

> Some notebooks may require additional packages; inspect notebook metadata or individual imports.

## Notes

- This repository is intended primarily as an educational collection. Code notebooks demonstrate algorithms, dataset exploration, and model evaluation.
- Folder names and notebook names are preserved from the original project structure.
- Some datasets are stored alongside notebooks to support local execution.

## License

No license is specified for this repository at this time.
