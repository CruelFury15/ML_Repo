# Machine Learning & Web Development Projects

A hands-on collection of ML and web projects, Jupyter notebooks, and datasets covering supervised and unsupervised learning, neural networks, CNNs, dimensionality reduction, feature selection, ensemble methods, exploratory data analysis, and Flask web development.

> 📚 **Learning Credit:** The majority of projects and exercises in this repository are based on courses and guided projects from [Codecademy](https://www.codecademy.com). All credit for curriculum design, datasets, and project structure goes to Codecademy. This repository serves as a personal learning archive and portfolio built while completing their Data Science, Machine Learning, and Web Development paths.

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
    - [Convolutional Neural Networks (CNN)](#convolutional-neural-networks-cnn)
    - [Flask Web Applications](#flask-web-applications)
      - [To-Do App](#to-do-app)
      - [TriPlanned (Travel Site)](#triplanned-travel-site)
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
│       ├── svm.ipynb
│       └── svm_scikit.ipynb
├── CNN/
│   ├── galaxy.ipynb
│   ├── app.py
│   └── visualize.py
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
├── Flask/
│   ├── first_flask_app.py
│   ├── Flask-SQLAlchemy/
│   │   ├── app.py
│   │   ├── create_object.py
│   │   └── README.md
│   ├── pet-shop/
│   │   ├── app.py
│   │   └── helper.py
│   ├── tourist-attractions-app/
│   │   ├── app.py
│   │   ├── forms.py
│   │   ├── locations.py
│   │   ├── data.csv
│   │   └── templates/
│   │       ├── base.html
│   │       └── locations.html
│   ├── To-Do_App/
│   │   ├── app.py
│   │   ├── create_todos.py
│   │   └── templates/
│   └── Travel_Site/
│       ├── app.py
│       ├── extensions.py
│       ├── models.py
│       ├── routes.py
│       ├── forms.py
│       ├── README.md
│       └── templates/
│           ├── base.html
│           ├── landing_page.html
│           ├── login.html
│           ├── register.html
│           └── user.html
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
| `Algorithms/LinearRegression/Linear_manula.ipynb` | Manual gradient descent implementation from first principles |
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
| `Algorithms/Naive Bayes Classifier/Email Similarity/email.ipynb` | Email similarity classification using Naive Bayes |

#### Support Vector Machines (SVM)

| Project | Description |
|---|---|
| `Algorithms/SVM/svm.ipynb` | SVM fundamentals and margin visualisation |
| `Algorithms/SVM/svm_scikit.ipynb` | Scikit-learn SVC with linear, polynomial, and RBF kernels |

---

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

An end-to-end digit recognition project combining a Python ML backend with a browser-based drawing interface.

| File | Description |
|---|---|
| `Handwriting Recognition/script.py` | Core ML script — trains a digit classifier and serves predictions |
| `Handwriting Recognition/index.html` | Browser canvas UI for drawing digits |
| `Handwriting Recognition/JsCode.js` | JavaScript — captures canvas input and calls the backend |
| `Handwriting Recognition/test.html` | Test page for the drawing interface |
| `Handwriting Recognition/outputs/` | Saved visualisation images (cluster centres, digit overview, sample) |

#### Recommender System

| Project | Description |
|---|---|
| `Recommender System/recommender.ipynb` | Goodreads rating-based book recommender system |

#### Exploratory Data Analysis — GDP & Life Expectancy

| Project | Description |
|---|---|
| `EDA_GDP/life_expectancy_gdp.ipynb` | EDA on GDP and life expectancy across countries — visualisation and trend analysis |

#### Pipeline

| Project | Description |
|---|---|
| `Pipeline/bone_marrow.ipynb` | End-to-end scikit-learn Pipeline for bone marrow transplant outcome prediction — preprocessing, encoding, and model evaluation in a single pipeline |

#### Neural Networks

| Project | Description |
|---|---|
| `Neural Networks/neural.ipynb` | Neural network fundamentals — architecture, forward pass, activation functions, and training |
| `Neural Networks/Life_Expectancy/life.ipynb` | Neural network regression on life expectancy data — feature preprocessing, training, and evaluation |

#### Classification with TensorFlow

| Project | Description |
|---|---|
| `Classification_Tensorflow/heart.ipynb` | Binary classification of heart failure outcomes using TensorFlow/Keras — preprocessing, model building, training, and evaluation on clinical data |

#### Convolutional Neural Networks (CNN)

| Project | Description |
|---|---|
| `CNN/galaxy.ipynb` | CNN-based galaxy morphology classification — image preprocessing, convolutional architecture design, training, and feature visualisation |
| `CNN/visualize.py` | Helper script for visualising CNN layer activations and feature maps |
| `CNN/app.py` | Application script for running CNN inference |

#### Flask Web Applications

| Project | Description |
|---|---|
| `Flask/first_flask_app.py` | Introductory Flask app — routing, templates, and request handling basics |
| `Flask/pet-shop/app.py` | Pet shop Flask app with helper utilities |
| `Flask/tourist-attractions-app/app.py` | Tourist attractions CRUD app with form handling, data model, and Jinja2 templates |
| `Flask/Flask-SQLAlchemy/app.py` | Flask + SQLAlchemy demo — defines `Book`, `Reader`, `Review` models and persists data to SQLite |
| `Flask/Flask-SQLAlchemy/create_object.py` | Script to insert sample data into the SQLite database |
| `Flask/To-Do_App/app.py` | To-do list app with Flask-WTF form, SQLAlchemy-backed `Todo` model, and persistent task storage |
| `Flask/Travel_Site/` | **TriPlanned** — full-featured travel planning app with user registration, login, session management, and per-user trip posts. See [`Flask/Travel_Site/README.md`](Flask/Travel_Site/README.md) for setup and details |

---

## Getting Started

1. Install Python 3.10 or newer.
2. Create and activate a virtual environment.
3. Install dependencies for notebook work:
   ```bash
   pip install jupyter scikit-learn pandas numpy matplotlib seaborn scipy tensorflow flask flask_sqlalchemy
   ```
   Or for the Handwriting Recognition project specifically:
   ```bash
   pip install -r "Handwriting Recognition/requirements.txt"
   ```
4. Launch Jupyter Notebook or JupyterLab from the repository root:
   ```bash
   jupyter lab
   ```

---

## Dependencies

| Package | Used in |
|---|---|
| `scikit-learn` | Most ML algorithm notebooks |
| `pandas` | Data loading and manipulation throughout |
| `numpy` | Numerical computation throughout |
| `matplotlib` | Visualisation throughout |
| `seaborn` | Statistical visualisation |
| `scipy` | Linear regression, statistics |
| `tensorflow` / `keras` | Neural Networks, Classification, CNN |
| `flask` | All Flask web app projects |
| `flask_sqlalchemy` | Flask-SQLAlchemy project, To-Do App, Travel Site |
| `flask-login` | Travel Site — session and authentication management |
| `flask-wtf` / `wtforms` | Travel Site, To-Do App — form handling and validation |
| `email-validator` | Travel Site — email field validation |
| `jupyter` | All `.ipynb` notebooks |

> Some notebooks may require additional packages. Check individual notebook imports or the folder's `requirements.txt` if present.

---

## Notes

- Projects are primarily based on [Codecademy](https://www.codecademy.com) courses — see the learning credit note at the top.
- Folder and notebook names are preserved from their original project structure.
- Datasets are stored alongside notebooks to support local execution.
- Virtual environment directories (`Include/`, `Lib/`, `Scripts/`) are excluded from version control via `.gitignore`.

---

## License

No license is specified for this repository at this time. All Codecademy course materials and datasets remain the intellectual property of [Codecademy](https://www.codecademy.com).
