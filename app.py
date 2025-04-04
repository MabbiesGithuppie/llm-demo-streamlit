import streamlit as st
import openai
import os

# Maak een OpenAI client aan met je API key
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="LLM Live Demo", layout="centered")

st.title("🤖 LLM Live Demo")
st.write("Voer een prompt in en kies een schrijfstijl.")

prompt = st.text_area("✍️ Prompt:", height=150)

style = st.selectbox("🖋️ Kies schrijfstijl:", ["Standaard", "Formeel", "Casual", "Shakespeare", "Voor een kind"])

def format_prompt(prompt, style):
    if style == "Formeel":
        return f"Herschrijf de volgende tekst op formele toon:\n{prompt}"
    elif style == "Casual":
        return f"Herschrijf de volgende tekst op informele toon:\n{prompt}"
    elif style == "Shakespeare":
        return f"Herschrijf deze tekst in de stijl van Shakespeare:\n{prompt}"
    elif style == "Voor een kind":
        return f"Leg dit uit aan een kind van 6 jaar:\n{prompt}"
    return prompt

if st.button("✨ Genereer Tekst"):
    if prompt.strip() == "":
        st.warning("Voer eerst een prompt in.")
    else:
        with st.spinner("Even denken..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo
