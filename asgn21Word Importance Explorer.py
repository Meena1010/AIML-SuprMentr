from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    "Machine learning is powerful",
    "AI and machine learning are related",
    "Data science uses machine learning",
    "Deep learning is a part of AI",
    "AI is transforming the world"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)

feature_names = vectorizer.get_feature_names_out()

for i, doc in enumerate(X):
    scores = zip(feature_names, doc.toarray()[0])
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    print(f"Doc {i+1} Top Words:", sorted_scores[:3])
 #TF-IDF highlights important words by reducing common words and emphasizing unique terms in each document.   
    