import fitz  # PyMuPDF
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def match_resume_with_job(resume_text, job_text):
    resume_doc = nlp(resume_text.lower())
    job_doc = nlp(job_text.lower())

    resume_tokens = set([token.lemma_ for token in resume_doc if token.is_alpha and not token.is_stop])
    job_tokens = set([token.lemma_ for token in job_doc if token.is_alpha and not token.is_stop])

    common_tokens = resume_tokens & job_tokens
    match_score = len(common_tokens) / len(job_tokens) * 100 if job_tokens else 0

    return match_score, list(common_tokens)
