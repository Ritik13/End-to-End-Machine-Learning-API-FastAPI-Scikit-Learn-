import joblib
from pathlib import Path


def load_model(model_name : str):
    """
    Load a saved ML model and its vectorizer.
    :param model_name: name of the model files (without _model.joblib suffix)
    :return: (model, vectorizer)
    """
    base_path = Path("ml_pipeline/models")
    model_path = base_path / f"{model_name}_pipeline.joblib"

    if not model_path.exists():
        raise FileNotFoundError(f"Model  for '{model_name}' not found.")

    model = joblib.load(model_path)
    return model
