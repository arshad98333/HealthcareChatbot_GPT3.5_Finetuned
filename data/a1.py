import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Retrieve the job details
job = client.fine_tuning.jobs.retrieve("ftjob-RIAIzAsuar98Q7AKQFFQIlWl")
print(job)