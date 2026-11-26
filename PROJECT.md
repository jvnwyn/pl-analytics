# Premier League Analytics Platform

An end-to-end football analytics platform that collects, processes, stores, analyzes, visualizes, and predicts Premier League match data using Python, Jupyter Notebook, AWS, SQL, and Power BI.

---

# Project Goal

Build a cloud-based analytics platform that demonstrates the complete data analytics lifecycle:

- Collect Premier League data
- Clean and transform raw data
- Perform exploratory data analysis (EDA)
- Store data in AWS
- Query data using SQL
- Build interactive Power BI dashboards
- Predict future match outcomes using Machine Learning
- Automate data updates
- Simulate an entire season using Monte Carlo methods

---

# Learning Objectives

By completing this project, you will gain hands-on experience with:

- Python
- Pandas
- NumPy
- SQL
- Jupyter Notebook
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- AWS S3
- AWS Glue
- Amazon Athena
- AWS Lambda
- Amazon EventBridge
- IAM (least-privilege policy design)
- Power BI
- Power Query
- DAX
- Machine Learning
- Monte Carlo Simulation
- Statistical Shrinkage
- Git & GitHub

---

# 🛠 Tech Stack

## Programming

- Python
- SQL

## Development Environment

- Jupyter Notebook
- VS Code

## Python Libraries

- pandas
- numpy
- matplotlib
- plotly
- seaborn
- requests
- scikit-learn
- sqlalchemy
- boto3

## Cloud

- AWS S3
- AWS Glue
- Amazon Athena
- AWS Lambda
- Amazon EventBridge

## Visualization

- Power BI

## Version Control

- Git
- GitHub

---

# System Architecture

Football API

↓

Python (Jupyter Notebook) — Data Cleaning → Feature Engineering

↓

Amazon S3 Data Lake

↓

AWS Glue / Amazon Athena

↓

Power BI Dashboard

↓

Machine Learning Predictions & Season Simulation

↓

AWS Lambda + EventBridge (automated daily ingestion of new match data)

---

# Repository Structure

premier-league-analytics/

├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_exploratory_analysis.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_upload_to_s3.ipynb
│   ├── 06_sql_analysis.ipynb
│   ├── 07_machine_leaning.ipynb
│   ├── 08_season_simulation.ipynb
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── features/
│   └── predictions/
│
├── lambda/
│   └── lambda_function.py
│
├── dashboards/
│   └── PremierLeagueDashboard.pbix
│
├── sql/
│   ├── create_tables.sql
│   └── analytics_queries.sql
│
├── reports/
│   ├── screenshots/
│   └── dashboard.pdf
│
├── requirements.txt
├── requirements-dev.txt
├── README.md
└── PROJECT.md

---

# Development Roadmap

---

# Phase 1 — Data Collection

## Objective

Collect Premier League data across multiple seasons from football-data.org.

## Notebook

01_data_collection.ipynb

## Tasks

- Pull match data for the 2023/24, 2024/25, and 2025/26 seasons
- Pull team data across the same seasons
- Extract a clean season year (e.g. `"2023"`) from the API's nested season object *before* saving, so every downstream notebook works with a plain, consistent value
- Save raw multi-season datasets

## Output

- raw_matches_multi_season.csv
- raw_teams_multi_season.csv

## Skills

- API Integration
- Data Collection
- Pandas

---

# Phase 2 — Data Cleaning

## Notebook

02_data_cleaning.ipynb

## Tasks

- Parse nested JSON-like `score`/`homeTeam`/`awayTeam` fields into plain columns
- Filter to finished matches only
- Select final columns and save

## Output

clean_matches_multi_season.csv

## Skills

- Data Cleaning
- Data Wrangling
- Pandas

---

# Phase 3 — Exploratory Data Analysis

## Notebook

03_exploratory_analysis.ipynb

## Scope

Rebuilt to run against the full multi-season dataset (2023/24–2025/26), rather than a single season, for consistency with the rest of the pipeline. League standings and each match's "upset magnitude" are now derived per-season directly from match results, rather than a separate single-season standings pull.

## Questions Answered

- Which team scores the most goals (across all seasons)?
- Which team has the strongest defense (across all seasons)?
- Which months have the most goals, and the highest average goals per match?
- Which matches were the biggest upsets, judged against each team's final position *for that season*?

