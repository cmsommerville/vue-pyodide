import pickle
import base64
from sklearn import datasets
from sklearn.svm import SVC

# read in iris dataset
iris = datasets.load_iris()

# split iris dataset into X and Y matrices
X = iris.data
Y = iris.target

# create a support vector machine model object and fit with X and Y data
model = SVC(kernel='linear', C=1).fit(X, Y)

# pickle a dictionary containing the fitted model and the class names
model_pickled = pickle.dumps({
    "model": model,
    "classes": iris.target_names
})

# convert the pickled object to base64
model_b64 = base64.b64encode(model_pickled)

# write the model to a text file
with open("model.txt", "wb") as f:
    f.write(model_b64)

print("Successfully wrote the model to model.txt...")
