import re
import string
import nltk

from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression


# -----------------------------------------
# Download NLTK Resources
# -----------------------------------------
nltk.download("punkt")
nltk.download("stopwords")

# -----------------------------------------
# NLP Objects
# -----------------------------------------
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()

# -----------------------------------------
# Text Preprocessing Function
# -----------------------------------------
def preprocess_text(text):

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Tokenize
    tokens = word_tokenize(text)

    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]

    # Apply stemming
    tokens = [stemmer.stem(word) for word in tokens]

    return " ".join(tokens)


# ===================================================
# SENTIMENT TRAINING DATA
# ===================================================

sentiment_reviews = [

    # Positive
    "Food was delicious",
    "Pizza was amazing",
    "Excellent delivery",
    "Burger tasted great",
    "Very happy with service",
    "Fresh food",
    "Loved the meal",
    "Fast delivery",
    "Amazing experience",
    "Highly recommend",

    # Negative
    "Food was cold",
    "Delivery was late",
    "Burger was burnt",
    "Very bad service",
    "Terrible experience",
    "Pizza tasted awful",
    "Order cancelled",
    "Food was stale",
    "App crashed",
    "Very disappointed"
]

sentiment_labels = [

    "Positive","Positive","Positive","Positive","Positive",
    "Positive","Positive","Positive","Positive","Positive",

    "Negative","Negative","Negative","Negative","Negative",
    "Negative","Negative","Negative","Negative","Negative"
]

# ===================================================
# ISSUE CATEGORY DATA
# ===================================================

category_reviews = [

    # Delivery
    "Delivery was late",
    "Order never arrived",
    "Delivery person rude",
    "Food arrived late",
    "Delivery delayed",

    # Food Quality
    "Food was cold",
    "Burger was burnt",
    "Pizza tasted bad",
    "Food stale",
    "Soup spilled",

    # App
    "App crashed",
    "Payment failed",
    "Unable to login",
    "App very slow",
    "Coupon not working",

    # General
    "Good experience",
    "Loved everything",
    "Amazing restaurant",
    "Nice service",
    "Satisfied with order"
]

category_labels = [

    "Delivery",
    "Delivery",
    "Delivery",
    "Delivery",
    "Delivery",

    "Food Quality",
    "Food Quality",
    "Food Quality",
    "Food Quality",
    "Food Quality",

    "App",
    "App",
    "App",
    "App",
    "App",

    "General",
    "General",
    "General",
    "General",
    "General"
]

# ===================================================
# Preprocess Training Data
# ===================================================

sentiment_reviews = [preprocess_text(review) for review in sentiment_reviews]
category_reviews = [preprocess_text(review) for review in category_reviews]

# ===================================================
# Sentiment Model
# TF-IDF + Logistic Regression
# ===================================================

sentiment_model = Pipeline([

    ("tfidf", TfidfVectorizer()),

    ("classifier", LogisticRegression(max_iter=1000))

])

sentiment_model.fit(sentiment_reviews, sentiment_labels)

# ===================================================
# Category Model
# TF-IDF + Naive Bayes
# ===================================================

category_model = Pipeline([

    ("tfidf", TfidfVectorizer()),

    ("classifier", MultinomialNB())

])

category_model.fit(category_reviews, category_labels)

# ===================================================
# Storage
# ===================================================

stored_reviews = []

# Store processed reviews separately
processed_reviews = []

print("Models trained successfully.")
print("Backend setup completed.")




# ===================================================
# Add New Review
# ===================================================

def add_review():

    review = input("\nEnter customer review: ").strip()

    if review == "":
        print("\nReview cannot be empty.")
        return

    # Preprocess the review
    processed = preprocess_text(review)

    # Store original review
    stored_reviews.append(review)

    # Store processed review
    processed_reviews.append(processed)

    print("\nReview added successfully.")

    print("\nOriginal Review:")
    print(review)

    print("\nProcessed Review:")
    print(processed)





# ===================================================
# Classify Review
# ===================================================

def classify_review():

    # Edge case
    if len(stored_reviews) < 3:
        print("\nNot enough reviews available.")
        print("Please add at least 3 reviews before classification.")
        return

    review = input("\nEnter a review to classify: ").strip()

    if review == "":
        print("\nReview cannot be empty.")
        return

    # Preprocess review
    processed = preprocess_text(review)

    # Predict sentiment
    sentiment = sentiment_model.predict([processed])[0]

    # Predict issue category
    category = category_model.predict([processed])[0]

    print("\n========== Classification Result ==========")
    print(f"Original Review : {review}")
    print(f"Processed Review: {processed}")
    print(f"Sentiment       : {sentiment}")
    print(f"Issue Category  : {category}")
    print("=" * 43)




# ===================================================
# Summary Report
# ===================================================

def summary_report():

    if len(stored_reviews) == 0:
        print("\nNo reviews available.")
        return

    sentiment_counter = Counter()
    category_counter = Counter()
    word_counter = Counter()

    # Process every stored review
    for review in processed_reviews:

        # Predict sentiment
        sentiment = sentiment_model.predict([review])[0]
        sentiment_counter[sentiment] += 1

        # Predict category
        category = category_model.predict([review])[0]
        category_counter[category] += 1

        # Count words
        words = review.split()
        word_counter.update(words)

    print("\n" + "=" * 50)
    print("          SUMMARY REPORT")
    print("=" * 50)

    print(f"\nTotal Reviews Added : {len(stored_reviews)}")

    print("\nSentiment Count")
    print("-" * 25)

    for sentiment, count in sentiment_counter.items():
        print(f"{sentiment:<15}: {count}")

    print("\nIssue Category Count")
    print("-" * 25)

    for category, count in category_counter.items():
        print(f"{category:<15}: {count}")

    print("\nTop 5 Frequent Content Words")
    print("-" * 30)

    for word, count in word_counter.most_common(5):
        print(f"{word:<15}: {count}")

    print("=" * 50)




# ===================================================
# Menu Function
# ===================================================

def show_menu():

    print("\n" + "=" * 55)
    print("     Food Delivery Review Intelligence System")
    print("=" * 55)
    print("1. Add New Review")
    print("2. Classify Review")
    print("3. View Summary Report")
    print("4. Exit")


# ===================================================
# Main Program
# ===================================================

while True:

    show_menu()

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
         add_review()

    elif choice == "2":
        classify_review()

    elif choice == "3":
        summary_report()

    elif choice == "4":
        print("\nThank you for using the Food Delivery Review Intelligence System.")
        print("Goodbye!")
        break

    else:
        print("\nInvalid choice! Please enter a number between 1 and 4.")