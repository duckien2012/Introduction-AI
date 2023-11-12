import heapq
import math
import random

maxClass = 0

def getValue(item):
  global maxClass
  return (math.ceil(math.log2(item[2] + 1)) == maxClass, item[1])
  #return item[1]
  
def Local_Beam(item_list = None, capacity = 0, classes = 0):
  print ("Local beam search")
  listSize = len(item_list)
  global maxClass
  maxClass = classes
  queue = list()

  max = (0, 0, 0, 0) #capacity, value, index, number node of each class

  for idx in range(listSize): #initialize starting points
    nextWeight = max[0] + item_list[idx][0]

    if (nextWeight > capacity): continue

    nextValue = max[1] + item_list[idx][1]
    nextNode = max[2] | (1 << idx)
    nextClass = max[3] | (1 << (item_list[idx][2] - 1))
    queue.append((nextWeight, nextValue, nextNode, nextClass))

  randomRestart = list()
  restartChance = 200 # 1000 -> 20%
  restartable = True
  searchSize = int(listSize * 1.5)

  classCheck = 2**classes - 1

  while queue:
    tmp = list()
    for node in queue:
      if node[1] > max[1] and node[3] == classCheck:
        max = node
      looted = math.ceil(math.log2(node[2] + 1))
      for idx in range(looted, listSize): # cut repeatable branch
        nextWeight = node[0] + item_list[idx][0]

        if (nextWeight > capacity): continue #cut unnecessary branch

        nextValue = node[1] + item_list[idx][1]
        nextNode = node[2] | (1 << idx)
        nextClass = node[3] | (1 << (item_list[idx][2] - 1)) 

        tmp.append((nextWeight, nextValue, nextNode, nextClass))
        if restartable:
          if random.randint(0, 1000) <= restartChance:
            randomRestart.append((nextWeight, nextValue, nextNode, nextClass))

    queue.clear()
    queue = heapq.nlargest(searchSize, tmp, key=getValue)
    tmp.clear()

    if not queue and restartable:
      restartable = False
      queue = randomRestart
      randomRestart.clear()

  return max 