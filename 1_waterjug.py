#Experiment 1 Solving the water jug problem using python
#objectibve to understand the basics of ai and ds by solving water jug problem
#used to efficently implement FIFO queue behaviour required for BFS
from collections import deque

#define a function water_jug solver with threee paramenters 
def water_jug_solver(jug1_capacity, jug2_capacity, target):
    visited = set()  #keep trasck of all visited state to avoid repeating time
    queue = deque()  #initialises a queue for BFS to hold the jug states (amounts of jug1 and jug 2)
    queue.append((0, 0))  #start with both jug empty :initial state(0,0)
    while queue: #continue looping until the queue is empty (all possible state have been reached)
        state = queue.popleft() #dequeues (pops from front ) the current state to explore
        if state in visited:  #skip processing oif state is already visited before
            continue
        visited.add(state)  #marks the current state as visited
        (a,b) = state  #a is current state of jug 1 and b for jug 2
        print(f"Jug1: {a}L, Jug2: {b}L")  #displays the current state for tracing 
        if a == target or b == target: #goal check if either jug has a target amount,print succeed
            print("Target achieved!")
            return
        possible_states = set()    #A set to store all new possible state from the current state 
        possible_states.add((jug1_capacity, b)) #fills jug 1 completly ,jug 2 remain same
        possible_states.add((a, jug2_capacity)) #fills jug 2 completly ,jug 1 remain same
        possible_states.add((0, b)) #empty jug 1, jug 2 remain the same
        possible_states.add((a, 0)) #empty jug 2, jug 1 remain the same
        pour_to_jug2 = min(a, jug2_capacity - b)  #pour water from jugs,,, poured from jug1 to jug2
        pour_to_jug1 = min(b, jug1_capacity - a)  #pour water from jugs,,, poured from jug2 to jug1
        possible_states.add((a - pour_to_jug2, b + pour_to_jug2)) #POUR FROM JUG 1 TO JUG 2
        possible_states.add((a + pour_to_jug1, b - pour_to_jug1)) #POUR FROM JUG 2 TO JUG 1
        queue.extend(possible_states) #adds all newly genrated states into the queue for further exploration

water_jug_solver(4, 3, 2) #calls the function