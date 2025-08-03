import requests
import pandas as pd
import logging
import json

def scrape_and_process_data(url: str, headers: dict, data_key: str) -> pd.DataFrame | None:
    """
    Scrapes data, navigates the JSON, and extracts a specific dataset.

    Args:
        url (str): The API endpoint URL.
        headers (dict): The request headers.
        data_key (str): The key for the data to extract (e.g., 'top_survivor_perks').

    Returns:
        pd.DataFrame | None: A DataFrame of the requested data, or None on error.
    """
    logging.info("Requesting data from %s", url)
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        logging.info("Data received successfully!")
        data = response.json()
    except requests.exceptions.RequestException:
        logging.error("Request failed.", exc_info=True)
        return None
    except json.JSONDecodeError:
        logging.error("Failed to decode JSON from response.", exc_info=True)
        return None

    try:
        target_data_list = data['data'][data_key]
        
        if not isinstance(target_data_list, list):
            logging.error("Data for key '%s' is not a list.", data_key)
            return None

        df = pd.DataFrame(target_data_list)
        logging.info("Successfully processed %d items for key '%s'.", len(df), data_key)
        return df

    except (KeyError, TypeError):
        logging.error("Could not find the key '%s' in the JSON structure.", data_key, exc_info=True)
        return None


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    API_URL = "https://nightlight.gg/api/v1/stats/global/perks_and_builds"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }

    logging.info("--- Starting Scraper ---")

    # Load the lookup table
    try:
        lookup_df = pd.read_csv(LOOKUP_FILE)
        logging.info("Successfully loaded lookup table from '%s'.", LOOKUP_FILE)
    except FileNotFoundError:
        logging.error("Error: The lookup file '%s' was not found.", LOOKUP_FILE)
        lookup_df = None

    survivor_perks_df = scrape_and_process_data(url=API_URL, headers=HEADERS, data_key="top_survivor_perks")
    if survivor_perks_df is not None and lookup_df is not None:
        survivor_perks_df = pd.merge(survivor_perks_df, lookup_df, left_on='perk_id', right_on='id', how='left')
        survivor_perks_df.drop(columns=['id'], inplace=True)
        survivor_perks_df.to_csv("./scrapper/survivor_perks.csv", index=False)
        logging.info("Saved survivor perks to survivor_perks.csv")

    killer_perks_df = scrape_and_process_data(url=API_URL, headers=HEADERS, data_key="top_killer_perks")
    if killer_perks_df is not None and lookup_df is not None:
        killer_perks_df = pd.merge(killer_perks_df, lookup_df, left_on='perk_id', right_on='id', how='left')
        killer_perks_df.drop(columns=['id'], inplace=True)
        killer_perks_df.to_csv("./scrapper/killer_perks.csv", index=False)
        logging.info("Saved killer perks to killer_perks.csv")
    
    logging.info("--- Scraper Finished ---")