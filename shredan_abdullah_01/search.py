from problem import HeuristicFunction, Problem, S, A, Solution
from collections import deque
import queue
from queue import PriorityQueue, Queue
from helpers.utils import NotImplemented

#TODO: Import any modules you want to use
import heapq

# All search functions take a problem and a state
# If it is an informed search function, it will also receive a heuristic function
# S and A are used for generic typing where S represents the state type and A represents the action type

# All the search functions should return one of two possible type:
# 1. A list of actions which represent the path from the initial state to the final state
# 2. None if there is no solution

def BreadthFirstSearch(problem: Problem[S, A], initial_state: S) -> Solution:
    #TODO: ADD YOUR CODE HERE # 8/8
    explored = set()
    pathe = []  # action path
    path = []  # stetes path
    # node = [initial_state]
    frontier = [initial_state]  # list of states FIFO
    # list of parents of each node
    parents = {initial_state: ('null', initial_state)}
    while frontier:
        # last state in FIFO
        node = frontier.pop(0)
        if node not in explored:  # add to visitied if not have been before , check and do else
            explored.add(node)
        else:  # to avoid double expansion
            continue
        # loop over possible actions from a state
        for action in problem.get_actions(node):

            # get successor of current node
            child = problem.get_successor(node, action)
            if child == action:
                flag = 0  # graph #know the kind of question to see if return states or paths
            else:
                flag = 1  # suko
            if child not in explored and child not in frontier:
                if problem.is_goal(child):  # if goal reached
                    if flag == 0:
                        # intialize parent of current child
                        parents[child] = (node, action)
                        path.append(child)
                        newnode = path[0]
                        parent = parents[newnode]
                        prev = parent[0]

                        while prev != initial_state:
                            path.append(prev)  # append the state
                            parent = parents[prev]  # fro looping
                            prev = parent[0]

                        path.reverse()
                        return path

                    else:
                        pathe.append(action)  # append the action case of suko
                        parent_tuple = parents[node]  # parent of that child
                        parent = parent_tuple[0]
                        actioon = parent_tuple[1]
                        while parent != 'null':
                            # getting parent of the node called parent "originally was child"
                            pathe.append(actioon)
                            # parent is a key tuple and we want it equal to first element only
                            parent_tuple = parents[parent]
                            parent = parent_tuple[0]
                            actioon = parent_tuple[1]

                        pathe.reverse()
                        return pathe
                        # explored.add(child)
                else:

                    parents[child] = (node, action)  # intialize parent
                    frontier.append(child)  # add to frontier and move forword

    return None
#################second try################ 1/8
    # # Initialize sets and lists
    # explored = set()  # to store explored states
    # frontier = [initial_state]  # to store states for BFS
    # parents = {initial_state: ('null', initial_state)}  # to store parents of each node

    # # Main BFS loop
    # while frontier:
    #     # Get the last state in the FIFO queue
    #     node = frontier.pop(0)

    #     # Check if the node has not been explored yet
    #     if node not in explored:
    #         explored.add(node)  # mark node as explored
    #     else:
    #         continue  # skip to the next iteration if the node has already been explored

    #     # Loop over possible actions from a state
    #     for action in problem.get_actions(node):
    #         # Get the successor of the current node
    #         child = problem.get_successor(node, action)
    #         flag = 0 if child == action else 1  # flag to distinguish between graph and suko

    #         # Check if the child is a new state and not in the frontier
    #         if child not in explored and child not in frontier:
    #             # Check if the goal is reached
    #             if problem.is_goal(child):
    #                 path = [child]
    #                 new_node = path[0]
    #                 parent = parents[new_node]
    #                 prev = parent[0]

    #                 # Reconstruct the path by backtracking through parents
    #                 while prev != initial_state:
    #                     path.append(prev)  # append the state
    #                     parent = parents[prev]  # for looping
    #                     prev = parent[0]

    #                 path.reverse()  # reverse the path to get the correct order

    #                 # Return the path or path of actions based on the flag
    #                 return path if flag == 0 else [parents[node][1]] + path

    #             else:
    #                 parents[child] = (node, action)  # initialize parent
    #                 frontier.append(child)  # add to frontier and move forward

    # return None  # return None if no solution is found
