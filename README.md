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
  - [Bike Rental Data](#bike-rental-data)
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
│   │   │   ├── BPvAge.ipynb
│   │   │   └── BPvAge.xlsx
│   │   ├── HeartDisesase/
│   │   │   ├── HeartAttack_Model.ipynb
│   │   │   └── Heart_disease_cleveland_new.csv
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
│   │   ├── Email Similarity/
│   │   │   └── email.ipynb
│   │   └── bayes.ipynb
│   └── SVM/
│       ├── graph.py
│       ├── svm.ipynb
│       └── svm_scikit.ipynb
├── CNN/
│   ├── galaxy.ipynb
│   ├── app.py
│   └── visualize.py
├── Classification_Tensorflow/
│   └── HeartFailureClassification/
│       ├── heart.ipynb
│       └── heart_failure.csv
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
│   │       └── index.html
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
├── bike-rental-starter-kit/
│   ├── bike_data.ipynb
│   ├── data/
│   │   ├── combined_bike_data.csv
│   │   ├── JC-201601-citibike-tripdata.csv
│   │   │   ... (one file per month, Jan–Dec 2016)
│   │   ├── JC-201612-citibike-tripdata.csv
│   │   └── newark_airport_2016.csv
│   ├── data-dictionaries/
│   │   ├── citibike.pdf
│   │   └── weather.pdf
│   └── queries/
│       ├── average_distance.sql
│       ├── popular_distance.sql
│       ├── popular_routes.sql
│       ├── ride.sql
│       ├── unique_stations_pairs.sql
│       └── weekly_rides.sql
├── Handwriting Recognition/
│   ├── index.html
│   ├── JsCode.js
│   ├── requirements.txt
│   ├── script.py
│   ├── test.html
│   └── outputs/
│       ├── cluster_centers.png
│       ├── digits_overview.png
│       └── sample_digit.png
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
            └── wrapper_method_projects/
                └── wrapper_method_starter.ipynb
```

---

## Projects

### Algorithms

#### Linear Regression

Linear regression models that learn to predict a continuous output by fitting a line (or hyperplane) to data, using methods ranging from manual gradient descent to Scikit-learn and SciPy.

| Project | Description |
|---|---|
| `LinearRegression/Linear_linregress.ipynb` | Simple linear regression using `scipy.stats.linregress` — slope, intercept, R², and t-statistics |
| `LinearRegression/Linear_manula.ipynb` | Manual implementation of gradient descent for linear regression from first principles |
| `LinearRegression/Linear_scikit.ipynb` | Scikit-learn `LinearRegression` walkthrough on a toy dataset |
| `LinearRegression/AgevBP/BPvAge.ipynb` | Predicts blood pressure from age; data sourced from `BPvAge.xlsx` |
| `LinearRegression/HoneyProduction/honey.ipynb` | Forecasts US honey production trends from historical CSV data using time series aggregation |
| `LinearRegression/HeartDisesase/HeartAttack_Model.ipynb` | Heart disease risk modelling with EDA on the Cleveland heart disease dataset (`Heart_disease_cleveland_new.csv`) |
| `LinearRegression/StreetEasy_MLR/streeteasy.ipynb` | Multiple linear regression on NYC rental listings (`streeteasy.csv`) — feature selection and coefficient interpretation |
| `LinearRegression/TennisAce_MLR/TennisAce.ipynb` | Tennis performance multiple regression using ATP stats (`tennis_stats.csv`) — model comparison and residual analysis |

#### Logistic Regression

Binary and multi-class classifiers built with logistic regression, covering probability thresholds, ROC curves, and feature engineering on real-world datasets.

| Project | Description |
|---|---|
| `LogisticRegression/Logistic_Regression_1/logistic_scikit.ipynb` | Logistic regression fundamentals — feature scaling, sigmoid function, and classification metrics on Codecademy university data |
| `LogisticRegression/Logistic_Regression_2/data.ipynb` | Breast cancer malignancy classification (`breast_cancer_data.csv`) — confusion matrix, accuracy, and ROC/AUC analysis |
| `LogisticRegression/census+income/census.ipynb` | Income prediction (>50K or ≤50K) on the UCI Adult dataset (`adult.data`) — label encoding, feature engineering, and model evaluation |
| `LogisticRegression/CreditCardFraud/detection.ipynb` | Credit card fraud classification on imbalanced transaction data (`transactions_modified.csv`) — threshold tuning and precision/recall trade-offs |

#### K-Nearest Neighbours

KNN applied to both classification and regression tasks, with k-value tuning and performance comparison.

| Project | Description |
|---|---|
| `K-NearestNeighbour/movies.ipynb` | Introduction to KNN on a movie dataset — distance metrics and neighbourhood visualisation |
| `K-NearestNeighbour/movies.py` | Python script version of the movies KNN example |
| `K-NearestNeighbour/movies_classifier.ipynb` | KNN classifier predicting movie audience score categories |
| `K-NearestNeighbour/movies_regressor.ipynb` | KNN regressor for continuous movie rating prediction with k-tuning |
| `K-NearestNeighbour/Cancer_Classifier/classifier.ipynb` | Breast cancer KNN classification — k-value sweep and accuracy optimisation |

#### K-Means Clustering

Unsupervised clustering from a manual implementation to a Scikit-learn solution with elbow-method k selection.

| Project | Description |
|---|---|
| `K-Means Clustering/kmeans_manual.ipynb` | K-Means clustering implemented from scratch — centroid initialisation, assignment, and update steps |
| `K-Means Clustering/kmeans_scikit.ipynb` | Scikit-learn `KMeans` with inertia plots and elbow-method analysis for optimal k |

#### Decision Trees

Tree-based classifiers with pruning, depth tuning, and visualisation.

| Project | Description |
|---|---|
| `DecisionTrees/decision.ipynb` | Decision tree classifier on a categorical dataset — Gini impurity, information gain, and tree depth tuning |
| `DecisionTrees/Find_the_flag/flag.ipynb` | Flag country classification using decision trees — feature importance, tree pruning, and `graphviz` visualisation |

#### Naive Bayes Classifier

Probabilistic classifiers based on Bayes' theorem applied to text and categorical data.

| Project | Description |
|---|---|
| `Naive Bayes Classifier/bayes.ipynb` | Naive Bayes classification fundamentals — prior/posterior probabilities and Laplace smoothing |
| `Naive Bayes Classifier/Email Similarity/email.ipynb` | Email topic classification using `MultinomialNB` — bag-of-words vectorisation and accuracy evaluation |

#### Support Vector Machines (SVM)

Maximum-margin classifiers with multiple kernel types and decision boundary visualisation.

| Project | Description |
|---|---|
| `SVM/svm.ipynb` | SVM theory — support vectors, margin maximisation, and the kernel trick |
| `SVM/svm_scikit.ipynb` | Scikit-learn `SVC` with linear, polynomial, and RBF kernels — hyperparameter tuning with `C` and `gamma` |
| `SVM/graph.py` | Helper script for plotting SVM decision boundaries and margins |

---

### Additional Topics

#### Ensembling Methods

Ensemble techniques that combine multiple learners — random forests, bagging, and gradient boosting — applied to classification tasks.

| Project | Description |
|---|---|
| `Ensembling Methods/boosting.ipynb` | Boosting concepts — AdaBoost and gradient boosting theory with worked examples |
| `Ensembling Methods/ensemble_rforest.ipynb` | Random forest ensemble exploration — bagging, feature randomness, and out-of-bag error |
| `Ensembling Methods/rforest_scikit.ipynb` | Scikit-learn `RandomForestClassifier` walkthrough with feature importance plots |
| `Ensembling Methods/Random_forest_Project/adult.ipynb` | Random Forest applied to the UCI Adult dataset (`adult.data`) for binary income classification |
| `Ensembling Methods/Boosting/census.ipynb` | Gradient boosting on the UCI Adult census dataset — `GradientBoostingClassifier` and `AdaBoostClassifier` comparison |

#### Hyperparameter Tuning

Systematic search strategies for finding optimal model hyperparameters.

| Project | Description |
|---|---|
| `HyperParameter Tuning/tuning.ipynb` | Grid search (`GridSearchCV`), random search (`RandomizedSearchCV`), and cross-validation with scoring metrics |
| `HyperParameter Tuning/Raisins_Classify/notebook.ipynb` | Raisin variety classification (`Raisin_Dataset.csv`) — SVM and decision tree hyperparameter optimisation with `GridSearchCV` |

#### Principal Component Analysis (PCA)

Dimensionality reduction via PCA — explained variance, component selection, and downstream classifier performance.

| Project | Description |
|---|---|
| `PCA/pca.ipynb` | PCA theory — covariance matrix, eigenvectors, explained variance ratio, and scree plots |
| `PCA/Telescope/telescope1.ipynb` | PCA applied to telescope sensor data (`telescope_data.csv`) — data standardisation and component analysis |
| `PCA/Telescope/telescope2.ipynb` | Classifier evaluation on PCA-reduced telescope features — comparing accuracy at different component counts |

#### Perceptron

The building block of neural networks — a single-layer perceptron for binary classification.

| Project | Description |
|---|---|
| `Perceptron/perceptron.ipynb` | Perceptron learning rule — weight updates, decision boundaries, and convergence |
| `Perceptron/gates.ipynb` | Logic gate (AND, OR, NOT) simulation using perceptron models |

#### Regularisation

Techniques to reduce overfitting by penalising model complexity.

| Project | Description |
|---|---|
| `Regularisation/regularisation.ipynb` | L1 (Lasso) and L2 (Ridge) regularisation on student maths performance data (`students_maths.csv`) — coefficient shrinkage and validation curve comparison |

#### Wrapper Methods (Feature Selection)

Filter-free feature selection using model performance as the selection criterion.

| Project | Description |
|---|---|
| `WrapperMethod/wrapper.ipynb` | Wrapper method concepts — sequential feature selection (SFS/SBS) and recursive feature elimination (RFE) |
| `WrapperMethod/eating_habit/wrapper_method_solution.ipynb` | Feature selection on eating habits and obesity data (`obesity.csv`) — RFE with logistic regression and accuracy tracking |
| `WrapperMethod/eating_habit/wrapper_methods_project_v2/wrapper_method_projects/wrapper_method_starter.ipynb` | Starter notebook for the wrapper methods guided project |

#### Handwriting Recognition

An end-to-end digit recognition project using `scikit-learn` on the MNIST-style digits dataset, with a browser-based canvas drawing interface.

| File | Description |
|---|---|
| `Handwriting Recognition/script.py` | Core ML script — trains a `KMeans` digit classifier on `sklearn.datasets.load_digits`, produces cluster centre and sample visualisations |
| `Handwriting Recognition/index.html` | Browser canvas UI for drawing digits — sends the drawing to the Python backend for prediction |
| `Handwriting Recognition/JsCode.js` | JavaScript — captures canvas strokes, preprocesses pixel data, and calls the prediction endpoint |
| `Handwriting Recognition/test.html` | Secondary test page for the canvas drawing interface |
| `Handwriting Recognition/outputs/cluster_centers.png` | Visualisation of the 10 KMeans cluster centres (one per digit) |
| `Handwriting Recognition/outputs/digits_overview.png` | Grid overview of sample digits from the dataset |
| `Handwriting Recognition/outputs/sample_digit.png` | Single sample digit image |
| `Handwriting Recognition/requirements.txt` | Dependencies: `matplotlib`, `numpy`, `scikit-learn` |

#### Recommender System

| Project | Description |
|---|---|
| `Recommender System/recommender.ipynb` | Collaborative filtering book recommender system using Goodreads ratings (`goodreads_ratings.csv`) — user-item matrix, cosine similarity, and top-N recommendations |

#### Exploratory Data Analysis — GDP & Life Expectancy

| Project | Description |
|---|---|
| `EDA_GDP/life_expectancy_gdp.ipynb` | EDA on GDP and life expectancy across multiple countries (`all_data.csv`) — scatter plots, correlation analysis, grouped comparisons, and trend visualisation with `matplotlib` and `seaborn` |

#### Pipeline

| Project | Description |
|---|---|
| `Pipeline/bone_marrow.ipynb` | End-to-end `sklearn.pipeline.Pipeline` for bone marrow transplant outcome prediction (`bone-marrow.arff`) — `ColumnTransformer` for mixed preprocessing, imputation, encoding, scaling, and classifier evaluation in a single pipeline |

#### Neural Networks

Multi-layer neural networks built with TensorFlow/Keras for regression and classification.

| Project | Description |
|---|---|
| `Neural Networks/neural.ipynb` | Neural network fundamentals — layer architecture, forward pass, activation functions (`ReLU`, `sigmoid`), loss functions, and backpropagation |
| `Neural Networks/Life_Expectancy/life.ipynb` | Neural network regression on life expectancy data (`life_expectancy.csv`) — feature normalisation, `Dense` layers, training/validation curves, and MAE evaluation |

#### Classification with TensorFlow

| Project | Description |
|---|---|
| `Classification_Tensorflow/HeartFailureClassification/heart.ipynb` | Binary classification of heart failure outcomes (`heart_failure.csv`) using TensorFlow/Keras — feature preprocessing, `Sequential` model with `Dense` + `Dropout` layers, `Adam` optimiser, `binary_crossentropy` loss, training curves, and classification report |

#### Convolutional Neural Networks (CNN)

| Project | Description |
|---|---|
| `CNN/galaxy.ipynb` | CNN galaxy morphology classifier — 4 classes (Regular, Ringed, Merger, Other); convolutional + pooling layers, `ImageDataGenerator` augmentation, training, and evaluation |
| `CNN/app.py` | Data loader helper — fetches and caches the galaxy `.npz` dataset from the Codecademy CDN; returns `(data, labels)` arrays |
| `CNN/visualize.py` | Activation visualiser — builds a `keras.Model` that outputs every `Conv2D` layer's activations, runs 5 validation samples through it, and saves per-filter greyscale plots alongside prediction vs. true label images |

---

### Flask Web Applications

A progression of Flask projects from a single-file introductory app through to a full-stack multi-user web application with authentication, a database ORM, and form validation.

#### First Flask App

| File | Description |
|---|---|
| `Flask/first_flask_app.py` | Introductory Flask app — defines routes, returns inline HTML responses, and demonstrates the request/response cycle |

#### Pet Shop

A dynamic multi-page Flask app serving pet listings from an in-memory dictionary.

| File | Description |
|---|---|
| `Flask/pet-shop/app.py` | Three routes: `/` (index with category links), `/animals/<pet_type>` (list of pets), `/animals/<pet_type>/<int:pet_id>` (individual pet detail with image, breed, and age) |
| `Flask/pet-shop/helper.py` | Data store — `pets` dictionary with dogs (Spot, Shadow), cats (Snowflake), and rabbits (Easter), each with name, age, breed, description, and image URL |

#### Tourist Attractions App

A CRUD tourist attractions manager with categorised lists, form-based additions, and record promotion/deletion.

| File | Description |
|---|---|
| `Flask/tourist-attractions-app/app.py` | Routes: `/` (redirects to recommended), `/<category>` (GET/POST — displays and manages location list), `/add_location` (POST — validates and adds a new location) |
| `Flask/tourist-attractions-app/forms.py` | `AddLocationForm` — `name` (StringField), `description` (TextAreaField), `category` (RadioField: Recommended / Places To Go / Visited) with `DataRequired` validators |
| `Flask/tourist-attractions-app/locations.py` | `Locations` class — in-memory location store with `add`, `delete`, `moveup`, and `get_list_by_category` methods |
| `Flask/tourist-attractions-app/data.csv` | Seed data for initial location records |
| `Flask/tourist-attractions-app/templates/base.html` | Shared Jinja2 base layout |
| `Flask/tourist-attractions-app/templates/locations.html` | Location list template with category tabs, add form, and promote/delete buttons |

#### Flask-SQLAlchemy Demo

Demonstrates Flask + SQLAlchemy ORM — model definitions, relationships, data insertion, and querying. See [`Flask/Flask-SQLAlchemy/README.md`](Flask/Flask-SQLAlchemy/README.md) for setup instructions.

| File | Description |
|---|---|
| `Flask/Flask-SQLAlchemy/app.py` | Defines three models: `Book` (id, title, author_name, author_surname, month, year), `Reader` (id, name, surname, email), `Review` (id, stars, text, book_id FK, reviewer_id FK) — one-to-many relationships between Book↔Review and Reader↔Review |
| `Flask/Flask-SQLAlchemy/create_object.py` | Inserts sample data: 2 books (`Demian` by Hesse, `The Stranger` by Camus), 2 readers (Ann Adams, Sam Adams), and 2 reviews — commits to `myDB.db` |

#### To-Do App

A persistent to-do list backed by SQLite, with Flask-WTF form submission.

| File | Description |
|---|---|
| `Flask/To-Do_App/app.py` | Single route `/` (GET/POST) — renders `TodoForm` (WTForms `StringField` + `SubmitField`), saves new `Todo` records (`id`, `todo_text`) to SQLite via SQLAlchemy, and passes all todos to the template |
| `Flask/To-Do_App/create_todos.py` | Utility script to seed initial todo entries |
| `Flask/To-Do_App/templates/index.html` | Jinja2 template — displays the todo list and the submission form |

#### TriPlanned — Travel Site

A full-stack multi-user travel planning app with authentication, per-user trip posts, and a community landing page. See [`Flask/Travel_Site/README.md`](Flask/Travel_Site/README.md) for detailed setup.

**Models** (`models.py`):
- `User` — `id`, `username` (unique), `email` (unique), `password_hash` (Werkzeug `generate_password_hash`); one-to-many relationship with `Post`
- `Post` — `id`, `city`, `country`, `description`, `timestamp`, `user_id` FK

**Forms** (`forms.py`):
- `RegistrationForm` — `username`, `email`, `password`, `password2` (EqualTo validator); custom validators check DB for duplicate username/email
- `LoginForm` — `username`, `password`, `remember_me` (BooleanField)
- `DestinationForm` — `city`, `country`, `description` for submitting a new trip post

**Routes** (`routes.py`):

| Route | Methods | Description |
|---|---|---|
| `/` | GET | Landing page — renders `landing_page.html` (community trip posts) |
| `/register` | GET, POST | New account creation — hashes password, writes `User` to DB, redirects to login |
| `/login` | GET, POST | Authenticates user via `check_password_hash`, starts Flask-Login session, supports `remember_me` and `next` redirect |
| `/logout` | GET | Calls `logout_user()`, redirects to login |
| `/user/<username>` | GET, POST | `@login_required` — displays user's posts and `DestinationForm`; on POST creates a new `Post` record |

| File | Description |
|---|---|
| `Flask/Travel_Site/app.py` | App factory — configures `SECRET_KEY`, `SQLALCHEMY_DATABASE_URI` (SQLite `test.db`), initialises `db` and `login` extensions, registers `user_loader`, imports routes, calls `db.create_all()` |
| `Flask/Travel_Site/extensions.py` | Separate module holding `db = SQLAlchemy()` and `login = LoginManager()` to avoid circular imports |
| `Flask/Travel_Site/models.py` | `User` and `Post` ORM models |
| `Flask/Travel_Site/routes.py` | All URL route handlers |
| `Flask/Travel_Site/forms.py` | WTForms form definitions |
| `Flask/Travel_Site/templates/base.html` | Shared Jinja2 base layout with navigation |
| `Flask/Travel_Site/templates/landing_page.html` | Home page showing community trip posts |
| `Flask/Travel_Site/templates/login.html` | Login form page |
| `Flask/Travel_Site/templates/register.html` | Registration form page |
| `Flask/Travel_Site/templates/user.html` | User dashboard — displays user's trips and destination submission form |

**Tech stack:** Flask · Flask-SQLAlchemy · Flask-Login · Flask-WTF / WTForms · Werkzeug · email-validator · SQLite

---

## Bike Rental Data

A data engineering and analytics project using 2016 CitiBike (Jersey City) trip data, Newark airport weather data, SQL queries, and a Python notebook.

| File / Folder | Description |
|---|---|
| `bike-rental-starter-kit/bike_data.ipynb` | Main notebook — data ingestion of 12 monthly CSVs, cleaning, feature engineering (trip duration, distance), joins with weather data, and visualisation |
| `bike-rental-starter-kit/data/combined_bike_data.csv` | Pre-merged dataset combining all monthly trip files |
| `bike-rental-starter-kit/data/JC-201601-citibike-tripdata.csv` … `JC-201612-citibike-tripdata.csv` | Raw monthly CitiBike trip records (Jan–Dec 2016) — start/end station, coordinates, duration, user type, bike ID |
| `bike-rental-starter-kit/data/newark_airport_2016.csv` | Hourly weather data from Newark Liberty Airport for 2016 — temperature, precipitation, wind speed |
| `bike-rental-starter-kit/data-dictionaries/citibike.pdf` | Field definitions for CitiBike trip data columns |
| `bike-rental-starter-kit/data-dictionaries/weather.pdf` | Field definitions for the weather dataset columns |
| `bike-rental-starter-kit/queries/average_distance.sql` | SQL — average trip distance per station pair |
| `bike-rental-starter-kit/queries/popular_distance.sql` | SQL — most frequently occurring trip distances |
| `bike-rental-starter-kit/queries/popular_routes.sql` | SQL — top station-to-station routes by ride count |
| `bike-rental-starter-kit/queries/ride.sql` | SQL — per-ride metrics including duration and distance |
| `bike-rental-starter-kit/queries/unique_stations_pairs.sql` | SQL — distinct origin/destination station pair combinations |
| `bike-rental-starter-kit/queries/weekly_rides.sql` | SQL — weekly ride volume aggregation over the year |

> `Bike-Rental-Data/` is an empty placeholder directory. All project content lives in `bike-rental-starter-kit/`.

---

## Getting Started

### Notebooks

1. Install Python 3.10 or newer.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS / Linux
   ```
3. Install notebook dependencies:
   ```bash
   pip install jupyter scikit-learn pandas numpy matplotlib seaborn scipy tensorflow
   ```
4. Launch JupyterLab from the repository root:
   ```bash
   jupyter lab
   ```

### Handwriting Recognition

```bash
pip install -r "Handwriting Recognition/requirements.txt"
python "Handwriting Recognition/script.py"
```

### Flask Apps

Each Flask project has its own virtual environment under its folder. To run any app:

```bash
cd Flask/<project-folder>
<project-folder>\Scripts\activate   # Windows
pip install flask flask-sqlalchemy flask-login flask-wtf email-validator
flask run
```

For the **TriPlanned** Travel Site specifically — see [`Flask/Travel_Site/README.md`](Flask/Travel_Site/README.md).  
For the **Flask-SQLAlchemy** demo — see [`Flask/Flask-SQLAlchemy/README.md`](Flask/Flask-SQLAlchemy/README.md).

---

## Dependencies

| Package | Used in |
|---|---|
| `scikit-learn` | All ML algorithm notebooks, Handwriting Recognition |
| `pandas` | Data loading and manipulation throughout |
| `numpy` | Numerical computation throughout |
| `matplotlib` | Visualisation throughout |
| `seaborn` | Statistical visualisation (EDA, regression notebooks) |
| `scipy` | Linear regression (`linregress`), statistical tests |
| `tensorflow` / `keras` | Neural Networks, TensorFlow Classification, CNN |
| `flask` | All Flask web app projects |
| `flask-sqlalchemy` | Flask-SQLAlchemy demo, To-Do App, Travel Site |
| `flask-login` | Travel Site — session and authentication management |
| `flask-wtf` / `wtforms` | Tourist Attractions App, To-Do App, Travel Site — form handling and validation |
| `email-validator` | Travel Site — `Email()` WTForms validator |
| `werkzeug` | Travel Site — `generate_password_hash` / `check_password_hash` |
| `jupyter` | All `.ipynb` notebooks |

> Some notebooks may require additional packages. Check individual notebook import cells or any `requirements.txt` present in the project folder.

---

## Notes

- Projects are primarily based on [Codecademy](https://www.codecademy.com) courses — see the learning credit note at the top.
- Folder and notebook names are preserved from their original project structure.
- Datasets are stored alongside notebooks to support self-contained local execution.
- Virtual environment directories (`Include/`, `Lib/`, `Scripts/`, `var/`) inside Flask project folders are excluded from version control via `.gitignore`.
- The `__MACOSX/` folder at the repo root is a macOS artifact from the original zip extraction and can be ignored.

---

## License

No license is specified for this repository at this time. All Codecademy course materials and datasets remain the intellectual property of [Codecademy](https://www.codecademy.com).

## Disclaimer & Credits

This repository is a personal portfolio created for educational purposes. The code represents my own implementation and learning journey through various machine learning concepts. 

The project structures, guided prompts, and specific educational datasets used in this repository are credited to [Codecademy](https://www.codecademy.com). Many of the underlying datasets originate from public open-source repositories (e.g., UCI Machine Learning Repository, Kaggle). 

No commercial use is intended. All Codecademy proprietary curriculum materials remain their intellectual property.