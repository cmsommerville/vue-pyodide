import pickle
import base64
import numpy
from sklearn import datasets
from sklearn.svm import SVC


# x = pickle.dumps({"A": 1, "B": 2})
iris = datasets.load_iris()
X = iris.data
Y = iris.target

model = SVC(kernel='linear', C=1).fit(X, Y)


model_bin = pickle.dumps({
    "model": model,
    "classes": iris.target_names
})

model_b64 = base64.b64encode(model_bin)
with open("model.txt", "wb") as f:
    f.write(model_b64)

res = model.predict(numpy.array([5, 2, 3, 100]).reshape(1, -1))[0]
print(iris.target_names[res])
