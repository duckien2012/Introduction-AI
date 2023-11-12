import queue
import math

def Brute_Force(item_list = None, capacity = 0, classes = 0): #using bfs to find
  print ("Brute_Force")
  listSize = len(item_list)

  bfs = queue.Queue()

  max = (0, 0, 0, 0) #capacity, value, index, number node of each class
  bfs.put(max) #each node contained selected items
  classCheck = 2**classes - 1
  
  while not bfs.empty():
    node = bfs.get()
    # check with hold

    if node[0] <= capacity and node[1] > max[1] and node[3] == classCheck: 
      max = node

    looted = math.ceil(math.log2(node[2] + 1))

    if looted == listSize:
      continue
    for idx in range(listSize):
      if (1 << idx) & node[2]: continue # no reselect
      nextWeight = node[0] + item_list[idx][0]
      nextValue = node[1] + item_list[idx][1]
      nextNode = node[2] | (1 << idx)
      nextClass = node[3] | (1 << (item_list[idx][2] - 1))
      bfs.put((nextWeight, nextValue, nextNode, nextClass))

  return max 
