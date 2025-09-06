# scripts/1_anonymize_data.py
import pandas as pd
import re
import os

def anonymize_text(text):
    # This is a basic example. For real-world use, a more robust solution is needed.
    # It removes age and gender information using regular expressions.
    if isinstance(text, str):
        text = re.sub(r'Age is \d+,', 'Age has been removed,', text)
        text = re.sub(r'gender (male|female)', 'gender has been removed', text)
    return text

def main():
    # --- START OF CHANGES ---
    # Get the absolute path of the current script
    script_dir = os.path.dirname(__file__)
    # Go up one level to the project root (from /scripts to /finetuned-chatbot)
    project_root = os.path.dirname(script_dir)
    # Construct the full path to the data files
    input_csv_path = os.path.join(project_root, 'data', 'synthetic_data_summarize_soap.csv')
    output_csv_path = os.path.join(project_root, 'data', 'anonymized_data.csv')
    
    print(f"Attempting to read data from: {input_csv_path}")
    # --- END OF CHANGES ---

    try:
        df = pd.read_csv(input_csv_path)
        # Ensure the 'raw_transcript' column exists before applying the function
        if 'raw_transcript' in df.columns:
            df['raw_transcript'] = df['raw_transcript'].apply(anonymize_text)
            df.to_csv(output_csv_path, index=False)
            print(f"Anonymization complete. Cleaned data saved to: {output_csv_path}")
        else:
            print("Error: 'raw_transcript' column not found in the CSV file.")

    except FileNotFoundError:
        print(f"Error: The file was not found at the specified path: {input_csv_path}")
        print("Please ensure the file exists and the path is correct in your project structure.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()