import random
import heapq
import time
import statistics
import tracemalloc
from typing import List, Tuple , Callable
from itertools import combinations


def is_valid_state(board: List[int], n: int) -> bool:
    return len(set(board)) == len(board) and not any(abs(a-b) == abs(x-y) for (a,x), (b,y) in combinations(enumerate(board), 2))

#hàm tạo các trạng thái khi fi chuyển 1 quân hậu ở từng cột
def generate_successor_states(board: List[int],n: int) ->List[List[int]]:
    successor_states = []
    for col in range(n):
        for row in range(n):
            if board[col] != row + 1:
                new_board = board.copy()
                new_board[col] = row + 1
                successor_states.append(new_board)
    return   successor_states

def min_conflict_heuristic(board: List[int], n: int) -> int:
    conflicts = 0
    for i in range(n):
        # vòng for sẽ duyệt phần thử thứ i+1 trở đi nên sẽ không kiểm lại những quân hậu trước i+1 => số cặp quân hậu tấn công nhau
        for j in range(i+1, n):
            if board[i] == board[j] or abs(board[i]-board[j]) == abs(i-j):
                conflicts += 1
    return conflicts 

def uniform_Cost_Search (board: List[int], n : int) -> Tuple[bool, List[int]]:
    tracemalloc.start()
    # thêm start vào frontier
    frontier = [(0,board)] #heap 
    explorer_set = set()
    while frontier: # chạy đến khi heap thành một empty sequence
        # pop ra khỏi frontier để xét 
        (cost, board) = heapq.heappop(frontier)
        # nếu đã có phần tử này trong expand thì bỏ qua nó
        if tuple(board) in explorer_set:
            continue
        #bảng được mở được thêm vào expand
        explorer_set.add(tuple(board))
        # kiểm tra bảng vừa thêm vào expand có phải goal không để dừng alg
        if is_valid_state(board, n):
            return True, board
        # tạo các trạng thái con , kiểm tra nó đã được xét chưa ( có thuộc expand không) , ko thì thêm vào frontier 
        for successor in generate_successor_states(board, n):
            if tuple(successor) not in explorer_set:
                heapq.heappush(frontier, (cost + 1, successor))
    tracemalloc.stop()
    return False, []

def graph_search_a_star(board: List[int], n: int) -> Tuple[bool, List[int]]:
    tracemalloc.start()
    # thêm start vào frontier
    frontier = [(min_conflict_heuristic(board, n), board)] #heap
    explorer_set = set()

    while frontier: # chạy đến khi heap thành một empty sequence
        # pop ra khỏi frontier để xét ( xét trạng thái bàn cờ)
        (h,node) = heapq.heappop(frontier)
        # nếu đã có node này trong expand thì bỏ qua nó
        if tuple(node) in explorer_set:
            continue
        # thêm node vào expand
        explorer_set.add(tuple(node))
        # kiểm tra nó có phải goal không
        if h == 0:
            return True, node
        # tạo các trạng thái con , kiểm tra nó đã được xét chưa ( có thuộc expand không) , ko thì thêm vào frontier 
        for successor in generate_successor_states(node, n):
            if tuple(successor) not in explorer_set:
                heapq.heappush(frontier, (min_conflict_heuristic(successor, n), successor))
    tracemalloc.stop()
    return False, []

def print_board(board):
    n = len(board)
    for i in range(n):
        row = ""
        for j in range(n):
            if board[j] == i+1:
                row += "Q   "
            else:
                row += "*   "
        print(row)
    print("")

def initialize_population(pop_size: int, n: int) -> List[List[int]]:
    # tạo danh sách rỗng , pop_size là kích thước quần thể
    population = []
    while len(population) < pop_size:
        # tạo bàn cờ ngẫu nhiên có n quân hậu khác nhau trên bàn cờ
        board = random.sample(range(1,n+1),n)
        #kiểm tra tính hợp lệ của bàn cờ
        if is_valid_state(board,len(board)):
            population.append(board)
    return population

