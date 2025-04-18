import spacy
import re

# Load spaCy model for text processing
nlp = spacy.load("en_core_web_sm")

def parse_resume(text):
    doc = nlp(text)

    skills_keywords = ['python', 'java', 'sql', 'machine learning', 'data analysis', 'nlp', 'flask', 'excel']
    found_skills = [word for word in skills_keywords if word.lower() in text.lower()]

    education = []
    experience = []

    for sent in doc.sents:
        if "university" in sent.text.lower() or "college" in sent.text.lower():
            education.append(sent.text)
        if "experience" in sent.text.lower() or "worked" in sent.text.lower():
            experience.append(sent.text)

    return {
        "skills": list(set(found_skills)),
        "education": education,
        "experience": experience
    }
