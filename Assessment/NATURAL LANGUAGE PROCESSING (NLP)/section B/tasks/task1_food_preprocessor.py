import re
import string
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


# Initialize stopwords and stemmer
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()


def preprocess_text(review):
    """
    Preprocesses a food delivery review.
    Steps:
    1. Lowercase conversion
    2. Remove punctuation
    3. Remove extra whitespace
    4. Tokenization
    5. Stopword removal
    6. Stemming
    """

    # Convert to lowercase
    review = review.lower()

    # Remove punctuation
    review = review.translate(str.maketrans('', '', string.punctuation))

    # Remove extra whitespace
    review = re.sub(r'\s+', ' ', review).strip()

    # Tokenize
    tokens = word_tokenize(review)

    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]

    # Apply stemming
    tokens = [stemmer.stem(word) for word in tokens]

    # Return processed string
    return " ".join(tokens)


# -------------------------------
# Test the function
# -------------------------------

reviews = [
    "The Pizza was AMAZING!!! Delivery was super fast.",
    "Burger arrived cold and soggy. Very disappointed.",
    "Food was okay, but the delivery took too long."
]

print("Processed Reviews:\n")

for i, review in enumerate(reviews, start=1):
    print(f"Review {i}")
    print("Original :", review)
    print("Processed:", preprocess_text(review))
    print("-" * 60)