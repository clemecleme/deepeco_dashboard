import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv('API_URL')

st.set_page_config(page_title="DeepEcology Mediator Dashboard", layout="centered")

def check_generation_status():
    response = requests.get(f"{API_URL}/generation_status")
    if response.status_code == 200:
        return response.json()['status']
    return "error"

def main():
    st.title("Deep Ecology - Mediator Dashboard")

    if st.button("Check State"):
        status = check_generation_status()
        
        if status == "not_started":
            st.info("No generation running.")
        elif status == "started":
            st.warning("Generation in progress...")
        elif status == "completed":
            st.success("Generation completed. Ready to launch experience!")
        else:
            st.error("Error checking generation status.")

if __name__ == "__main__":
    main()