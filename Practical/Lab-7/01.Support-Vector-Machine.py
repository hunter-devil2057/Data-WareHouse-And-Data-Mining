# Classifying Breast Cancer data using Support Vector Machine 
from sklearn import datasets
from sklearn.svm import SVC
from sklearn import metrics

cancer = datasets.load_breast_cancer()
x = cancer.data
y = cancer.target
print("Length of Data:", len(cancer.data))

split = int(len(x) * 0.7)
trainx, testx = x[:split], x[split:]
trainy, testy = y[:split], y[split:]

print("Number of features: ", len(cancer.feature_names))
# print("Features: ", *cancer.feature_names)
print("Number of classes: ", len(cancer.target_names))
print("Class Labels: ", cancer.target_names)

model = SVC(kernel="linear")  # Linear Kernel
model.fit(trainx, trainy)
yp = model.predict(testx)

# print("Actual Class: ", *testy)
# print("Predicted Class: ", *yp)

print("\nConfusion Matrix:")
print(metrics.confusion_matrix(testy, yp))

print("\nClassification Measures:")
print("Accuracy:", metrics.accuracy_score(testy, yp))
print("Recall:", metrics.recall_score(testy, yp))
print("Precision:", metrics.precision_score(testy, yp))
print("F1-score:", metrics.f1_score(testy, yp))