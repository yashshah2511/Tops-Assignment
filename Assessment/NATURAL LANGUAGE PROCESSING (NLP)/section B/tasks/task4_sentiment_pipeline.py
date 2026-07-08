import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.feature_extraction.text import TfidfVectorizer
from task1_food_preprocessor import preprocess_text

# ------------------------------------
# Dataset (30 Reviews)
# ------------------------------------

reviews = [

    # Positive Reviews (15)
    "The pizza was delicious and fresh.",
    "Excellent delivery service.",
    "Food arrived hot and tasty.",
    "Amazing customer support.",
    "Loved the burger and fries.",
    "Fast delivery and good packaging.",
    "Very happy with the food quality.",
    "The app was easy to use.",
    "Fresh ingredients and great taste.",
    "Highly recommend this restaurant.",
    "The order arrived before time.",
    "Fantastic food and quick delivery.",
    "Everything was perfect.",
    "Very satisfied with my order.",
    "Great experience overall.",

    # Negative Reviews (15)
    "Food arrived cold.",
    "Very slow delivery.",
    "The burger tasted bad.",
    "App crashed during payment.",
    "The pizza was burnt.",
    "Order was cancelled unexpectedly.",
    "Packaging was damaged.",
    "Customer service was poor.",
    "Soup was spilled.",
    "Delivery person was rude.",
    "Food was stale.",
    "Payment failed several times.",
    "The app is very slow.",
    "Terrible experience.",
    "Never ordering again."
]

labels = [

    "Positive","Positive","Positive","Positive","Positive",
    "Positive","Positive","Positive","Positive","Positive",
    "Positive","Positive","Positive","Positive","Positive",

    "Negative","Negative","Negative","Negative","Negative",
    "Negative","Negative","Negative","Negative","Negative",
    "Negative","Negative","Negative","Negative","Negative"
]



# ------------------------------------
# Train Test Split
# ------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    reviews,
    labels,
    test_size=0.20,
    random_state=42,
    stratify=labels
)

# ------------------------------------
# Pipeline 1
# TF-IDF + Naive Bayes
# ------------------------------------

nb_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

# ------------------------------------
# Pipeline 2
# TF-IDF + Logistic Regression
# ------------------------------------

lr_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression(max_iter=1000))
])

# ------------------------------------
# Train Models
# ------------------------------------

nb_pipeline.fit(X_train, y_train)
lr_pipeline.fit(X_train, y_train)

# ------------------------------------
# Predictions
# ------------------------------------

nb_predictions = nb_pipeline.predict(X_test)
lr_predictions = lr_pipeline.predict(X_test)

# ------------------------------------
# Evaluation Function
# ------------------------------------

def evaluate(model_name, y_true, y_pred):

    return [
        model_name,
        accuracy_score(y_true, y_pred),
        precision_score(y_true, y_pred, pos_label="Positive"),
        recall_score(y_true, y_pred, pos_label="Positive"),
        f1_score(y_true, y_pred, pos_label="Positive")
    ]

results = [

    evaluate("Naive Bayes", y_test, nb_predictions),
    evaluate("Logistic Regression", y_test, lr_predictions)

]

# ------------------------------------
# Comparison Table
# ------------------------------------

comparison = pd.DataFrame(
    results,
    columns=[
        "Model",
        "Accuracy",
        "Precision",
        "Recall",
        "F1-Score"
    ]
)

print("\nModel Comparison\n")

print(comparison)

# ------------------------------------
# Deployment Recommendation
# ------------------------------------

# I would deploy Logistic Regression because it generally provides
# better overall accuracy and balanced performance for TF-IDF based
# sentiment classification.