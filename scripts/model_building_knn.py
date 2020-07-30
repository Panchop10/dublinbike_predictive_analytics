import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import metrics

dataset = pd.read_csv (r'../datasets/final_dublinbike_dataset.csv')

#The X variable contains the first four columns of the dataset (attributes) while Y contains the labels.
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, 5]

#The script splits the dataset into 80% train data and 20% test data.
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# Initialize an array that stores the error rates.
error_rates = []

for a in range(1, 20):
    k = a
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    preds = knn.predict(X_test)
    error_rates.append(np.mean(y_test - preds))

# plt.figure(figsize=(10, 7))
# plt.plot(range(1,20),error_rates,color='blue', linestyle='dashed', marker='o',
#          markerfacecolor='red', markersize=10)
# plt.title('Error Rate vs. K Value')
# plt.xlabel('K')
# plt.ylabel('Error Rate')


classifier = KNeighborsClassifier(n_neighbors=10)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

df = pd.DataFrame({'actual': y_test, 'predicted': y_pred})

df1 = df.head(40)
df1['index'] = df1.reset_index().index
#print(df1)

ax = plt.gca()

df1.plot(kind='line',x='index',y='actual', color='green',ax=ax)
df1.plot(kind='line',x='index',y='predicted', color='red', ax=ax)
plt.title('Bikes available vs Bikes available predicted (KNN Method)')
plt.xlabel('index')
plt.ylabel('bikes available')

plt.show(block=True)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))