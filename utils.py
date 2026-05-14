import numpy as np
import random
import matplotlib.pyplot as plt


def generate_random_solution(n_weights):  #generating our random solution as a start point for algorithms
    return[random.uniform(-0.05,0.05) for _ in range(n_weights)]


def fitness_function(prediction, actual): #minimization: makes sense to minimize prediction error
    fitness= 0
    for i in range(len(prediction)):
        error = ((actual[i] - prediction[i]) ** 2) ** 0.5
        fitness += error
    return fitness

