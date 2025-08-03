import pandas as pd
import json
import logging

def check_json_integrity(input_path: str) -> None:
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            json.load(f)
        logging.info("'%s' is a valid JSON file.", input_path)

    except json.JSONDecodeError as e:
        logging.error("Invalid JSON in '%s':", input_path)
        logging.error("Error: %s", e.msg)
        logging.error("At line %s, column %s", e.lineno, e.colno)

    except FileNotFoundError:
        logging.error("Error: The file '%s' was not found.", input_path)

def create_dataframe(json_file):
    try:
        # The json is a dictionary of perks, where keys are the IDs.
        # We'll orient by index to get the IDs as a column.
        df = pd.DataFrame.from_dict(json_file, orient='index')
        df.reset_index(inplace=True)
        df.rename(columns={'index': 'id'}, inplace=True)
    except Exception as e:
        logging.error(f"Error: Can't parse json to DataFrame: {e}")
        return None
    return df


if __name__ == "__main__":
    JSON_FILE = "./scrapper/perks_data.json"
    OUTPUT_FILE = "./scrapper/perks_labels.csv"

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    check_json_integrity("./scrapper/perks_data.json")
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        json_file = json.load(f)
    
    perks_df = create_dataframe(json_file)

    if perks_df is not None:
        logging.info(f"DataFrame shape: {perks_df.shape}")
        if len(perks_df) > 100:
            logging.info(f"DataFrame has {len(perks_df)} rows. The check was successful.")
            
            # Create the final lookup table with 'id' and 'label'
            lookup_df = perks_df[['id', 'n']].rename(columns={'n': 'label'})
            
            lookup_df.to_csv(OUTPUT_FILE, index=False)
            logging.info(f"Successfully created lookup table at '{OUTPUT_FILE}'")
        else:
            logging.error(f"Error: DataFrame has only {len(perks_df)} rows, which is not more than 100.")