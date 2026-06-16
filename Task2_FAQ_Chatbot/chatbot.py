import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import re
import string

from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

from sklearn.metrics.pairwise import cosine_similarity

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

def load_dataset():
    df = pd.read_csv("dataset/final_healthcare_faq.csv")
    df["preprocessed_question"] = df["question"].apply(preprocess_text)
    return df

df = load_dataset()

vectorizer = TfidfVectorizer(
    stop_words="english",
    lowercase=True,
    ngram_range=(1, 2)
)

tfidf_matrix = vectorizer.fit_transform(df["preprocessed_question"])

def preprocess_query(text):
    processed = preprocess_text(text)
    query_vector = vectorizer.transform([processed])
    return processed, query_vector

def get_response(user_query, threshold=0.50):
    processed_query = preprocess_text(user_query)
    query_vector = vectorizer.transform([processed_query])

    similarities = cosine_similarity(query_vector, tfidf_matrix)

    best_match_idx = similarities.argmax()
    best_score = similarities[0, best_match_idx]

    if best_score >= threshold:
        return {
            "question": df.loc[best_match_idx, "question"],
            "answer": df.loc[best_match_idx, "answer"],
            "score": best_score,
            "found": True,
        }
    else:
        return {
            "question": None,
            "answer": (
                "Sorry, I couldn't find a relevant healthcare FAQ. "
                "Please try rephrasing your question or ask using different medical terms."
            ),
            "score": best_score,
            "found": False,
        }
        
