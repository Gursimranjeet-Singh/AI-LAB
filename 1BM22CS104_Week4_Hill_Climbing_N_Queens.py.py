def calculate_heuristic(state):
    heuristic = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]: 
                heuristic += 1
            if abs(state[i] - state[j]) == abs(i - j):  
                heuristic += 1
    return heuristic

def generate_neighbors(state):
    neighbors = []
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            new_state = state.copy()
            new_state[i], new_state[j] = new_state[j], new_state[i]  
            neighbors.append(new_state)
    return neighbors

def print_board(state):
    n = len(state)
    board = [['.'] * n for _ in range(n)]
    for row in range(n):
        board[row][state[row]] = 'Q'
    for row in board:
        print(' '.join(row))
    print()

def hill_climbing_n_queens(initial_state):
    current_state = initial_state
    
    while True:
        current_heuristic = calculate_heuristic(current_state)
        print(f"Current State: {current_state}, Heuristic: {current_heuristic}")
        print_board(current_state)  
        
        if current_heuristic == 0:
            return current_state
        
        neighbors = generate_neighbors(current_state)
        best_neighbor = None
        best_heuristic = float('inf')
        
        for neighbor in neighbors:
            heuristic = calculate_heuristic(neighbor)
            if heuristic < best_heuristic:
                best_heuristic = heuristic
                best_neighbor = neighbor
        
        if best_heuristic >= current_heuristic:
            break 
        
        current_state = best_neighbor
    
    return None 

def solve_n_queens():
    try:
        n = int(input("Enter the size of the board (N): "))
        if n <= 0:
            raise ValueError("N must be a positive integer.")
        initial_state = list(map(int, input(f"Enter the initial state for {n}-Queens as space-separated values (e.g., '0 1 2 3' for N=4): ").split()))
        if len(initial_state) != n or any(i < 0 or i >= n for i in initial_state):
            raise ValueError(f"Initial state must have {n} values, each between 0 and {n-1}.")
    except ValueError as e:
        print("Invalid input:", e)
        return
    
    solution = hill_climbing_n_queens(initial_state)
    
    if solution:
        print(f"Solution found for {n}-Queens problem: {solution}")
        print_board(solution) 
    else:
        print("No solution found.")

solve_n_queens()
