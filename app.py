import streamlit as st
from openai import OpenAI

api_key = st.secrets["OPENROUTER_API_KEY"]

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

st.title("AI Chatbot Amelia")

prompt = st.text_input("Tulis pertanyaan kamu")

if prompt:
    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        st.write(response.choices[0].message.content)

    except Exception as e:
        st.error(f"Error: {e}")