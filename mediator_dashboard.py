import streamlit as st
import requests
import time
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
    st.title("Mediator Dashboard")

    if 'generation_started' not in st.session_state:
        st.session_state.generation_started = False

    if not st.session_state.generation_started:
        if st.button("Start Generation"):
            st.session_state.generation_started = True
            st.rerun()

    if st.session_state.generation_started:
        status_placeholder = st.empty()
        progress_bar = st.progress(0)
        
        while True:
            status = check_generation_status()
            
            if status == "not_started":
                status_placeholder.info("Generation not started yet.")
                break
            elif status == "started":
                for i in range(100):
                    time.sleep(1)
                    progress_bar.progress(i + 1)
                    status_placeholder.info(f"Experience generation in progress... {i+1}%")
                    
                    # Check status every 10%
                    if (i + 1) % 10 == 0:
                        current_status = check_generation_status()
                        if current_status == "completed":
                            status_placeholder.success("Experience generation completed!")
                            st.session_state.generation_started = False
                            return
                        elif current_status == "error":
                            status_placeholder.error("Error in generation process.")
                            st.session_state.generation_started = False
                            return
            elif status == "completed":
                status_placeholder.success("Experience generation completed!")
                st.session_state.generation_started = False
                break
            elif status == "error":
                status_placeholder.error("Error in generation process.")
                st.session_state.generation_started = False
                break
            
            time.sleep(2)  # Check every 2 seconds

    if not st.session_state.generation_started:
        if st.button("Reset"):
            st.session_state.generation_started = False
            st.rerun()

if __name__ == "__main__":
    main()