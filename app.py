import streamlit as st
from openai import OpenAI


st.set_page_config(
    page_title="Amelia AI",
    page_icon="🤖",
    layout="centered"
)


api_key = st.secrets["OPENROUTER_API_KEY"]


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)


st.title("🤖 Amelia AI")
st.caption("Smart AI Assistant by Amelia")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


prompt = st.chat_input("Tulis pertanyaan kamu...")


if prompt:

    
    st.chat_message("user").markdown(prompt)

    
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    try:

        
        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",

            messages=[
                {
                    "role": "system",
                    "content": """
                    Kamu adalah Amelia AI.

                    Kamu adalah AI assistant yang:
                    - pintar
                    - ramah
                    - suportif
                    - modern
                    - interaktif
                    - natural seperti manusia

                    Gaya bicara:
                    - santai tapi tetap sopan
                    - mudah dipahami
                    - hangat dan friendly
                    - tidak terlalu formal
                    - suka membantu pengguna belajar

                    Tugas kamu:
                    - menjawab pertanyaan
                    - membantu belajar
                    - memberikan penjelasan
                    - memberi motivasi
                    - membantu brainstorming
                    - membantu produktivitas

                    Jika ditanya tentang berita terbaru,
                    jelaskan bahwa informasi real-time
                    mungkin terbatas.
                    """
                }
            ] + st.session_state.messages
        )

        
        reply = response.choices[0].message.content

        
        with st.chat_message("assistant"):
            st.markdown(reply)

        
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

    except Exception as e:
        st.error(f"Error: {e}")