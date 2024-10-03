import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# nltk.download('punkt')
# nltk.download('stopwords')

df=pd.read_csv('docs/dataset.csv')
# 2. Vectorize the Text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])

labels=df['label']
# 3. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# 4. Train the Classifier (Logistic Regression)
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

# save the model to disk
filename = 'classifier_model.sav'
pickle.dump(classifier, open(filename, 'wb')) 
pickle.dump(vectorizer,open('vectorizer.sav','wb'))
# 5. Test the Classifier
y_pred = classifier.predict(X_test)

# 6. Evaluate the Classifier
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Example: Classify a new query
def classify_query(query):
    query_vec = vectorizer.transform([query])
    prediction = classifier.predict(query_vec)
    if prediction == 1:
        return "Informational - Call the VectorDB"
    else:
        return "Non-informational - No need to call the VectorDB"

# Test with a query
query = "what is sound?"

print(classify_query(query))  # Example test
