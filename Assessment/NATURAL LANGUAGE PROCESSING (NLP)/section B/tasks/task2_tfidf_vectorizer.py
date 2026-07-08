import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# -----------------------------
# Food Delivery Review Corpus
# -----------------------------
reviews = [
    "The pizza was delicious and delivered on time.",
    "Burger arrived cold and tasted bad.",
    "Fast delivery and excellent customer service.",
    "The food was average but the packaging was good.",
    "My order was delayed by one hour.",
    "Fresh pasta with amazing taste and quality.",
    "The app was easy to use and ordering was simple.",
    "Terrible delivery experience and cold food."
]

# -----------------------------
# TF-IDF Vectorization
# -----------------------------
vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(reviews)

# Feature names
feature_names = vectorizer.get_feature_names_out()

# Convert to DataFrame
df = pd.DataFrame(
    tfidf_matrix.toarray(),
    columns=feature_names,
    index=[f"Review {i+1}" for i in range(len(reviews))]
)

# -----------------------------
# Display TF-IDF Matrix
# -----------------------------
print("\nTF-IDF Matrix:\n")
print(df)

# -----------------------------
# Top 3 Words for Each Review
# -----------------------------
print("\nTop 3 TF-IDF Words Per Review:\n")

for i, row in enumerate(tfidf_matrix.toarray()):

    word_scores = list(zip(feature_names, row))

    # Sort by score (highest first)
    word_scores = sorted(word_scores, key=lambda x: x[1], reverse=True)

    print(f"Review {i+1}")

    count = 0
    for word, score in word_scores:
        if score > 0:
            print(f"{word:<15} {score:.3f}")
            count += 1
            if count == 3:
                break

    print("-" * 40)