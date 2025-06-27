import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.metrics import accuracy_score

# Load data
df = pd.read_csv(r"rainfall.csv")
df.columns = df.columns.str.strip()  # Strip column name spaces

# Convert target column 'rainfall' to 0 and 1
df['rainfall'] = df['rainfall'].map({'no': 0, 'yes': 1})

# Select only required columns
X = df[['temperature', 'humidity', 'windspeed']]
y = df['rainfall']

# Handle missing values
X = X.fillna(X.mean())

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {acc:.2f}")

# Save model
joblib.dump(model, 'rainfall_model.pkl')
print("Model saved successfully!")

# Test the model
test_input = [[25.0, 80.0, 15.0]]  # temperature, humidity, wind_speed
prediction = model.predict(test_input)
print(f"Test prediction: {prediction[0]}")
