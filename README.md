# Investment Recommendation System with Machine Learning

## Description
**Investment Recommendation System** is an advanced machine learning project that integrates with a stock data retrieval system. This tool reads financial data stored in a PostgreSQL database, analyzes it using machine learning algorithms, and classifies investments based on fundamental financial factors. It employs clustering and classification techniques to recommend the best investment options.

## Table of Contents

- [Description](#description)
- [How to Use](#how-to-use)
- [Features](#features)
- [Dependencies](#dependencies)
- [Execution](#execution)

## How to Use

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone <repository-link>
```

### 2. Set Up Database
Ensure the PostgreSQL database `ml_fundamentus` is running with the required tables and data. Use the accompanying stock data retrieval project to populate the database.

### 3. Configure Connection
Update the `param_dic` dictionary in the script with your PostgreSQL connection details:
```python
param_dic = {
    "host": "localhost",
    "database": "ml_fundamentus",
    "user": "postgres",
    "password": "postgres"
}
```

### 4. Run the Notebook
Open the project in Jupyter Notebook or any Python IDE, and execute the cells sequentially to:

1. Fetch data from the database.
2. Preprocess and analyze the data.
3. Apply machine learning algorithms for classification and clustering.

## Features

- **Database Integration**: Reads financial data directly from a PostgreSQL database.
- **Data Analysis**: Performs exploratory data analysis and visualization.
- **Machine Learning Models**:
  - Clustering: Identifies groups of similar investments using KMeans.
  - Classification: Evaluates and recommends investments based on financial indicators.
- **Performance Metrics**: Calculates accuracy, F1 scores, and visualizes results.

## Dependencies

The project relies on the following Python libraries:

- `numpy`
- `pandas`
- `psycopg2`
- `matplotlib`
- `seaborn`
- `scikit-learn`

Install the dependencies using pip:
```bash
pip install numpy pandas psycopg2 matplotlib seaborn scikit-learn
```

## Execution

### From Jupyter Notebook

1. Open the notebook in Jupyter or your preferred Python IDE.
2. Run each cell sequentially to load data, preprocess, and apply machine learning models.

### From Command Line

1. Ensure the database connection parameters are configured correctly.
2. Run the script using:
   ```bash
   python <script_name>.py
   ```
