# app.py
import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# --- App Configuration ---
st.set_page_config(page_title="Medical SOAP Note Generator", page_icon="")
st.title(" Medical SOAP Note Generator")
st.caption("A fine-tuned chatbot to summarize medical transcripts into SOAP notes.")

# --- OpenAI Integration ---
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#  Updated fine-tuned model ID
FINE_TUNED_MODEL = "ft:gpt-3.5-turbo-0125:personal::CCSuLWS7"

# --- Chat Interface ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle new user input
if prompt := st.chat_input("Enter the medical transcript here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Stream the fine-tuned model's response
        stream = client.chat.completions.create(
            model=FINE_TUNED_MODEL,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )

        for chunk in stream:
            full_response += chunk.choices[0].delta.content or ""
            message_placeholder.markdown(full_response + "▌")  # Typing indicator

        message_placeholder.markdown(full_response)

    # Save assistant's response to session
    st.session_state.messages.append({"role": "assistant", "content": full_response})
