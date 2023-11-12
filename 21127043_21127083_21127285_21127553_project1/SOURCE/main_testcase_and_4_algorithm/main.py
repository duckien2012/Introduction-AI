import numpy as np
import math
import queue
import heapq
import time
import random
import tracemalloc
import sys

from brute import Brute_Force
from branch import Branch_Bound
from local import Local_Beam
from genetic import Genetic_Algorithm

def printans(item,item_list):
  binary_str = format(item[2], 'b')
  binary_list = list(binary_str)
  binary_list.reverse()
  print("{}".format(item[1]))
  n = "{}".format(', '.join(binary_list))
  if (len(item_list) - len(bin(item[2]-1)[2:])) != 0 :
    for i in range (len(item_list) - len(bin(item[2]-1)[2:])):
      n = n + ", 0"
  print(n)

def runAlgorithm(item_list, capacity, classes, algorithm):
  if algorithm is None:
    return
  start = time.time()
  tracemalloc.start()

  printans(algorithm(item_list, capacity, classes), item_list)

  mem = tracemalloc.get_traced_memory()
  print("Total memory: ", abs(mem[0] - mem[1]) // 1024, "KB")
  print("Running time: ", time.time() - start, "s")
  tracemalloc.stop()

def start():
  #read data
  algorithm = str()
  inputFile = open("input_x.txt", "r")

  if (len(sys.argv) > 1):
    algorithm = sys.argv[1]
    if (len(sys.argv) > 2):
      inputFile = open(sys.argv[2], "r")
  else:
    algorithm = input()

  capacity = int(inputFile.readline())
  classes = int(inputFile.readline())
  item_weights = map(int, inputFile.readline().split(", "))
  item_values = map(int, inputFile.readline().split(", "))
  item_classes = map(int, inputFile.readline().split(", "))
  
  item_list = list(map(lambda w, v, c:(w, v, c), item_weights, item_values, item_classes))
  # print(item_list)
  algorithmMap = {'1':Brute_Force, '2':Branch_Bound, '3':Local_Beam, '4': Genetic_Algorithm}

  #run algorithm
  try:
    runAlgorithm(item_list, capacity, classes, algorithmMap[algorithm])
  except KeyError:
    runAlgorithm(item_list, capacity, classes, Brute_Force)
    runAlgorithm(item_list, capacity, classes, Branch_Bound)
    runAlgorithm(item_list, capacity, classes, Local_Beam)
    runAlgorithm(item_list, capacity, classes, Genetic_Algorithm)

if __name__ == '__main__':
  start()