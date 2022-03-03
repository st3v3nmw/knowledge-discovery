import pandas
pandas.options.mode.chained_assignment = None

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import classification_report

import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV

data_frame = pandas.read_csv('datasets/processed_risk_data.csv')

# remove the result column
x = data_frame.drop('RISK', axis=1)

# separate the result column
y = data_frame['RISK']

#split the datasets
trainX, testX, trainY, testY = train_test_split(x, y, test_size = 0.2)


################### SCALING

#To train a MLP network, the data should always be scaled

sc = StandardScaler()               # will be using the Standard Scaler
scaler = sc.fit(trainX)             # compute the mean and std to use for later scaling
trainX_scaled = scaler.transform(trainX)    # scale training set
testX_scaled = scaler.transform(testX)      #scale test set

# NB: no need to scale y since it is in discrete values
# NB: if y was a continuous dataset, scaling would be needed for that also

# Activation function - ‘identity’, ‘logistic’, ‘tanh’, ‘relu(default)’
# Solver - stochastic solvers eg sgd or adam || non stochastic lbfs (quasi newtonian)

mlp_clf = MLPClassifier(hidden_layer_sizes=(5,2), learning_rate='constant', learning_rate_init=0.001, max_iter = 300, activation = 'relu', solver = 'adam', shuffle=True)

# ######## TRAINING THE CLASSIFIER MODEL mlp_clf
mlp_clf.fit(trainX_scaled, trainY)


############ EVALUATION
y_pred = mlp_clf.predict(testX_scaled)


print('Accuracy: {:.2f}'.format(accuracy_score(testY, y_pred)))

# #### OTHER EVALUATION MENTRICS FROM THE MODEL
print('Error rate: {:.2f}'.format(1 - accuracy_score(testY, y_pred)))


fig = plot_confusion_matrix(mlp_clf, testX_scaled, testY, display_labels=mlp_clf.classes_)
fig.figure_.suptitle("Confusion Matrix for risk Dataset")
plt.show()



###### May take some time to run this bit ####################################
####### HYPER PARAMETER TUNING

param_grid = {
    'hidden_layer_sizes': [(150,100,50), (120,80,40), (100,50,30)],
    'max_iter': [50, 100, 150],
    'activation': ['tanh', 'relu'],
    'solver': ['sgd', 'adam'],
    'alpha': [0.0001, 0.05],
    'learning_rate': ['constant','adaptive'],
}

### gets the best parameter combinations of the ones given would return the best results
grid = GridSearchCV(mlp_clf, param_grid, n_jobs= -1, cv=5)

grid.fit(trainX_scaled, trainY)

print("\n\nYou can improve the results by using the folowing parameters: ", grid.best_params_)

grid_predictions = grid.predict(testX_scaled) 

print('Accuracy: {:.2f}'.format(accuracy_score(testY, grid_predictions)))