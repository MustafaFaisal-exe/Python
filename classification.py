from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score, roc_curve, confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('heart.csv')

X = df[['Cholesterol']]
Y = df['HeartDisease']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)

rf = RandomForestClassifier(n_estimators=100, random_state=42)

rf.fit(x_train, y_train)

y_pred = rf.predict(x_test)

print("precision score = ", precision_score(y_test, y_pred))
print("recall score = ", recall_score(y_test, y_pred))
print("f1 score = ", f1_score(y_test, y_pred))
print("Confusion matrix\n", confusion_matrix(y_test, y_pred))
y_prob = rf.predict_proba(x_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
plt.plot(fpr, tpr, label="Random Forest")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()