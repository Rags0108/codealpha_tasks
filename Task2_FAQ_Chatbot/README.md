# 🏥 Healthcare FAQ Chatbot

## 📌 Project Overview

The Healthcare FAQ Chatbot is an AI-powered question-answering system developed using Python, Natural Language Processing (NLP), TF-IDF Vectorization, Cosine Similarity, and Streamlit.

The chatbot retrieves the most relevant answer from a healthcare FAQ dataset by comparing user queries with stored healthcare-related questions. It provides quick and accurate responses for common medical and mental health questions.

This project was developed as part of the **CodeAlpha Artificial Intelligence Internship Program**.

---

## 🎯 Features

* Healthcare FAQ Question Answering
* NLP-based Text Preprocessing
* TF-IDF Vectorization
* Cosine Similarity Matching
* Streamlit Web Interface
* Confidence Score Display
* Example Questions Sidebar
* Fast Response Retrieval
* User-Friendly Interface

---

## 🛠️ Technologies Used

* Python 3.12
* Pandas
* NumPy
* NLTK
* Scikit-learn
* Streamlit

---

## 📂 Project Structure

```text
Task2_FAQ_Chatbot/
│
├── dataset/
│   ├── final_healthcare_faq.csv
│   ├── medquad.csv
│   └── Mental_Health_FAQ.csv
│
├── app.py
├── chatbot.py
├── task2.ipynb
├── requirements.txt
├── README.md
│
└── __pycache__/
```

---

## ⚙️ Working Methodology

### 1. Data Collection

Two healthcare datasets were collected:

* MedQuAD Dataset
* Mental Health FAQ Dataset

### 2. Data Cleaning

* Removed duplicate questions
* Removed null values
* Standardized column names
* Merged datasets into a single healthcare FAQ dataset

### 3. Text Preprocessing

The following NLP preprocessing techniques were applied:

* Lowercase conversion
* Punctuation removal
* Number removal
* Stopword removal

### 4. Feature Extraction

TF-IDF Vectorization was used to convert text into numerical vectors.

### 5. Similarity Calculation

Cosine Similarity was used to compare user questions with stored FAQ questions.

### 6. Response Retrieval

The chatbot retrieves the most relevant answer based on the highest similarity score.

---

## 🔄 Workflow

```text
User Question
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Cosine Similarity
      │
      ▼
Best Matching Question
      │
      ▼
Answer Retrieval
      │
      ▼
Display Response
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Task2_FAQ_Chatbot.git

cd Task2_FAQ_Chatbot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 💡 Example Questions

* What causes mental illness?
* What are some of the warning signs of mental illness?
* What is glaucoma?
* What causes glaucoma?
* What are the symptoms of glaucoma?
* What is stomach cancer?

---

## 📊 Model Details

### Text Vectorization

```python
TfidfVectorizer(
    stop_words="english",
    lowercase=True,
    ngram_range=(1, 2)
)
```

### Similarity Metric

```python
Cosine Similarity
```

### Threshold

```python
0.50
```

---

## 📸 Output Screenshots

### Main Interface

(Add Screenshot Here)

### Question Matching

(Add Screenshot Here)

### Answer Retrieval

(Add Screenshot Here)

---

## 🔮 Future Improvements

* Semantic Search using Sentence Transformers
* BERT-based Question Answering
* Medical Knowledge Graph Integration
* Voice-based Interaction
* Multi-language Support
* Healthcare RAG Chatbot

---

## 👨‍💻 by

**Ragavan S**

* GitHub: https://github.com/Rags0108
* LinkedIn: https://www.linkedin.com/in/s-ragavan/

---

## 📜 License

This project is developed for educational and internship purposes under the CodeAlpha Artificial Intelligence Internship Program.

---

## ⭐ Acknowledgement

Thanks to CodeAlpha for providing the opportunity to work on practical Artificial Intelligence and NLP projects.
