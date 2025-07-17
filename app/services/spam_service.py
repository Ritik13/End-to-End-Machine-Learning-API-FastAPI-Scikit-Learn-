import joblib
pipeline = joblib.load("ml_pipeline/models/spam_detector_pipeline.joblib")
import pandas as pd


def predict_spam(review: str, threshold: float = 0.6):
    if not review:
        raise ValueError("Review text cannot be empty or None")

    input_df = pd.DataFrame({"text_": [review]})

    # Get spam probability
    spam_prob = pipeline.predict_proba(input_df)[0][1]

    # Apply custom threshold
    is_spam = spam_prob >= threshold

    return {
        "is_spam": bool(is_spam),
        "confidence": float(spam_prob)
    }
