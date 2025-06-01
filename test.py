import pickle
from sklearn_crfsuite import CRF
from helper import sent2features

# Load model
with open("marathi_crf_model.pkl", "rb") as f:
    crf = pickle.load(f)

# Example test sentence (tokenized manually)
test_sent = ["सपना", "पुण्याला", "रवाना", "झाली."]

# Extract features
X_test = [sent2features(test_sent)]

# Predict
pred = crf.predict(X_test)[0]

# Display result
print("\nNamed Entity Recognition:")
for token, tag in zip(test_sent, pred):
    print(f"{token:10s} -> {tag}")

