import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

print("Step 1: Reading datasets...")
app = pd.read_csv("dataset/application_record.csv")
credit = pd.read_csv("dataset/credit_record.csv")

print("Step 2: Filling missing values...")
app["OCCUPATION_TYPE"] = app["OCCUPATION_TYPE"].fillna("Unknown")

print("Step 3: Encoding application data...")
le = LabelEncoder()

for col in app.columns:
    if app[col].dtype == "object" or str(app[col].dtype) == "string" or str(app[col].dtype) == "str":
        app[col] = LabelEncoder().fit_transform(app[col].astype(str))

print("Step 4: Merging...")
df = app.merge(credit, on="ID")

print("Step 5: Creating target...")
df["Target"] = df["STATUS"].apply(lambda x: 1 if x in ["0", "C", "X"] else 0)

print("Step 6: Droppinpython test_model.pyg STATUS...")
X = df.drop(["STATUS", "Target", "ID", "MONTHS_BALANCE"], axis=1)
y = df["Target"]

# Encode remaining object columns
for col in X.columns:
    if X[col].dtype == "object" or str(X[col].dtype) == "string" or str(X[col].dtype) == "str":
        X[col] = LabelEncoder().fit_transform(X[col].astype(str))
# Check for remaining text columns
print("\nObject columns remaining:")
print(X.select_dtypes(include=["object"]).columns.tolist())

print("\nData types:")
print(X.dtypes)

print("Step 7: Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Step 8: Training model...")
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

print("Step 9: Saving model...")

print("Training features:")
print(X.columns.tolist())
print("Total features:", len(X.columns))

joblib.dump(model, "model.pkl")

print("Model Saved Successfully!")