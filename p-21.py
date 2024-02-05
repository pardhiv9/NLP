from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
documents = [
    "Natural language processing is a subfield of artificial intelligence.",
    "Machine learning techniques are widely used in natural language processing.",
    "Semantic analysis helps in understanding the meaning of words and sentences.",
    "TF-IDF is a common technique used in information retrieval and text mining.",
]

# Preprocess the documents (you may need to perform more advanced preprocessing based on your specific requirements)
preprocessed_documents = [doc.lower() for doc in documents]

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Compute TF-IDF features for the documents
tfidf_matrix = vectorizer.fit_transform(preprocessed_documents)

def rank_documents(query, documents, tfidf_matrix, vectorizer):
    # Preprocess the query
    preprocessed_query = query.lower()

    # Compute TF-IDF features for the query
    query_vector = vectorizer.transform([preprocessed_query])

    # Calculate cosine similarity between the query and the documents
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()

    # Rank documents based on similarity
    ranked_documents = sorted(enumerate(similarities), key=lambda x: x[1], reverse=True)

    # Print the ranked documents
    print("Ranked Documents:")
    for rank, (doc_index, similarity) in enumerate(ranked_documents):
        print(f"Rank {rank + 1}: Document {doc_index + 1} - Similarity: {similarity:.4f}")

# Example query
query = "What is natural language processing?"

# Rank documents based on the query
rank_documents(query, documents, tfidf_matrix, vectorizer)
