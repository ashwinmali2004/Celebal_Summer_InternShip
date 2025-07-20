# Train a classifier on Iris dataset
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
iris = load_iris()
X, y = iris.data, iris.target

model = RandomForestClassifier()
model.fit(X, y)

model_dir = 'Week_7\model'
os.makedirs(model_dir, exist_ok=True)

model_path = os.path.join(model_dir, 'trained_model.pkl')
joblib.dump(model, model_path)
