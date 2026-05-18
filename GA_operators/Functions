'''Choice: Highly effective for continuous numerical optimization problems
Cons: It limits exploitation since offspring are strictly formed by linear combinations of parents. 
To maintain healthy exploration, it is often paired with a strong mutation operator - Gaussian Mutation.
Why Gaussian Mutation will ensure the algoprithms criativity because it allows for small, random perturbations in the offspring's genes, which can help the algorithm escape local optima and explore new areas of the solution space. 
This combination of Aritmethic Crossover and Gaussian Mutation can lead to a more robust search process, balancing exploitation of good solutions with exploration of new possibilities.'''
#PARA COMPLETAR SERIA BOM TAMBEM O UNIFORME MUTATION because it allows for a wider range of mutations, which can further enhance the algorithm's ability to explore the solution space and avoid premature convergence. By randomly altering genes with a uniform distribution, it can introduce more diversity into the population, increasing the chances of finding optimal solutions.


from random import random

#Exploitation (Exploração de Conhecimento)
def arithmetic_crossover(parent1, parent2): #select how much of the parents the children will inherit
    alpha = random()  # Randomly select a value between 0 and 1
    child1 = alpha * parent1 + (1 - alpha) * parent2
    child2 = alpha * parent2 + (1 - alpha) * parent1
    return child1, child2 #two children to maintain the population size and find the solution faster 


#Exploration (Exploração de Território)
def gaussian_mutation(child, mutation_rate, mutation_strength):
# Mutation Rate: Probability of changing 
# Mutation Strength: How much will change 
    for i in range(len(child)):
        if random() < mutation_rate:  # Check if mutation should occur
            child[i] += random() * mutation_strength  # Add a small random value to the gene
    return child            

if random() < mutation_rate:
    child1 = gaussian_mutation(child1, mutation_rate, mutation_strength)

if random() < mutation_rate:
    child2 = gaussian_mutation(child2, mutation_rate, mutation_strength)


# Exploration (Exploração de Território)
def blend_crossover(parent1, parent2, alpha=0.3):
  """Like arithmetic but children can land OUTSIDE the parent range. 
  The alpha parameter controls how far outside they can go."""
    child1 = []
    child2 = []
    for g1, g2 in zip(parent1, parent2):
        lo = min(g1, g2)
        hi = max(g1, g2)
        span = hi - lo
        # extend the sampling range by alpha on each side
        lo_ext = lo - alpha * span
        hi_ext = hi + alpha * span
        child1.append(lo_ext + random() * (hi_ext - lo_ext))
        child2.append(lo_ext + random() * (hi_ext - lo_ext))
    return child1, child2

def polynomial_mutation(child, mutation_rate, lower_bound, upper_bound, eta=20):
    """eta controls the shape of the perturbation distribution:
      - low eta  (e.g. 5)  → wide perturbations, more exploration
      - high eta (e.g. 20) → narrow perturbations, more exploitation
    Stays within [lower_bound, upper_bound] by design.
    """
    for i in range(len(child)):
        if random() < mutation_rate:
            u = random()
            delta_i = upper_bound - lower_bound
            if u < 0.5:
                delta = (2 * u) ** (1 / (eta + 1)) - 1
            else:
                delta = 1 - (2 * (1 - u)) ** (1 / (eta + 1))
            child[i] += delta * delta_i
            # clamp to valid range
            child[i] = max(lower_bound, min(upper_bound, child[i]))
    return child

 
