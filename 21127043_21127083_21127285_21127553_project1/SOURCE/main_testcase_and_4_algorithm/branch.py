import queue
import math

def Branch_Bound(item_list = None, capacity = 0, classes = 0):
  print ("Branch and bound")
  listSize = len(item_list)

  bfs = queue.Queue()

  max = (0, 0, 0, 0) #capacity, value, index, number node of each class
  bfs.put(max) #each node contained selected items
  classCheck = 2**classes - 1

  while not bfs.empty():
    node = bfs.get()
    # check with hold

    if node[1] > max[1] and node[3] == classCheck:
      max = node

    looted = math.ceil(math.log2(node[2] + 1))

    if looted == listSize:
      continue
    for idx in range(looted, listSize): # cut repeatable branch
      nextWeight = node[0] + item_list[idx][0]

      if (nextWeight > capacity): continue #cut unnecessary branch

      nextValue = node[1] + item_list[idx][1]
      nextNode = node[2] | (1 << idx)
      nextClass = node[3] | (1 << (item_list[idx][2] - 1))
      bfs.put((nextWeight, nextValue, nextNode, nextClass))
  return max 
