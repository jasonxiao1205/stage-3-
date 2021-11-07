import pandas as pd
from sklearn import linear_model
from sklearn import metrics
from sklearn.model_selection import train_test_split

df = pd.read_csv('clean salary.csv')
column_names = list(df.columns)
input_names = column_names[0:len(column_names)-1]# slice data frame to extract input variable
target_name = column_names[7] # slice data frame to extract target variable

X = df[input_names]
y = df[target_name]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)
clf = linear_model.LogisticRegression(solver='liblinear').fit(X_train, y_train)
y_pred = clf.predict(X_test)
y_pred_proba = clf.predict_proba(X_test)

print('----- Sample case -----')
last_sample = X_test.loc[list(X_test.index)[-1]]
last_sample_proba = y_pred_proba[-1]
print('Probability of 0:', last_sample_proba[0])
print('Probability of 1:', last_sample_proba[1])
print('Predicted class:',y_pred[-1])
print('Actual class:', y_test.loc[list(y_test.index)[-1]])
print('where 0 means basesalary less than 140000, 1 means basesalary exceeds 140000')
print('-----------------------')
print('Calculate the accuracy using the test data')
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))