## Visualizations

- Bar charts (top scorers, best defense, goals by month)

## Known Limitation

"Upset magnitude" uses each team's *final* season position to judge every match in that season, including matches played in August — so an early-season result can only be judged an upset in hindsight, once that season's table is decided.

## Skills

- Exploratory Data Analysis
- Data Visualization

---

# Phase 4 — Feature Engineering

## Notebook

04_feature_engineering.ipynb

## Features Created

- Rolling Form (last 5 matches, shifted to avoid leakage)
- Win Streak / Loss Streak
- Average Goals Scored / Conceded (expanding, shifted)
- Clean Sheet Percentage
- Days Since Last Match
- Home Win % / Away Win %
- Head-to-Head Win % (across all historical seasons, not reset per season)
- **Prior Season Position** — each team's final league position the season before, added to support preseason-style predictions (see Phase 11). Newly-promoted teams with no top-flight history default to the historical average finishing position of promoted teams already in the dataset, rather than an arbitrary guess.

## Skills

- Feature Engineering
- Statistical Defaults / Imputation

---

# Phase 5 — AWS Data Lake

## Notebook

05_upload_to_s3.ipynb

## Tasks

- Upload processed and feature datasets to S3, one dataset per subfolder
- Upload model predictions
- Upload Phase 11 season simulation outputs

## Folder Structure

s3://pl-analytics-2026/

- raw/
- processed/
- features/
- predictions/

## Skills

- AWS S3
- Cloud Storage

---

# Phase 6 — AWS Glue & Athena

## Tasks

- Manually define external tables in the Glue Data Catalog (`pl_analytics` database) for each dataset
- Query datasets via Amazon Athena

## Tables

- clean_matches / clean_matches_multi_season
- match_features / match_features_multi_season
- predictions
- season_simulation_summary
- preseason_simulation_summary
- midseason_vs_preseason_comparison
- season_simulation_raw
- preseason_simulation_raw

## Skills

- AWS Glue
- Data Catalog
- Amazon Athena

---

# Phase 7 — SQL Analysis

## Notebook

06_sql_analysis.ipynb

## Query Examples

- Top scoring teams / best defensive records
- League-wide home/away/draw split
- Highest-scoring individual matches
- All-time league table
- Longest win streaks
- Biggest home-vs-away performance gaps

## Skills

- SQL
- Amazon Athena

---

# Phase 8 — Power BI Dashboards

## Executive Dashboard

KPIs: Total Matches, Total Goals, Average Goals, Home/Away/Draw Win %, Total Teams. Charts: League Table, Monthly Goals, Win Distribution.

## Team Performance Dashboard

Wins, Draws, Losses, Goal Difference, Points, Recent Form, Home/Away Performance.

## Offensive Dashboard

Goals, Shots, Shots on Target, Conversion Rate.

## Defensive Dashboard

Goals Conceded, Clean Sheets, Fouls, Yellow/Red Cards.

## Prediction Dashboard

Home Win / Draw / Away Win Probability, Predicted Winner — powered by the retrained Logistic Regression model (see Phase 9).

## Season Outlook Dashboard

New in Phase 11. Built from `season_simulation_summary` (1,000-run Monte Carlo mid-season simulation):
- **Title Race** — % of simulations won, top 8 teams
- **Top 4 Race** — % of simulations finishing in Champions League spots, top 8 teams
- **Relegation Battle** — % of simulations finishing in the bottom 3, top 8 teams
- **Full Season Outlook table** — all 20 teams: average points, average position, title/top-4/relegation odds

## Skills

- Power BI
- Power Query
- DAX
- Dashboard Design

---

# Phase 9 — Machine Learning

## Notebook

07_machine_leaning.ipynb

## Objective

Predict match outcomes (Home Win / Draw / Away Win) using engineered features.

## Model Used

Logistic Regression (unscaled) — the version actually saved and used everywhere downstream (dashboard, season simulation).

## Features

18 total (9 home + 9 away): rolling form, win/loss streaks, average goals scored/conceded, clean sheet %, days since last match, head-to-head win %, and prior season position.

## Retraining Note

The model was retrained during Phase 11 to add `prior_season_position` as a feature (accuracy improved from 42.8% to 43.7%). While retraining, a stale bug was found and fixed: an earlier version of the column-drop logic only removed 2 of 4 irrelevant win-pct columns, meaning the model had silently been trained on 16 features instead of the intended 18 for a period — caught by checking `model.feature_names_in_` directly against the notebook's code.

