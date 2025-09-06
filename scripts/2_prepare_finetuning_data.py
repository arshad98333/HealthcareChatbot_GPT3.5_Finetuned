# scripts/2_prepare_finetuning_data.py
import pandas as pd
import json
import os

def create_finetuning_data(row):
    return {
        "messages": [
            {"role": "system", "content": "You are a helpful medical assistant that summarizes raw medical transcripts into a SOAP note format."},
            {"role": "user", "content": str(row.get('raw_transcript', ''))},
            {"role": "assistant", "content": str(row.get('formatted_soap_note', ''))}
        ]
    }

def main():
    # --- START OF CHANGES ---
    script_dir = os.path.dirname(__file__)
    project_root = os.path.dirname(script_dir)
    input_csv_path = os.path.join(project_root, 'data', 'anonymized_data.csv')
    output_jsonl_path = os.path.join(project_root, 'data', 'training_data.jsonl')
    
    print(f"Reading anonymized data from: {input_csv_path}")
    # --- END OF CHANGES ---

    try:
        df = pd.read_csv(input_csv_path)
        with open(output_jsonl_path, 'w') as f:
            for _, row in df.iterrows():
                f.write(json.dumps(create_finetuning_data(row)) + '\n')
        print(f"Fine-tuning data prepared successfully. Saved to: {output_jsonl_path}")

    except FileNotFoundError:
        print(f"Error: The file was not found: {input_csv_path}")
        print("Please make sure you have run the '1_anonymize_data.py' script first.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()