##############################first try
    # queue = deque()
    # visited = set()

    # queue.append((initial_state, []))

    # while queue:
    #     current_state, path = queue.popleft()

    #     if problem.is_goal(current_state):
    #         return path + [current_state]

    #     visited.add(current_state)

    #     for action in problem.get_actions(current_state):
    #         next_state = problem.apply_action(current_state, action)
    #         if next_state not in visited:
    #             queue.append((next_state, path + [current_state]))

    # return None

def DepthFirstSearch(problem: Problem[S, A], initial_state: S) -> Solution:
    #TODO: ADD YOUR CODE HERE
    # Initialize sets and lists
    explored = set()  # to store explored states
    frontier = [initial_state]  # to store states for DFS
    parents = {initial_state: ('null', initial_state)}  # to store parents of each node

    # Initialize path variables
    pathe = []  # to store action path
    path = []  # to store states path

    # Main DFS loop
    while frontier:
        # Get the last state in the LIFO stack
        node = frontier.pop(-1)

        # Check if the node has not been explored yet
        if node not in explored:
            explored.add(node)  # mark node as explored
        else:
            continue  # skip to the next iteration if the node has already been explored

        # Check if the goal is reached
        if problem.is_goal(node):
            if flag == 0:
                # Initialize parent of the current child
                path.append(node)
                new_node = path[0]
                parent = parents[new_node]
                prev = parent[0]

                # Reconstruct the path by backtracking through parents
                while prev != initial_state:
                    path.append(prev)  # append the state
                    parent = parents[prev]  # for looping
                    prev = parent[0]

                path.reverse()  # reverse the path to get the correct order

                # Return the path or path of actions based on the flag
                return path if flag == 0 else [parents[node][1]] + path

            else:
                # Reconstruct the action path for suko case
                parent_tuple = parents[node]  # parent of that child
                parent = parent_tuple[0]
                actioon = parent_tuple[1]
                while parent != 'null':
                    pathe.append(actioon)
                    parent_tuple = parents[parent]
                    parent = parent_tuple[0]
                    actioon = parent_tuple[1]

                pathe.reverse()  # reverse the path to get the correct order
                return pathe

        # Loop over possible actions from a state
        for action in problem.get_actions(node):
            # Get the successor of the current node
            child = problem.get_successor(node, action)
            flag = 0 if child == action else 1  # flag to distinguish between graph and suko

            # Check if the child is a new state
            if child not in explored:
                parents[child] = (node, action)  # initialize parent
                frontier.append(child)  # add to frontier and move forward

    return None  # return None if no solution is found
    

