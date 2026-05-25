import os

import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types


# Load environment variables from a local .env file.
# This helps beginners keep the API key separate from the code.
load_dotenv(dotenv_path=".env")


def get_api_key():
    """Read the Gemini API key from Streamlit secrets or the .env file."""
    try:
        return st.secrets["GEMINI_API_KEY"]
    except Exception:
        return "AIzaSyCyHWfMBT0ErWX1CC-wVpPy8tAcLF8J8B4"


def build_prompt(source_code, language):
    """Create a clear instruction prompt for Gemini."""
    return f"""
You are an AI coding mentor for a beginner Computer Science student.

Explain the following {language} code in simple language.

Please include:
1. What the code does
2. Step-by-step explanation
3. Important variables/functions
4. Final output, if it can be predicted
5. Any possible improvement

Keep the explanation beginner-friendly and avoid unnecessary jargon.

Code:
```{language}
{source_code}
```
"""


def explain_code(source_code, language):
    """Send the user's code to Gemini and return the explanation."""
    api_key = get_api_key()

    if not api_key:
        return "Please add your Gemini API key in a .env file or Streamlit secrets."

    client = genai.Client(api_key=api_key)
    prompt = build_prompt(source_code, language)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
            max_output_tokens=3000,
        ),
    )

    return response.text


st.set_page_config(
    page_title="AI Code Explainer Bot",
    page_icon=":computer:",
    layout="centered",
)

st.title("AI-Powered Code Explainer Bot")
st.write("Paste your code below and Gemini will explain it in simple language.")

language = st.selectbox(
    "Select programming language",
    ["Python", "C", "C++", "Java", "JavaScript", "Other"],
)

source_code = st.text_area(
    "Paste your source code here",
    height=280,
    placeholder="Example:\nfor i in range(5):\n    print(i)",
)

if st.button("Explain Code", type="primary"):
    if source_code.strip() == "":
        st.warning("Please paste some code before clicking the button.")
    else:
        with st.spinner("Gemini is explaining your code..."):
            try:
                explanation = explain_code(source_code, language)
                st.subheader("Explanation")
                st.markdown(explanation)
            except Exception as error:
                st.error("Something went wrong while calling Gemini API.")
                st.info(f"Error details: {error}")

st.divider()
st.caption("Mini project built with Python, Streamlit, and Gemini API.")