## Evaluation Metrics

Accuracy, Precision, Recall, F1 Score, Confusion Matrix. Random Forest and XGBoost were trained for comparison but are not the saved/deployed model.

## Known Limitation

Draw prediction remains weak (F1 ≈ 0.08) — the model is much better at distinguishing Win/Loss than identifying draws, a common challenge in football outcome prediction.

## Skills

- Machine Learning
- scikit-learn
- Model Evaluation

---

# Phase 10 — Automation ✅

## Status

Complete (scoped down from original plan — see Design Decision below). Verified running automatically, unattended, on a daily schedule for over a week (Sept 6–13, 2026) via CloudWatch log review.

## What Was Built

- **AWS Lambda function** (`lambda/lambda_function.py`) that calls the football-data.org API for recently finished Premier League matches and writes them to S3.
- **IAM role** scoped narrowly to `s3:PutObject` on the incremental data folder only, plus CloudWatch logging permissions.
- **EventBridge scheduled trigger** (daily cron, 06:00 UTC) invoking the Lambda automatically.
- Verified end-to-end via manual test invocation, then confirmed real automatic daily runs via CloudWatch log streams.

## Actual Workflow

AWS EventBridge (daily schedule)

↓

AWS Lambda — fetch recent finished matches from football-data.org

↓

Upload raw match data to S3 (`raw/raw_matches_incremental/<date>/matches.csv`)

## Design Decision: Scope Reduction

The original plan (API → Lambda → S3 → Glue table refresh → Athena → Power BI, fully automated end-to-end) was deliberately scaled back to **raw data ingestion only**. Reasoning:

- The feature-engineering pipeline (Phase 4) relies on rolling and expanding calculations across a team's full match history — recomputing these correctly and leakage-safely inside a stateless Lambda invocation would require duplicating notebook logic into a second codebase, with real risk of subtle bugs or leakage if the two ever drifted out of sync.
- A raw-only landing zone is simpler to test, debug (via CloudWatch), and reason about, while still demonstrating the core serverless automation skillset.
- Refreshing `clean_matches` / `match_features` and Power BI remains a manual notebook step for now.

## Future Extension: Full Pipeline Automation (Not Built)

1. **Glue/Athena auto-refresh** — schedule the Glue Crawler (or automate partition registration) so new incremental S3 files appear in Athena without manual steps.
2. **Automated feature recomputation** — a Glue ETL job or heavier Lambda to rerun cleaning/feature-engineering logic against full match history whenever new data lands. Deferred due to sync-risk with the notebook logic.
3. **Power BI Service scheduled refresh** — requires a Pro license and an On-premises Data Gateway to bridge Power BI Service to Athena. Deferred as an unnecessary cost/infrastructure jump for a portfolio project scoped to AWS Free Tier.

## Skills

- AWS Lambda
- IAM (least-privilege policy design)
- Amazon EventBridge
- Automation
- Cloud Pipelines

---

# Phase 11 — Season Simulation (Monte Carlo) ✅

## Notebook

08_season_simulation.ipynb

## Objective

Predict the outcome of the remaining 2026/27 season using the Phase 9 Logistic Regression model, chained across simulated match results, and compare against a "blank slate" preseason-style projection.

## Approach

- Fetches remaining `SCHEDULED` fixtures via football-data.org.
- **Mid-season simulation**: for each of 1,000 simulated seasons, predicts each fixture using live, continuously updated team state (rolling form, goals, head-to-head), seeded from today's real results so far.
- **Preseason simulation**: the same engine, but every team starts from a blank slate (only `prior_season_position` and historical head-to-head — no in-season results used), isolating how much of the mid-season outlook is driven by early-season form.
- Generates realistic scorelines via a Poisson goal model, with statistical shrinkage toward league averages for small-sample teams, consistent with the classifier's predicted Win/Draw/Loss outcome.
- Runs 1,000 independent Monte Carlo simulations per mode, aggregating results into title/top-4/relegation probabilities per team.

## Key Finding: The Hull City Case Study