def UniformCostSearch(problem: Problem[S, A], initial_state: S) -> Solution:
    #TODO: ADD YOUR CODE HERE
    # Initialize sets, dictionaries, and priority queue
    explored = {}       # Dictionary to store explored states and their costs
    exploredOrder = {}  # Dictionary to store the order in which states are explored
    order = 0           # Initialize order
    pathe = []          # List to store action path
    frontier = queue.PriorityQueue()  # Priority queue for UCS
    frontier.put((0, order, initial_state))  # Put initial state in the priority queue
    parents = {initial_state: ('null', initial_state)}  # Dictionary to store parents of each node

    while not frontier.empty():
        # Dequeue the item with the highest priority (lowest cost)
        dequeued_item = frontier.get()
        node = dequeued_item[2]       # Get the node from the dequeued item
        node_priority = dequeued_item[0]  # Get the priority (cost) of the node

        if problem.is_goal(node):
            if flag == 0:
                # Reconstruct the path for graph search
                path = [node]           # Initialize the path list with the current node
                prev = node              # Set the previous node to the current node

                while prev != initial_state:
                    parent = parents[prev][0]   # Get the parent of the current node
                    path.append(parent)         # Append the parent to the path
                    prev = parent               # Update the previous node to be the parent

                path.reverse()                 # Reverse the path to get the correct order
                path.pop(0)                    # Remove the initial state from the path
                return path                    # Return the reconstructed path

            else:
                # Reconstruct the action path for suko search
                parent_tuple = parents[node]    # Get the tuple (parent, action) for the current node
                parent = parent_tuple[0]        # Get the parent from the tuple
                action = parent_tuple[1]        # Get the action from the tuple

                while parent != 'null':
                    pathe.append(action)        # Append the action to the path
                    parent_tuple = parents[parent]  # Get the tuple (parent, action) for the parent
                    parent = parent_tuple[0]    # Get the parent from the tuple
                    action = parent_tuple[1]    # Get the action from the tuple

                pathe.reverse()                 # Reverse the path to get the correct order
                return pathe                    # Return the reconstructed action path

        else:
            for action in problem.get_actions(node):
                child = problem.get_successor(node, action)

                if child == action:
                    flag = 0  # Graph
                else:
                    flag = 1  # Suko

                frontier_list = list(frontier.queue)

                if child not in explored:
                    # Add child to explored set
                    explored[child] = node_priority + problem.get_cost(child, action)
                    order += 1
                    exploredOrder[child] = order
                    parents[child] = (node, action)
                    frontier.put((node_priority + problem.get_cost(child, action), order, child))

                elif does_exist(frontier_list, child):
                    # Check if child is in the frontier and has a lower cost
                    if node_priority + problem.get_cost(child, action) < explored[child]:
                        # Remove the existing item from the frontier
                        frontier.queue.remove((explored[child], exploredOrder[child], child))
                        # Put the updated item with lower cost in the frontier
                        frontier.put((node_priority + problem.get_cost(child, action), order, child))
                        parents[child] = (node, action)

    #return None

def does_exist(flist: list, child_node: S) -> bool:
    # Check if child_node exists in the frontier list
    for item in flist:
        if item[2] == child_node:
            return True
        else:
            continue
    return False
# End of does_exist function
    

def AStarSearch(problem: Problem[S, A], initial_state: S, heuristic: HeuristicFunction) -> Solution:
    #TODO: ADD YOUR CODE HERE
    # Set to keep track of explored states
    explored = set()
    # Dictionary to store the order of exploration for each state
    exploredOrder = {}
    # Counter to track the order of exploration
    order = 0
    # Lists to store the final path
    pathe = []
    # Dictionary to store the cost of reaching each state
    explored = {}
    explored[initial_state] = 0
    # Dictionary to store the order of exploration for each state
    exploredOrder[initial_state] = 0
    # Priority queue (min heap) to maintain the frontier of states to explore
    frontier = queue.PriorityQueue()
    frontier.put((0, order, initial_state))
    # Dictionary to store the parent of each state in the final path
    parents = {initial_state: ('null', initial_state)}
    # List to store the final path
    path = []
    # Main loop for exploring states in the priority queue
    while not frontier.empty():
    # Dequeue the item with the highest priority (lowest cost)
        dequeued_item = frontier.get()
        node = dequeued_item[2]
        nodePri = dequeued_item[0]
    # Check if the goal state is reached
        if problem.is_goal(node):
            if flag == 0:
                 # Reconstruct the path for graph search
                path.append(node)
                curr = path[0]
                parent = parents[curr]
                prev = parent[0]

                while prev != 'null':

                    path.append(prev)
                    parent = parents[prev]
                    prev = parent[0]

                path.reverse()
                path.pop(0)
                return path

            else:
                parent_tuple = parents[node]  # parent of that child
                parent = parent_tuple[0]
                actioon = parent_tuple[1]
                while parent != 'null':
                    # getting parent of the node called parent "originally was child"
                    pathe.append(actioon)
                    # parent is a key tuple and we want it equal to first element only
                    parent_tuple = parents[parent]
                    parent = parent_tuple[0]
                    actioon = parent_tuple[1]
                pathe.reverse()
                return pathe

        else:
            # Explore the successors of the current state
            for action in problem.get_actions(node):
                child = problem.get_successor(node, action)
                if child == action:
                    flag = 0  # graph
                else:
                    flag = 1  # dung
                frontierlist = list(frontier.queue)
                 # Check if the child is not explored and not in the frontier
                if child not in explored and not frontier.queue.__contains__(child):
                    # Update the cost and order of exploration for the child
                    explored[child] = problem.get_cost(
                        child, action) + heuristic(problem, child)
                    order += 1
                    exploredOrder[child] = order
                     # Record the parent and add the child to the frontier
                    parents[child] = (node, action)
                    frontier.put(
                        (heuristic(problem, child)+problem.get_cost(child, action) + heuristic(problem, child), order, child))

                elif does_exist(frontierlist, child):
                     # If the child is in the frontier and has a lower cost, update its information
                    if (problem.get_cost(child, action) + heuristic(problem, child)) < explored[child]:

                        frontier.queue.remove(
                            (explored[child], exploredOrder[child], child))
                        frontier.put(
                            (problem.get_cost(child, action) + heuristic(problem, child)), order, child)

                        parents[child] = (node, action)

        # return None


