import streamlit as st
from utils import extract_text_from_pdf, match_resume_with_job
import spacy
import os

st.title("AI-Powered Resume Analyzer and Job Matcher")

# Upload resume
uploaded_file = st.file_uploader("Upload your resume (PDF format)", type=["pdf"])

# Load job description from file or text area
job_file = "sample_jobs/data_scientist.txt"
job_text = ""

if os.path.exists(job_file):
    job_text = open(job_file, "r", encoding="utf-8").read()
    st.success("Loaded job description from sample_jobs/data_scientist.txt")
else:
    st.warning("Job description file not found. Please enter it manually below.")
    job_text = st.text_area("Enter job description manually", height=200)

# Main logic
if uploaded_file is not None and job_text.strip() != "":
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    resume_text = extract_text_from_pdf("temp.pdf")

    st.subheader("Extracted Resume Text")
    st.text(resume_text[:1000] + "...")

    score, keywords = match_resume_with_job(resume_text, job_text)

    st.subheader("Match Score")
    st.write(f"{score:.2f}%")

    st.subheader("Matched Keywords")
    st.write(", ".join(keywords))

elif uploaded_file is None:
    st.info("Please upload a PDF resume to continue.")

elif job_text.strip() == "":
    st.info("Please provide a job description to compare.")
