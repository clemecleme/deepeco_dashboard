import streamlit as st
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv('API_URL')

st.set_page_config(page_title="DeepEcology Mediator Dashboard", layout="centered")

def main():
    st.title("Mediator Dashboard")

    if st.button("Check Generation Status"):
        while True:
            response = requests.get(f"{API_URL}/generation_status")
            if response.status_code == 200:
                status = response.json()['status']
                if status == "not_started":
                    st.info("No generation in progress.")
                    break
                elif status == "started":
                    st.info("Experience generation in progress...")
                elif status == "completed":
                    st.success("Experience generation completed!")
                    break
            else:
                st.error("Error checking generation status")
                break
            time.sleep(2)  # Check every 2 seconds

if __name__ == "__main__":
    main()