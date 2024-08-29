import streamlit as st
import requests
import os
import time
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

    status_placeholder = st.empty()
    
    while True:
        status = check_generation_status()
        
        if status == "started":
            status_placeholder.warning("Generation in progress...")
        elif status == "completed":
            status_placeholder.success("Generation completed. Ready to launch experience!")
        elif status == "not_started":
            status_placeholder.info("No generation running")
        else:
            status_placeholder.error("Error checking generation status.")
        
        # time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    main()