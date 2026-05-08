from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, accuracy_score
from testing import data

def data_partition(data,target_name):
    X=data.drop(columns=target_name)
    Y=data[target_name]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)
    X_train, X_val, Y_train, Y_val = train_test_split(X_train,
                                                      Y_train,
                                                      test_size=0.25, random_state=15, shuffle=True, stratify=Y_train
                                                      )

    return X_train, Y_train, X_test, Y_test


X_train, Y_train, X_test, Y_test=data_partition(data,'status')
print(X_test)