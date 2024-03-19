from google.colab import drive
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

//경로설정
drive.mount('')
data_path = ''
data = pd.read_csv(data_path)

print(data['not.fully.paid'].value_counts())
a = data.drop('not.fully.paid', axis=1)
b = data['not.fully.paid']
a_encoded = pd.get_dummies(a, columns=['purpose'])
a_train, a_test, b_train, b_test = train_test_split(a_encoded, b, test_size=0.3, random_state=42)
smote = SMOTE(random_state=42)
a_train_resampled, b_train_resampled = smote.fit_resample(a_train, b_train)
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(a_train_resampled, b_train_resampled)
b_pred = log_reg.predict(a_test)
accuracy = accuracy_score(b_test, b_pred)
print("Accuracy:", accuracy)
print(classification_report(b_test, b_pred))