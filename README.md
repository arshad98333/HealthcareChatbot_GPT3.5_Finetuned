## Project Vision & Overview

**Live Demo Deployment:**  
[Access the Application Here](https://arshad98333-healthcarechatbot-gpt3-5-finetuned-app-gqbbns.streamlit.app/)

----------------------------------------------------------------------------------------------------------------


In modern healthcare, clinicians spend a significant amount of time on administrative tasks, particularly on documenting patient encounters. This project addresses this challenge by leveraging a large language model (LLM) to automate the creation of SOAP (Subjective, Objective, Assessment, Plan) notes from unstructured, conversational medical transcripts.

As an AI engineering project, the focus is not just on the model's output but on the entire end-to-end MLOps lifecycle:

- **Data Curation & Privacy**: Starting with raw data and implementing a crucial PII (Personally Identifiable Information) anonymization step to ensure patient confidentiality.
- **Model Specialization**: Finetuning a powerful base model (like GPT-3.5-Turbo) on a specialized dataset to teach it the specific task of medical summarization.
- **Application Development**: Building an intuitive, ChatGPT-like user interface using Streamlit for seamless interaction.
- **Deployment**: Packaging the application for easy, scalable deployment on a cloud platform (Streamlit Community Cloud).

This repository serves as a complete blueprint for building and deploying specialized, privacy-conscious AI applications.

## Features

- **Medical Specialization**: The model is finetuned to understand medical terminology and the specific structure of a SOAP note.
- **PII Anonymization Pipeline**: A preliminary script to identify and remove sensitive patient data (e.g., age, gender) before it is processed by the AI model.
- **End-to-End Finetuning Workflow**: Includes scripts to prepare data, launch, and monitor an OpenAI finetuning job.
- **Interactive UI**: A user-friendly, real-time chat interface built with Streamlit, providing an experience similar to ChatGPT.
- **Cloud-Ready**: Designed for easy deployment to Streamlit Community Cloud, making the application accessible from anywhere.
- **Reproducible Environment**: A requirements.txt file ensures that the development and deployment environments are consistent.

# System Architecture

## Tech Stack

| Technology | Description |
|------------|-------------|
| Python     | Core programming language for all scripts and the application. |
| OpenAI API | Used for the finetuning process and for model inference. |
| Pandas     | For data manipulation and processing of the CSV files. |
| Streamlit  | For building and serving the interactive web application UI. |
| Dotenv     | For managing environment variables and API keys securely. |

## Local Installation and Setup

Follow these steps to get the project running on your local machine.

### Prerequisites
- Python 3.9+
- Git for cloning the repository
- An OpenAI API Key with access to finetuning

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-github-username/finetuned-chatbot.git
cd finetuned-chatbot
```

### Step 2: Set Up a Virtual Environment
It is a best practice to create a virtual environment to isolate project dependencies.

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```
You will see `(venv)` at the beginning of your terminal prompt if it's active.

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
The OpenAI API key is sensitive and should not be hardcoded. Create a new file named `.env` in the root of the project directory and add your API key:

```text
OPENAI_API_KEY="your-api-key-here"
```

This file is listed in `.gitignore` and will not be committed to your repository.

## Running the Project: The Finetuning Workflow

This is a multi-step process. Run these commands from the root of the project directory (`finetuned-chatbot`).

### Step 1: Anonymize the Raw Data
```bash
python scripts/1_anonymize_data.py
```
This script reads the raw CSV, removes basic PII, and saves a new `anonymized_data.csv` file.

### Step 2: Prepare Data for Finetuning
```bash
python scripts/2_prepare_finetuning_data.py
```
This converts the anonymized data into the JSONL format required by OpenAI.

### Step 3: Launch the Finetuning Job
```bash
python scripts/3_run_finetuning.py
```
This uploads the data and starts the finetuning process. This may take time and will incur costs on your OpenAI account.

After running, you will get a Job ID. You need to wait for the job to complete. You can monitor its status on the OpenAI Finetuning Dashboard.

### Step 4: Run the Streamlit App Locally
Once your finetuning job succeeds, copy the new model ID from the dashboard (e.g., `ft:gpt-3.5-turbo...`). Open `app.py` and replace the placeholder with your model ID:

```python
# in app.py
FINE_TUNED_MODEL = "paste-your-new-model-id-here"
```

Save the file and run the app:

```bash
streamlit run app.py
```

Your browser will open to `http://localhost:8501` with the running application.

## Deployment to Streamlit Community Cloud

Deploying your app makes it accessible to anyone with a web browser.

### Step 1: Push to GitHub
```bash
git add .
git commit -m "feat: complete finetuning and configure app"
git push origin main
```

### Step 2: Deploy on Streamlit
1. Go to [Streamlit Cloud](https://share.streamlit.io) and sign in with your GitHub account.
2. Click "New app" and select your repository.
3. In the deployment settings, go to **Advanced settings**.
4. Navigate to the **Secrets** section. This is where you will store your API key securely. Add your secret in the following format:
   ```toml
   OPENAI_API_KEY="your-api-key-here"
   ```
5. Click **Deploy**. Streamlit will handle the rest. After a few moments, your app will be live.

## Project Structure

```code
/finetuned-chatbot
├── .env                  # Stores API keys (Not committed)
├── .gitignore            # Files for Git to ignore
├── README.md             # This file
├── app.py                # Main Streamlit application
├── requirements.txt      # Project dependencies
│
├── data/
│   ├── synthetic_data_summarize_soap.csv  # Raw input data
│   ├── anonymized_data.csv                # Data after PII removal
│   └── training_data.jsonl                # Formatted for finetuning
│
└── scripts/
    ├── 1_anonymize_data.py          # PII removal script
    ├── 2_prepare_finetuning_data.py # Data formatting script
    └── 3_run_finetuning.py          # Finetuning job initiator
```

## Contributing

Contributions are welcome. If you have suggestions for improving the PII detection, adding new features, or enhancing the model's performance, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

