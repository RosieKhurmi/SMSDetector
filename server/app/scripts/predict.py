import pickle

with open('../services/nb_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('../services/vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)


def classify_message(message):
    message_transformed = vectorizer.transform([message])
    prediction = model.predict(message_transformed)
    return 'Spam' if prediction[0] == 0 else 'Ham'
