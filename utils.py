import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, accuracy_score


NN=MLPClassifier(hidden_layer_sizes=(100,), activation='relu', solver='adam', alpha=0.0001,  learning_rate='constant', coefs=)
def random_solution(n_weights):
    return[random.uniform(-0.05,0.05) for _ in range(n_weights)]


def fitness_function(solution):
    mlp_model = MLPClassifier(random_state=42, coefs=solution, max_iter=1000)

    fitness= accuracy_score(y_val, predv_mlp)
    return fitness