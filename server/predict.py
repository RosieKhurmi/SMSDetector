import pickle
import os

base_dir = os.path.dirname(__file__)

model_path = os.path.join(base_dir, 'app', 'services', 'nb_model.pkl')
vectorizer_path = os.path.join(base_dir, 'app', 'services', 'vectorizer.pkl')

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

with open(vectorizer_path, 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)


def classify_message(message):
    message_transformed = vectorizer.transform([message])
    prediction = model.predict(message_transformed)
    return 'Spam' if prediction[0] == 0 else 'Ham'
