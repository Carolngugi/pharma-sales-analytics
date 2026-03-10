**#**  Pharma Sales Analytics Dashboard

A full-stack data analytics project built as part of a Database & AI workshop series.

**##** What It Does
An interactive web dashboard that lets users explore pharmaceutical sales data
across 8 drug categories from 2014 to 2019, with filters and normalization toggle.

**##** Tech Stack
**-** Python + Pandas (data processing)
**-** SQLite (database)
**-** Flask (backend API)
**-** HTML + CSS + JavaScript (frontend)

**##** Project Walkthrough
The full database creation process is documented step by step in:
👉 pharma_db.ipynb

This notebook covers:
**-** Loading and inspecting the raw dataset (50,532 rows)
**-** Cleaning data types (datum string → datetime)
**-** Applying min-max normalization to all 8 drug columns
**-** Creating and populating the SQLite database (3 tables, 404,256 records)
**-** Adding indexes for query optimization

**##** How To Run

**###** 1. Clone the repository
git clone https://github.com/Carolngugi/pharma-sales-analytics.git
cd pharma-sales-analytics

**###** 2. Install dependencies
pip install flask pandas

**###** 3. Download the dataset
Download saleshourly.csv from:
https://www.kaggle.com/datasets/milanzdravkovic/pharma-sales-data
Place it inside the data/ folder.

**###** 4. Build the database
Open pharma_db.ipynb in Jupyter and run all cells in order.

**###** 5. Launch the app
python app.py

**###** 6. Open in browser
http://localhost:5001
