import re
import string
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Download required resources
nltk.download("punkt")
nltk.download("stopwords")

# Stopwords and Stemmer
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()


# -----------------------------
# Text Preprocessing Function
# -----------------------------
def preprocess_text(text):
    text = text.lower()

    text = text.translate(str.maketrans("", "", string.punctuation))

    text = re.sub(r"\s+", " ", text).strip()

    tokens = word_tokenize(text)

    tokens = [word for word in tokens if word not in stop_words]

    tokens = [stemmer.stem(word) for word in tokens]

    return " ".join(tokens)


# -----------------------------
# Training Dataset
# -----------------------------
reviews = [
    "The food was delicious",
    "Amazing pizza and fast delivery",
    "Loved the burger",
    "Excellent service",
    "Very tasty meal",
    "Food arrived cold",
    "Very slow delivery",
    "Burger tasted awful",
    "Terrible experience",
    "I hate this food"
]

labels = [
    "Positive",
    "Positive",
    "Positive",
    "Positive",
    "Positive",
    "Negative",
    "Negative",
    "Negative",
    "Negative",
    "Negative"
]

# Preprocess Reviews
processed_reviews = [preprocess_text(review) for review in reviews]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(processed_reviews)

y = labels

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Logistic Regression Model
model = LogisticRegression()

model.fit(X_train, y_train)

# Accuracy
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", accuracy)

# -----------------------------
# Predict New Reviews
# -----------------------------

print("\nEnter 3 new reviews:\n")

for i in range(3):

    review = input(f"Review {i+1}: ")

    processed = preprocess_text(review)

    vector = vectorizer.transform([processed])

    prediction = model.predict(vector)[0]

    print("Predicted Sentiment:", prediction)
    print("-" * 40)