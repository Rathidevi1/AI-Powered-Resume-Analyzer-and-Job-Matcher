from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_match_score(resume_text, job_text):
    # Combine resume and job description to calculate TF-IDF
    corpus = [resume_text, job_text]
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
    # Calculate cosine similarity between resume and job description
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(similarity * 100, 2)
