import math
from collections import deque

def solve_jug_problem(jug1,jug2,target):
    
    if target>max(jug1,jug2):
        return "Target quanitity cannot be greater than capacity of larget jug."
    if target % math.gcd(jug1,jug2) != 0:
        return "No solution exists for these inputs."
    
    queue = deque([[(0,0)]])
    visited = set()
    visited.add((0,0))

    while queue:
        path = queue.popleft()
        current_state = path[-1]
        amt1, amt2 = current_state

        if amt1 == target or amt2 == target:
            return path

        next_steps = set()

        next_steps.add((jug1, amt2))

        next_steps.add((amt1, jug2))

        next_steps.add((0,amt2))

        next_steps.add((amt1,0))

        pour_to_j1 = min(jug1-amt1,amt2)
        next_steps.add((amt1 + pour_to_j1, amt2 - pour_to_j1))

        pour_to_j2 = min(jug2-amt2,amt1)
        next_steps.add((amt1 - pour_to_j2, amt2 + pour_to_j2))

        for state in next_steps:
            if state not in visited:
                visited.add(state)
                new_path = list(path)
                new_path.append(state)
                queue.append(new_path)

    return "No solution found"
    
        

jug1=int(input("Enter quantity of jug 1:"))
jug2=int(input("Enter quantity of jug 2:"))
target=int(input("Enter target quantity:"))

if jug1<=0 or jug2<=0 or target<=0:
    print("Quantity cannot be negative")
else:
    result = solve_jug_problem(jug1, jug2, target)

    if isinstance(result, str):
        print("\n Result:",result)
    else:
        print("\n Solution found")
        print("Steps needed:",len(result)-1)
        print("Format:(Jug 1, Jug 2)")
        for num, state in enumerate(result):
            print(num,":",state)
    
