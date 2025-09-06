# scripts/3_run_finetuning.py
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Upload the training data
    file = client.files.create(
        file=open("data/training_data.jsonl", "rb"),
        purpose="fine-tune"
    )
    print(f"File uploaded with ID: {file.id}")

    # Create a fine-tuning job
    job = client.fine_tuning.jobs.create(
        training_file=file.id,
        model="gpt-3.5-turbo"
    )
    print(f"Fine-tuning job created with ID: {job.id}")

if __name__ == "__main__":
    main()