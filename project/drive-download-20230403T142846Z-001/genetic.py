import numpy as np
import pandas as pd
import copy
import warnings
import random

class Items:
    def __init__(self, index, weight, value, class_type):
        self.index = index
        self.weight = int(weight)
        self.value = int(value)
        self.class_type = int(class_type)

# class ListOfChromosome:
#     def __init__(self, total_weight, total_value, size):
#         self.total_weight = total_weight
#         self.total_value = total_value
#         self.size = size

class ReadInput:
    def __init__(self, filename):
        self.filename = filename
    def read(self):
        list_item = []
        with open(self.filename, 'r') as f:
            lines = f.read().splitlines()
            storage_capacity = lines[0]
            number_of_classes = lines[1]
            weights_of_n_items = [x.strip() for x in lines[2].split(',')]
            values_of_n_items = [x.strip() for x in lines[3].split(',')]
            class_of_n_items = [x.strip() for x in lines[4].split(',')]
            # print(len(weights_of_n_items))
            for i in range(len(weights_of_n_items)):
                list_item.append(Items(i, weights_of_n_items[i], values_of_n_items[i], class_of_n_items[i]))
            return storage_capacity, number_of_classes, weights_of_n_items, list_item


def RandomOneChromosomes(chromosome):
    return [random.randint(0, 1) for _ in range (chromosome)]

def GeneratePopulation(size, chromosome_len, weights_of_n_items):
    List_Of_Chromosome = []
    for _ in range(size):
        # List_Of_Chromosome.append(RandomOneChromosomes(chromosome_len))
        genes = [0, 1]
        chromosome = []
        for _ in range(len(weights_of_n_items)):
            chromosome.append(random.choice(genes))
        List_Of_Chromosome.append(chromosome)    
    return List_Of_Chromosome

def CalculateFitness(chromosome, list_item, weight_limit, number_of_classes):
    total_weight = 0
    total_value = 0
    class_count = [0] * int(number_of_classes)
    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            total_weight += list_item[i].weight
            total_value += list_item[i].value
            class_count[list_item[i].class_type - 1] += 1
    if 0 in class_count:
      return 0
    if (total_weight > int(weight_limit)):
      return 0 
    else: 
      return total_value
        

def SelectChromosomes(List_Of_Chromosome,list_item, weight_limit, number_of_classes):
    fitness_values = []
    for chromosome in List_Of_Chromosome:
      fitness_values.append(CalculateFitness(chromosome, list_item, weight_limit, number_of_classes))
    total_fitness = sum(i for i in fitness_values)
    if total_fitness==0:
        fitness_values = [1/len(List_Of_Chromosome) for i in fitness_values]
    else:
        fitness_values = [float(i)/total_fitness for i in fitness_values]
    # random_pick = np.random.choice(len(List_Of_Chromosome), p=fitness_values)
    # parent1 = List_Of_Chromosome[random_pick]
    # random_pick = np.random.choice(len(List_Of_Chromosome), p=fitness_values)
    # parent2 = List_Of_Chromosome[random_pick]
    parent1 = random.choices(List_Of_Chromosome, weights=fitness_values, k=1)[0]
    parent2 = random.choices(List_Of_Chromosome, weights=fitness_values, k=1)[0]
    return parent1, parent2

def crossover(parent1, parent2):
	crossover_point = random.randint(0, len(parent1)-1)
	child1 = parent1[0:crossover_point] + parent2[crossover_point:len(parent1)]
	child2 = parent2[0:crossover_point] + parent1[crossover_point:len(parent2)]
	return child1, child2

def mutate(chromosome):
    mutation_point = random.randint(0, len(chromosome) - 1)
    if (chromosome[mutation_point] == 0):
      chromosome[mutation_point] == 1
    else:
      chromosome[mutation_point] == 0
    return chromosome

def get_best(ListOfChromosome, list_item, weight_limit, number_of_classes):
    fitness_value = []
    for chromosome in ListOfChromosome:
      fitness_value.append(CalculateFitness(chromosome, list_item, weight_limit, number_of_classes))
    max_value = max(fitness_value)
    # print(max_value)
    max_index = fitness_value.index(max_value)
    return ListOfChromosome[max_index]

def main():
    Input = ReadInput('input_x.txt')
    weight_limit, number_of_classes, number_of_items, list_item = Input.read()
    population_size = 1000
    mutation_probability = 0.2
    generations = 500

    ListOfChromosome = GeneratePopulation(population_size, len(list_item), number_of_items)
    for j in range(generations):
        parent1, parent2 = SelectChromosomes(ListOfChromosome, list_item, weight_limit, number_of_classes)
        child1, child2 = crossover(parent1, parent2)
        if random.uniform(0, 1) < mutation_probability:
          child1 = mutate(child1)
        if random.uniform(0, 1) < mutation_probability:
          child2 = mutate(child2)
        ListOfChromosome = [child1, child2] + ListOfChromosome[2:]
    best = get_best(ListOfChromosome, list_item, weight_limit, number_of_classes)
    total_weight = 0
    total_value = 0
  
    for i in range(len(best)):
      if best[i] == 1:
          total_value += list_item[i].value
          total_weight += list_item[i].weight

    best_str = ', '.join(str(x) for x in best)
    print(total_value)
    print(best_str)


    with open("output_x.txt", 'w') as f:
      f.write(str(total_value) + '\n')
      f.write(best_str)

    



    # for i in range(len(weights_of_n_items)):
    #     List_Of_Items.append(Items(weights_of_n_items[i], values_of_n_items[i], class_of_n_items[i], i))

def Genetic_Algorithm(item_list, capacity, classes):
    main()