# tính điểm thích nghi của quần thể
def compute_fitness(population: List[List[int]]) -> List[int]:
    # danh sách điểm thích nghi của quân thể
    fitness_scores = []
    # tính điễm thích nghi  của cá thể
    # xét từng cá thể trong quần thể
    for individual in population:
        conflicts = 0
        for i in range(len(individual)):
            for j in range(i+1, len(individual)):
                # kiểm tra xung đột về hàng
                if individual[i] == individual[j]:
                    conflicts += 1
                # kiểm tra xung đột về đường chéo
                if abs(individual[i] - individual[j]) == abs(i - j):
                    conflicts += 1
        fitness_scores.append(conflicts)
    return fitness_scores

# 1. Nhận đầu vào là một danh sách các bàn cờ trong quần thể population 
# và danh sách điểm thích nghi tương ứng fitness_scores
# 2. Hàm sẽ chọn hai bàn cờ cha mẹ từ quần thể hiện tại 
# để tạo ra bàn cờ con mới trong quá trình lai ghép.
# trả về tuple để  bảo vệ dữ liệu khỏi việc sửa đổi vì chúng không thể được thay đổi sau khi khởi tạo.
def select_parents(population: List[List[int]], fitness_scores: List[int]) -> Tuple[List[int], List[int]]:
    # sử dụng thuật toán "roulette wheel" 
    # xác suất được chọn bằng tỷ lệ của điểm thích nghi của nó 
    # so với tổng điểm thích nghi của toàn bộ quần thể

    # chuyển danh sách các fitness về danh sách xác suất 
    probabilities = [1 - (fitness_score / sum(fitness_scores)) for fitness_score in fitness_scores]
    # chọn ngẫu nhiên ba mẹ
    parent1, parent2 = random.choices(population, weights=probabilities, k=2)
    return parent1, parent2

# giao phối cha và mẹ được chọn ngẫu nhiên để tạo ra một con 
# chọn một điểm cắt ngẫu nhiên trong dãy gen của bố , 
# và đưa các gen từ mẹ vào phía sau điểm cắt này để tạo ra đứa con
def crossover(parent1: List[int], parent2: List[int]) -> List[int]:
    n = len(parent1)
    # random vị trí điểm cắt
    crossover_point = random.randint(1, n-1)
    # dấu 2 chấm thể hiện sẽ lấy từ phần tử đầu đến phần tử mang vị trí được xác định lả điểm cắt
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# mutation_rate : xác suất đột biến (<1) 
def mutate(individual: List[int], mutation_rate: float) -> List[int]:
    n = len(individual)
    # nếu giá trị ngẫu nhiên được sinh ra nhỏ hơn mutation_rate, 
    # thì giá trị của phần tử đó sẽ bị đột biến thành một giá trị ngẫu nhiên mới 
    # nằm trong khoảng từ 0 đến n-1.
    for i in range(n):
        # random.random() sẽ sinh ra một số thực ngẫu nhiên trong khoảng từ 0 đến 1
        if random.random() < mutation_rate:
            # giá trị của phần tử đó sẽ bị đột biến thành 
            # một giá trị ngẫu nhiên mới nằm trong khoảng từ 0 đến n-1
            individual[i] = random.randint(0, n-1)
            #trả về danh sách các cá thể đột biến
    return individual

def genetic_algorithm(pop_size: int, n: int, generations: int, mutation_rate: float) -> List[int]:
    tracemalloc.start()
    # Khởi tạo quần thể ban đầu
    population = initialize_population(pop_size, n)
    for i in range(generations):
        # Tính điểm thí nghi của mỗi cá thể trong quần thể
        fitness_scores = compute_fitness(population)
        #  kiểm tra xem bàn cờ tốt nhất trong thế hệ hiện tại có số lượng xung đột = 0
        #  (ko quân hậu nào xung đột) 
        if max(fitness_scores) == 0:
            return population[fitness_scores.index(max(fitness_scores))]
        # chọn ba mẹ để tiến hành lai ghép
        parent1, parent2 = select_parents(population, fitness_scores)
        # tạo cá thể con
        child = crossover(parent1, parent2)
        # đột bien ngẫu nhiên
        child = mutate(child, mutation_rate)
        # đánh giá điểm thích nghi 
        child_fitness = compute_fitness([child])[0]

        # Chọn ra các cá thể sinh tồn của thế hệ mới 
        # bao gồm cá thể con và các cá thể trong quần thể hiện tại
        # bằng cách sắp xếp tăng dần điểm thích nghi

        population_with_child = population + [child]
        fitness_scores_with_child = compute_fitness(population_with_child)
        # sắp xếp các cá thể theo thứ tự tăng dần của giá trị fitness
        sorted_indices = sorted(range(len(fitness_scores_with_child)), key=lambda k: fitness_scores_with_child[k])
        # chọn ra pop_size cá thể tốt nhất để truyền lại vào quá trình tiếp theo của thuật toán.
        population = [population_with_child[index] for index in sorted_indices[:pop_size]]
    # trả về trạng thái tốt nhất
    fitness_scores = compute_fitness(population)
    tracemalloc.stop()
    return population[fitness_scores.index(min(fitness_scores))]

