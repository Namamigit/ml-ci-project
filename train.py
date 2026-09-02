from src.model import train_model


model, accuracy = train_model()

print("ML Model Training Completed")
print(f"Accuracy: {accuracy:.2f}")