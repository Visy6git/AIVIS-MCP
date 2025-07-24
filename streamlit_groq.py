import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("💬 Ask LLaMA 3 (Groq)")

# User input
user_input = st.text_area("Enter your question:", height=100)

if st.button("Submit") and user_input.strip():
    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": user_input}],
                model="llama-3.3-70b-versatile"
            )
            st.markdown("### 🧠 LLaMA 3's Answer:")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
