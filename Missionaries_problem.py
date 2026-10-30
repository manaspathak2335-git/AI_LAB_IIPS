from collections import deque

def is_valid_state(m, c):
    
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
        
    if m > 0 and m < c:
        return False
        
    right_m = 3 - m
    right_c = 3 - c
    if right_m > 0 and right_m < right_c:
        return False
        
    return True

def get_successors(state):
    
    m, c, boat = state
    successors = []
    
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    
    for m_move, c_move in moves:
        if boat == 1: 
            new_state = (m - m_move, c - c_move, 0)
        else:         
            new_state = (m + m_move, c + c_move, 1)
            
        if is_valid_state(new_state[0], new_state[1]):
            successors.append(new_state)
            
    return successors

def solve_bfs():
   
    initial_state = (3, 3, 1) 
    goal_state = (0, 0, 0)    
    
    queue = deque([[initial_state]])
    visited = set([initial_state])
    
    while queue:
        path = queue.popleft()
        current_state = path[-1]
        
        if current_state == goal_state:
            return path
            
        for next_state in get_successors(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((path + [next_state]))
                
    return None 

solution_path = solve_bfs()

if solution_path:
    print("Solution found in", len(solution_path) - 1, "steps:\n")
    print(f"{'Step':<6} | {'Left Bank (M, C)':<20} | {'Boat':<10} | {'Right Bank (M, C)'}")
    print("-" * 65)
    
    for step, state in enumerate(solution_path):
        m, c, boat = state
        boat_pos = "Left" if boat == 1 else "Right"
        right_m, right_c = 3 - m, 3 - c
        print(f"{step:<6} | {m}M, {c}C {'':<12} | {boat_pos:<10} | {right_m}M, {right_c}C")
else:
    print("No solution found.")
