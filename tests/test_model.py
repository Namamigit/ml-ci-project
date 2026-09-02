from src.model import train_model

def test_model():
    model, accuracy = train_model()
    assert accuracy >= 0.90