Early in development, Hull City AFC (newly promoted) showed an implausibly strong mid-season outlook (31% chance of a top-4 finish) after a genuinely strong but tiny 3-game sample (2W-1D, 0 goals conceded — including a 2-0 win over Manchester United). Investigation showed this wasn't a bug: the underlying results were real, and shrinkage alone couldn't fully account for it, since Hull's opponents weren't a weak schedule. The distortion was resolved by retraining the model with a `prior_season_position` feature and adding shrinkage to form-based features (`rolling_form_pts`, `clean_sheet_pct`) — after which Hull's mid-season top-4 odds settled to a far more plausible ~11%, and the preseason-mode projection (using only prior-season standing) shows an even more conservative ~4%.

## Output

- data/predictions/season_simulation_summary.csv
- data/predictions/season_simulation_raw.csv
- data/predictions/preseason_simulation_summary.csv
- data/predictions/preseason_simulation_raw.csv
- data/predictions/midseason_vs_preseason_comparison.csv

All five also registered as external tables in Athena (`pl_analytics` database) and used to power the new **Season Outlook** dashboard page in Power BI (see Phase 8).

## Known Limitation

The model has no feature for opponent strength ("strength of schedule") — goals-based features treat every opponent identically regardless of quality. This was investigated directly as part of the Hull City case study and found not to be the primary driver of that specific anomaly, but remains a general limitation of the model.

## Skills

- Monte Carlo Simulation
- Poisson Modeling
- Statistical Shrinkage
- Applied Machine Learning
- Debugging & Root-Cause Analysis

---

# Key Performance Indicators (KPIs)

- Matches Played
- Goals Scored / Conceded
- Goal Difference
- Win / Draw / Loss Percentage
- Home / Away Win Percentage
- Average Goals Per Match
- Clean Sheets
- Title / Top-4 / Relegation Probability (Monte Carlo)

---

# Machine Learning Features

- Rolling Form
- Home Advantage
- Away Form
- Goal Difference
- Average Goals Scored / Conceded
- Head-to-Head Results
- Win Streak
- Clean Sheet Percentage
- Rest Days
- Prior Season Position

---

# Skills Demonstrated

- Python, Pandas, NumPy
- Jupyter Notebook
- Data Cleaning & Exploratory Data Analysis
- Feature Engineering & Statistical Imputation
- SQL & Amazon Athena
- AWS S3, Glue, Lambda, EventBridge, IAM
- Power BI, Power Query, DAX
- Machine Learning (scikit-learn)
- Monte Carlo Simulation & Poisson Modeling
- ETL Pipelines & Cloud Automation
- Git & GitHub
- Root-cause debugging (pandas dtype inference, stale notebook state, silent training-data mismatches)

---

# Stretch Goals

- Strength-of-schedule adjustment for the goal model
- Automated feature recomputation on new incoming data (Phase 10 Future Extension)
- Power BI Service scheduled refresh
- Live API integration for in-play updates
- Interactive Streamlit dashboard
- Player-level analytics
- Docker containerization
- GitHub Actions CI/CD
- Infrastructure as Code (Terraform)

---

# Final Deliverables

- Jupyter Notebook analysis (8 notebooks, Phases 1–11)
- Clean, multi-season datasets
- AWS cloud pipeline (S3, Glue, Athena, Lambda, EventBridge)
- SQL analytics queries
- Interactive Power BI dashboard (6 pages, including Season Outlook)
- Machine learning prediction model + Monte Carlo season simulation
- GitHub repository with honest, in-line documentation of known limitations and design tradeoffs
- Architecture diagram

---

# Portfolio Outcome

This project demonstrates an end-to-end analytics workflow:

1. Collect real-world, multi-season Premier League data.
2. Clean and prepare data using Python.
3. Perform exploratory data analysis across all seasons.
4. Engineer predictive features, including a defensible statistical default for missing data (promoted teams).
5. Store data in a structured AWS data lake.
6. Query cloud data using SQL via Athena.
7. Build business intelligence dashboards in Power BI, including a Monte Carlo–powered season outlook.
8. Predict match outcomes using Machine Learning, with documented retraining and bug-fix history.
9. Automate data ingestion with AWS Lambda and EventBridge, verified over a real week of unattended runs.
10. Diagnose and resolve a genuine model anomaly (the Hull City case) through investigation rather than assumption — a concrete example of critical thinking, not just pipeline-building.
11. Showcase the complete solution in a professional GitHub portfolio.