def does_exist(flist: list, child_node: S) -> bool:
    # Function to check if a node exists in the frontier
    for item in flist:
        if item[2] == child_node:
            return True
        else:
            continue
    return False
# end of does_exist function

def BestFirstSearch(problem: Problem[S, A], initial_state: S, heuristic: HeuristicFunction) -> Solution:
    #TODO: ADD YOUR CODE HERE
    # Initialize sets and variables for explored states and their order
    explored = set()
    exploredOrder = {}
    order = 0

    # Initialize lists for storing the action and state paths
    pathe = []

    # Initialize a dictionary for explored states and their cost
    explored = {}  # Redundant variable name; consider renaming
    explored[initial_state] = 0
    exploredOrder[initial_state] = 0

    # Initialize priority queue for frontier states and set the initial state
    frontier = queue.PriorityQueue()
    frontier.put((0, order, initial_state))

    # Initialize dictionary for storing parent information
    parents = {initial_state: ('null', initial_state)}

    while not frontier.empty():

        dequeued_item = frontier.get()
        node = dequeued_item[2]
        nodePri = dequeued_item[0]
        if problem.is_goal(node):
            if flag == 0:
                path = [node]
                prev = node

                while prev != initial_state:
                    parent = parents[prev][0]
                    path.append(parent)
                    prev = parent

                path.reverse()
                path.pop(0)
                return path

            else:
                parent_tuple = parents[node]  # parent of that child
                parent = parent_tuple[0]
                actioon = parent_tuple[1]
                while parent != 'null':
                    # getting parent of the node called parent "originally was child"
                    pathe.append(actioon)
                    # parent is a key tuple and we want it equal to first element only
                    parent_tuple = parents[parent]
                    parent = parent_tuple[0]
                    actioon = parent_tuple[1]
                # end of while

                pathe.reverse()
                return pathe

        else:

            for action in problem.get_actions(node):

                child = problem.get_successor(node, action)
                if child == action:
                    flag = 0  # graph
                else:
                    flag = 1  # dung
                frontierlist = list(frontier.queue)
                if child not in explored:
                    # explored.add(child)
                    explored[child] = problem.get_cost(
                        child, node)+heuristic(problem, child)
                    order += 1
                    exploredOrder[child] = order
                    parents[child] = (node, action)
                    frontier.put(
                        (problem.get_cost(child, node)+heuristic(problem, child), order, child))

                elif does_exist(frontierlist, child):
                    if problem.get_cost(child, node)+heuristic(problem, child) < explored[child]:

                        frontier.queue.remove(
                            (explored[child], exploredOrder[child], child))
                        frontier.put(
                            (problem.get_cost(child, node)+heuristic(problem, child), order, child))

                        parents[child] = (node, action)

        # return None

def does_exist(flist: list, child_node: S) -> bool:
    # check
    for item in flist:
        if item[2] == child_node:
            return True
        else:
            continue
    return False