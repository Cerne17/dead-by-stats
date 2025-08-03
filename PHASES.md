# Project Phases

This document outlines the development phases for the Dead by Daylight Meta-Analysis Engine.

## Phase 1: Data Acquisition (Completed)

- [x] **Scraper Development:** Create a Python script to scrape perk data from `Nightlight.gg`.
- [x] **Data Storage:** Save the scraped data into structured CSV files (`killer_perks.csv`, `survivor_perks.csv`).
- [x] **Lookup Table:** Create a perk lookup table (`perks_labels.csv`) to map perk IDs to their names.
- [x] **Data Enrichment:** Add the perk labels to the main data files.

## Phase 2: Data Enrichment

- [ ] **Improve the data set:** Include the individual perks categories for survivors (stealth, bloodpoints farming, chase, solo, survive with friends, trolling) and killers (bloodpoints farming, slowdown, chase, information, and trolling)

## Phase 3: Exploratory Data Analysis (EDA)

- [ ] **Data Cleaning:** Investigate and handle any missing or inconsistent data.
- [ ] **Descriptive Statistics:** Calculate basic statistics for perk usage and effectiveness.
- [ ] **Visualization:** Create charts and graphs to visualize perk popularity and win rates.
- [ ] **Correlation Analysis:** Identify initial relationships between perks.

## Phase 4: Machine Learning Model Development

- [ ] **Feature Engineering:** Create new features from the existing data that could be useful for the models.
- [ ] **Model Selection:** Research and choose the most appropriate machine learning models for the project's goals.
- [ ] **Model Training:** Train the selected models on the prepared data.
- [ ] **Model Evaluation:** Evaluate the performance of the trained models.

## Phase 5: Insight Generation and Reporting

- [ ] **"Best Build" Identification:** Use the model's results to identify the most effective perk combinations.
- [ ] **Meta-Analysis:** Summarize the key findings and insights from the data.
- [ ] **Reporting:** Create a final report or dashboard to present the results.

## Phase 6: Data Visualization

- [ ] **Build a "Dashboard":** Create a frontend to show the trending perks
- [ ] **Builds crafting:** Develop a build crafting feature to allow users to customize the perks categories and builds
