# Premier League Analytics Platform

An end-to-end football analytics project that demonstrates modern data analytics, cloud computing, business intelligence, and machine learning using real-world Premier League data.

This project collects match data, performs exploratory data analysis (EDA), stores data in AWS, queries it with SQL, visualizes insights in Power BI, and predicts match outcomes using machine learning.

---

# Project Overview

The goal of this project is to simulate a real-world sports analytics platform by building an end-to-end data pipeline.

The workflow includes:

- Collecting Premier League data
- Cleaning and validating datasets
- Performing exploratory data analysis
- Engineering predictive features
- Storing data in AWS
- Querying cloud data with SQL
- Creating interactive Power BI dashboards
- Predicting match outcomes with machine learning
- Automating future data updates

---

# Tech Stack

## Programming

- Python
- SQL

## Development

- Jupyter Notebook
- Visual Studio Code

## Python Libraries

- Pandas
- NumPy
- Matplotlib
- Plotly
- Seaborn
- Requests
- Scikit-learn
- SQLAlchemy
- Boto3
- AWS Wrangler

## Cloud

- Amazon S3
- AWS Glue
- Amazon Athena
- AWS Lambda *(Future)*

## Business Intelligence

- Power BI
- Power Query
- DAX

## Version Control

- Git
- GitHub

---

# Project Architecture

```text
Football Data Source
        │
        ▼
Jupyter Notebook (Python)
        │
        ▼
Data Cleaning & Feature Engineering
        │
        ▼
Amazon S3 Data Lake
        │
        ▼
AWS Glue Data Catalog
        │
        ▼
Amazon Athena
        │
        ▼
Power BI Dashboard
        │
        ▼
Machine Learning Predictions
```

---

# Repository Structure

```text
premier-league-analytics/

├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_exploratory_analysis.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_upload_to_s3.ipynb
│   ├── 06_sql_analysis.ipynb
│   └── 07_machine_learning.ipynb
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── features/
│
├── dashboards/
│   └── PremierLeagueDashboard.pbix
│
├── sql/
│   ├── create_tables.sql
│   └── analytics_queries.sql
│
├── aws/
│   ├── architecture.png
│   └── lambda_update.py
│
├── reports/
│   ├── screenshots/
│   └── dashboard.pdf
│
├── requirements.txt
├── requirements-dev.txt
├── PROJECT.md
└── README.md
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/pl-analytics.git

cd pl-analytics
```

---

## 2. Create a virtual environment

```bash
python -m venv .venv
```

---

## 3. Activate the virtual environment

### Windows

If you get an error about scripts being disabled, run this first (only needs to be done once per terminal session):

​```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
​```

Then activate:

​```powershell
.venv\Scripts\activate
​```

### macOS/Linux

```bash
source .venv/bin/activate
```

---

## 4. Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

## 5. Install dependencies

​```bash
pip install -r requirements.txt
​```

This installs all required packages, including:

- **pandas / numpy** — data manipulation
- **requests** — football-data.org API calls
- **python-dotenv** — loading `.env` configuration
- **matplotlib / seaborn** — data visualization
- **scikit-learn** — machine learning (Phase 9)
- **boto3** — AWS SDK (S3, Athena)
- **s3fs** — lets pandas read/write directly from S3 paths
- **awscli** — AWS CLI, installed via pip since it doesn't require admin/IT permissions on locked-down systems

---

# Troubleshooting

**PowerShell blocks venv activation ("running scripts is disabled")**
Run once per terminal session before activating:
​```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
​```

**`aws` command not found**
Your `.venv` must be activated first — check for `(.venv)` at the start of your terminal prompt. If missing, run `.venv\Scripts\activate`.

**Notebook can't find data files (FileNotFoundError)**
All notebooks assume they're run from inside the `notebooks/` folder, using relative paths like `../data/raw/`. Confirm with `os.getcwd()` if a path error occurs.

---

## 6. Register the Jupyter kernel

```bash
python -m ipykernel install --user --name premier-league-analytics --display-name "Premier League Analytics"
```

---

## 7. Launch Jupyter Lab

```bash
jupyter lab
```

---

# Environment Variables

This project needs a `.env` file in the project root (same folder as `README.md`) to store your API key and AWS settings. This file is git-ignored and should never be committed.

Copy the template below into a new file named `.env`:

​```
# football-data.org API key
# Register for free at: https://www.football-data.org/client/register
FOOTBALL_DATA_API_KEY=your_api_key_here

# AWS settings
AWS_REGION=ap-southeast-2
AWS_S3_BUCKET=your-bucket-name
​```

**Note:** AWS credentials themselves (Access Key ID / Secret Access Key) are configured separately via `aws configure`, and are **not** stored in this file.

---

# Project Roadmap

- [x] Phase 1 — Data Collection
- [x] Phase 2 — Data Cleaning
- [x] Phase 3 — Exploratory Data Analysis
- [x] Phase 4 — Feature Engineering
- [x] Phase 5 — AWS Data Lake
- [x] Phase 6 — AWS Glue
- [x] Phase 7 — SQL Analytics
- [x] Phase 8 — Power BI Dashboard
- [x] Phase 9 — Machine Learning
- [ ] Phase 10 — Automation with AWS Lambda

---

# Dashboard Features

The Power BI dashboard will include:

### Executive Dashboard

- Total Matches
- Total Goals
- Average Goals
- Home Win Percentage
- Away Win Percentage
- Draw Percentage
- League Table

### Team Dashboard

- Wins
- Draws
- Losses
- Goal Difference
- Home Performance
- Away Performance
- Recent Form

### Offensive Dashboard

- Goals
- Shots
- Shots on Target
- Conversion Rate
- Expected Goals (Future)

### Defensive Dashboard

- Goals Conceded
- Clean Sheets
- Tackles
- Fouls
- Yellow Cards
- Red Cards

### Stadium Dashboard

- Goals Per Match
- Home Win Rate
- Attendance

### Prediction Dashboard

- Home Win Probability
- Draw Probability
- Away Win Probability
- Confidence Score
- Predicted Winner

---

# Machine Learning

The prediction model will classify match outcomes into:

- Home Win
- Draw
- Away Win

Planned algorithms include:

- Logistic Regression
- Random Forest
- XGBoost

Model evaluation will use:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC AUC
- Confusion Matrix

---

# Skills Demonstrated

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- SQL
- AWS S3
- AWS Glue
- Amazon Athena
- Power BI
- Power Query
- DAX
- Machine Learning
- ETL Pipelines
- Cloud Analytics
- Git
- GitHub

---

# Future Enhancements

- Live API integration
- Daily automated data updates
- AWS Lambda automation
- Power BI scheduled refresh
- Player-level analytics
- Fantasy Premier League recommendation engine
- Expected Goals (xG) model
- Streamlit web application
- Docker support
- CI/CD with GitHub Actions

---

# Documentation

Detailed project planning and implementation roadmap can be found in:

- **PROJECT.md**

---

# License

This project is licensed under the MIT License.

---

# Author

**Jovan Wayne Andrade**

Bachelor of Science in Computer Science  
Cavite State University – Main Campus

GitHub: https://github.com/jvnwyn

---

⭐ If you found this project interesting, consider giving it a star!