# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv('Data\\credit_data.csv')
df.loc[df.age < 0, 'age'] = 40.92 # Mean

features = df.iloc[:, 1:4].values
target = df.iloc[:,4].values

from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values = 'NaN', strategy='mean', axis=0)
imputer = imputer.fit(features[:, 1:4])
features[:, 1:4] = imputer.transform(features[:, 1:4])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
features = scaler.fit_transform(features)

from sklearn.model_selection import train_test_split
f_train, f_test, t_train, t_test = train_test_split(features, target, test_size = 0.3, random_state=0)

from sklearn.neural_network import MLPClassifier
# Verbose = True -> Show the error
# Solver = Adam -> The solver for weight otimization
# hidden_layer_sizes = number neurons
classifier = MLPClassifier(verbose = True, max_iter = 1000, tol = 0.000010, solver = 'adam', 
                           hidden_layer_sizes=(100), activation = 'relu')
classifier.fit(f_train, t_train)
predictions = classifier.predict(f_test)

from sklearn.metrics import confusion_matrix, accuracy_score
precision = accuracy_score(t_test, predictions)
matriz = confusion_matrix(t_test, predictions)
