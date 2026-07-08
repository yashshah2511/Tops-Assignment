from task1_food_preprocessor import preprocess_text

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix

# ------------------------------------
# Complaint Dataset (24 Samples)
# ------------------------------------

complaints = [

    # Delivery Issues (8)
    "My order arrived very late.",
    "Delivery person never came.",
    "Food was delivered to the wrong address.",
    "My order is still not delivered.",
    "Delivery took more than two hours.",
    "The rider cancelled my delivery.",
    "Food arrived much later than expected.",
    "Delivery was extremely slow.",

    # Food Quality Issues (8)
    "Pizza was cold.",
    "Burger was burnt.",
    "Food tasted stale.",
    "The meal was undercooked.",
    "Soup was spilled inside the bag.",
    "Food quality was terrible.",
    "The fries were soggy.",
    "My sandwich was not fresh.",

    # App Issues (8)
    "The app keeps crashing.",
    "Payment failed multiple times.",
    "Unable to login to the application.",
    "Order button is not working.",
    "App freezes while placing order.",
    "Coupon code is not applying.",
    "Unable to track my order in the app.",
    "Application is running very slowly."
]

labels = [

    # Delivery
    "Delivery","Delivery","Delivery","Delivery",
    "Delivery","Delivery","Delivery","Delivery",

    # Food Quality
    "Food Quality","Food Quality","Food Quality","Food Quality",
    "Food Quality","Food Quality","Food Quality","Food Quality",

    # App
    "App","App","App","App",
    "App","App","App","App"
]

# ------------------------------------
# Preprocessing using Task 1 function
# ------------------------------------

processed_complaints = [preprocess_text(text) for text in complaints]

# ------------------------------------
# TF-IDF Vectorization
# ------------------------------------

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(processed_complaints)

y = labels

# ------------------------------------
# Train Test Split (80-20)
# ------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ------------------------------------
# Train Naive Bayes Model
# ------------------------------------

model = MultinomialNB()

model.fit(X_train, y_train)

# ------------------------------------
# Prediction
# ------------------------------------

predictions = model.predict(X_test)

# ------------------------------------
# Results
# ------------------------------------

print("\nClassification Report\n")

print(classification_report(y_test, predictions))

print("\nConfusion Matrix\n")

print(confusion_matrix(y_test, predictions))

print("\nPreprocessed Complaints:\n")
