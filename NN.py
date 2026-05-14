from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from project_data import data


#data partition
def data_partition(data,target_name):
    X=data.drop(columns=target_name)
    Y=data[target_name]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)
    X_train, X_val, Y_train, Y_val = train_test_split(X_train,
                                                      Y_train,
                                                      test_size=0.25, random_state=15, shuffle=True, stratify=Y_train
                                                      )

    return X_train, X_val, X_test, Y_train, Y_val, Y_test

#training the data and getting the predictions
def get_predictions(solution,X_train,Y_train, X_val, Y_val):
    NN=MLPClassifier(hidden_layer_sizes=(100,), activation='relu', solver='adam', alpha=0.0001,  learning_rate='constant', coefs=solution)
    NN.fit(X_train, Y_train)
    Y_pred=NN.predict(X_val)
    return Y_pred



