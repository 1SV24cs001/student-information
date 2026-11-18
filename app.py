import streamlit as st
from groq import Groq
import os
st.set_page_config(
    page_title="AI Interview Assistant",
    page_icon="🫡",
    layout="centered"
)
st.title("AI Interview Assistant")
st.caption("A platform for AI-powered interview preparation")
try:
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        api_key = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=api_key)
except (KeyError, FileNotFoundError):
    st.error("API key is missing. Set GROQ_API_KEY or add GROQ_API_KEY to Streamlit secrets.")
    st.stop()
role = st.selectbox(
    "JOB TITLE",
    [
        "Software Engineer",
        "Senior Software Engineer",
        "Data Analyst",
        "Prompt Engineer",
        "DevOps Engineer",
        "Other"
    ]
)

if role == "Other":
    role = st.text_input("Enter your job title", " ")
model = st.selectbox(
    "MODEL",
    [
        "openai/gpt-oss-safeguard-20b",
        "openai/gpt-oss-120b"
    ]
)
difficulty = st.selectbox(
    "DIFFICULTY LEVEL",
    ["Beginner", "Intermediate", "Advanced"]
)
mode = st.radio(
    "ACTIVITY",
    [
        "Generate questions",
        "Generate code questions",
        "Evaluate answer",
        "Improve answers"
    ]
)
if mode == "Generate questions":
    count = st.slider("Number of questions", 1, 10, 5)
elif mode == "Generate code questions":
    topic = st.selectbox(
        "Topics",
        [
            "SQL", "AI/ML", "Python", "DSA",
            "C++/C", "Java", "Cyber Security", "ML"
        ]
    )
    count = st.slider("Number of questions", 1, 10, 5)
else:
    question = st.text_area("Enter interview question here")
    answer = st.text_area("Enter your answer", height=160)
if st.button("Submit"):
    st.info("Your inputs have been collected successfully.")
