# Dead by Daylight: Meta-Analysis Engine

A data-driven project to statistically analyze the *Dead by Daylight* meta, identify the most effective perks, and discover mathematically proven "best builds".

## 📖 Overview

This repository houses a two-part system designed to move beyond anecdotal evidence and community discussion to provide a quantitative understanding of the game's meta. By systematically collecting and analyzing in-game statistics, this project aims to answer key questions:
* Which individual perks are the strongest?
* What are the most popular and effective perk combinations ("builds")?
* How does the meta shift over time with new patches and characters?
* Can we statistically prove what constitutes an "S-Tier" build?

---

## 🚀 Project Components

The engine is composed of two distinct applications that work in sequence.

### 1. The Scrapper
The foundation of the project is a powerful and robust data scraper.
* **Purpose:** To programmatically collect perk, character, and build statistics from the community-driven database on `Nightlight.gg`.
* **Technology:** Built in Python, using the `requests` library to interface with unofficial APIs and `pandas` for data structuring.
* **Output:** Generates clean, structured `.csv` files containing raw data on Survivor and Killer performance metrics, ready for analysis.

### 2. The Machine Learning Model
The analytical core of the project where the raw data is transformed into actionable insights.
* **Purpose:** To analyze the scraped data to uncover hidden patterns, evaluate perk viability, and generate recommendations.
* **Methodology:** This application will employ several ML techniques:
    * **Regression Analysis:** To predict a perk's "meta score" based on its characteristics.
    * **Clustering Algorithms (e.g., K-Means):** To automatically discover common "build archetypes" (e.g., 'Altruistic Healer', 'Gen-Slowing Menace').
    * **Feature Importance:** To identify which perks contribute most significantly to high win/escape rates.
* **Output:** Delivers insights on the most statistically effective strategies in *Dead by Daylight*.

---

## 📂 Project Structure

```
deadbystats/
├── .git/
├── .gitignore
├── dbd-env/
├── scrapper/
│   ├── .gitignore
│   ├── main.py
│   ├── create-lookup.py
│   ├── perks_data.json
│   ├── killer_perks.csv   (Generated)
│   ├── survivor_perks.csv (Generated)
│   └── perks_labels.csv   (Generated)
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup and Installation

Follow these steps to set up the scrapper application on your local machine.

**1. Clone the Repository:**
```bash
git clone [https://github.com/your-username/deadbystats.git](https://github.com/your-username/deadbystats.git)
cd deadbystats
```
**2. Create and Activate Virtual Environment:**
* **Create:**
    ```bash
    python -m venv dbd-env
    ```

* **Activate:**
    * On **Windows**: `dbd-env\Scripts\activate`
    * On **macOS & Linux**: `source dbd-env/bin/activate`

**3. Install Dependencies:**
This command installs all the necessary libraries for the project.
```bash
pip install -r requirements.txt
```

## 🏃 How to Run the Scrapper

With your virtual environment activated, run the main scraper script from the project's root directory:
```bash
python scrapper/main.py
```
The script will log its progress in the terminal. Upon successful completion, it will generate or update `survivor_perks.csv` and `killer_perks.csv` inside the `scrapper/` directory.

### Creating the Perk Lookup Table

The `perks_labels.csv` file, which maps perk IDs to their names, is included in this repository. It is generated from `perks_data.json`, which is a manually extracted file from `Nightlight.gg`.

If the game updates and you need to regenerate this file with new data, you must first manually obtain an updated `perks_data.json` file. Once you have this file, you can run the following command to create a new lookup table:

```bash
python scrapper/create-lookup.py
```

## 📈 Next Steps

* **ML Model Development:** Begin building the machine learning models to analyze the scraped data.
