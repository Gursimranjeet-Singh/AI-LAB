import random
import math

def create_board(n, initial_config=None):
    if initial_config:
        return initial_config
    return [random.randint(0, n-1) for _ in range(n)]

def count_conflicts(board):
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

def get_neighbors(board):
    neighbors = []
    for i in range(len(board)):
        for row in range(len(board)):
            if row != board[i]:
                neighbor = board[:]
                neighbor[i] = row
                neighbors.append(neighbor)
    return neighbors

def print_board(board):
    n = len(board)
    for row in range(n):
        line = ['Q' if board[col] == row else '.' for col in range(n)]
        print(' '.join(line))
    print()

def simulated_annealing(n, initial_config, max_iterations=1000, initial_temperature=100, cooling_rate=0.95):
    current_board = create_board(n, initial_config)
    current_conflicts = count_conflicts(current_board)
    temperature = initial_temperature
    
    best_board = current_board[:]
    best_conflicts = current_conflicts
    
    print("Initial configuration:")
    print_board(current_board)
    print(f"Initial number of conflicts: {current_conflicts}\n")
    
    for iteration in range(max_iterations):
        if current_conflicts == 0:
            print(f"Solution found at iteration {iteration + 1}!")
            print("Final configuration (solution):")
            print_board(current_board)
            return current_board
        
        neighbors = get_neighbors(current_board)
        next_board = random.choice(neighbors)
        next_conflicts = count_conflicts(next_board)
        
        if next_conflicts < current_conflicts:
            current_board = next_board
            current_conflicts = next_conflicts
        else:
            probability = math.exp((current_conflicts - next_conflicts) / temperature)
            if random.random() < probability:
                current_board = next_board
                current_conflicts = next_conflicts
        
        temperature *= cooling_rate

    print(f"No solution found within {max_iterations} iterations.")
    print("Best configuration found:")
    print_board(best_board)
    return best_board

n = 4
initial_config = [2, 1, 3, 0]  
solution = simulated_annealing(n, initial_config)