if __name__ == "__main__":

    n = int(input("Nhập số quân hậu : "))
    choice = input(f"Chọn thuật toán (1: Uniform Cost Search, 2: A* Search, 3: Genetic Algorithm): ")

    if choice == "1":
        list_time = []
        list_mem = []
        for i in range(3):
            board_chess = random.sample(range(1,n+1),n)
            print(f"Bàn cờ ban đầu :")
            print(board_chess)
            start_time = time.time()
            (valid, solution) = uniform_Cost_Search(board_chess,n)
            end_time = time.time()
            run_time = end_time - start_time
            list_time.append(run_time)
            memory_used = tracemalloc.get_traced_memory()[0]
            list_mem.append(memory_used)
            if valid:
                print("")
                print(f"Bàn cờ hợp lệ thứ ", i+1 , ":")
                print_board(solution)
                print(f"Thời gian chạy lần thứ {i+1}: {run_time * 1000} ms")
                print(f"Giá trị bộ nhớ được sử dụng lần thứ {i+1}: { memory_used / 10**6} MB")
            else:
                print("Khong tim thay trang thai hop le")
        avg_time = statistics.mean(list_time)
        current = statistics.mean(list_mem)
        print("")
        print(f"Trung bình thời gian chạy: {avg_time*1000} ms")
        print(f"Trung bình giá trị bộ nhớ được sử dụng: {current / 10**6} MB")
    elif choice == "2":
        list_time = []
        list_mem = []
        for i in range(3):
            board_chess = random.sample(range(1,n+1),n)
            print(f"Bàn cờ ban đầu :")
            print(board_chess)
            start_time = time.time()
            (valid, solution) = graph_search_a_star(board_chess,n)
            end_time = time.time()
            run_time = end_time - start_time
            memory_used = tracemalloc.get_traced_memory()[0]
            list_mem.append(memory_used)
            list_time.append(run_time)
            if valid:
                print("")
                print(f"Bàn cờ hợp lệ thứ ", i+1 , ":")
                print_board(solution)
                print(f"Thời gian chạy lần thứ {i+1}: {run_time * 1000} ms")
                print(f"Giá trị bộ nhớ được sử dụng lần thứ {i+1}: { memory_used / 10**6} MB")
            else:
                print("Không tìm thấy trạng thái hợp lệ")
        avg_time = statistics.mean(list_time)
        current = statistics.mean(list_mem)
        print("")
        print(f"Trung bình thời gian chạy: {avg_time*1000} ms")
        print(f"Trung bình giá trị bộ nhớ được sử dụng: {current / 10**6} MB")    
    elif choice == "3":
        list_time = []
        list_mem = []
        for i in range(3):
            pop_size = 100
            generations = 1000
            mutation_rate = 0.1
            start_time = time.time()
            solution = genetic_algorithm(pop_size, n, generations, mutation_rate)
            end_time = time.time()
            run_time = end_time - start_time
            memory_used = tracemalloc.get_traced_memory()[0]
            list_mem.append(memory_used)
            list_time.append(run_time)
            if len(solution) > 0:
                print("")
                print(f"Bàn cờ hợp lệ thứ ", i+1 , ":")
                print_board(solution)
                print(f"Thời gian chạy lần thứ {i+1}: {run_time * 1000} ms")
                print(f"Giá trị bộ nhớ được sử dụng lần thứ {i+1}: { memory_used / 10**6} MB")
            else:
                print("Không tìm thấy trạng thái hợp lệ")
        avg_time = statistics.mean(list_time)
        current = statistics.mean(list_mem)
        print("")
        print(f"Trung bình thời gian chạy: {avg_time*1000} ms")
        print(f"Trung bình giá trị bộ nhớ được sử dụng: {current / 10**6} MB")
