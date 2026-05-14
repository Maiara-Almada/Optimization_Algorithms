from utils import generate_random_solution, fitness_function
from NN import data_partition, get_predictions
from project_data import data

X_train, X_val, X_test, Y_train, Y_val, Y_test=data_partition(data,'status') #partitioning our data

random_sol=generate_random_solution(2200) #generating a random solution to test our functions

y_pred_random=get_predictions(random_sol, X_train, X_val, Y_train, Y_val) #random prediction

fitness_random=fitness_function(y_pred_random, Y_val) #checking random prediction's fit
print(fitness_random)

