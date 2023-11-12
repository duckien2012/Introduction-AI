import random
import heapq
import time
from typing import List, Tuple , Callable
from itertools import combinations

def is_valid_state(board: List[int], n: int) -> bool:
    return len(set(board)) == len(board) and not any(abs(a-b) == abs(x-y) for (a,x), (b,y) in combinations(enumerate(board), 2))



# Example usage
n = 10


pop_size = 100
generations = 1000
mutation_rate = 0.1
solution = genetic_algorithm(pop_size, n, generations, mutation_rate)
print(solution)