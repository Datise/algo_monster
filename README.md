# algo_monster




Notes
DFS For combinatorial problems, finding nodes far away from root. 

BFS for close/closest node problems. 

While DFS uses recursion/stack to keep track of progress, BFS uses a queue (First In First Out). When we dequeue a node, we enqueue its children.



DFS
Combinatorial problems often implies DFS/backtracking or DFS with state 

def dfs(start_index, path, [...additional states]):
    if is_leaf(start_index):
        ans.append(path[:]) # add a copy of the path to the result
        return
    for edge in get_edges(start_index, [...additional states]):
        # prune if needed
        if not is_valid(edge):
            continue
        path.add(edge)
        if additional states:
            update(...additional states)
        dfs(start_index + len(edge), path, [...additional states])
        # revert(...additional states) if necessary e.g. permutations
        path.pop()



BFS 

# add root to queue
# loop while there's something in the queue
    # keep track of level/result if need be 
    # loop through queue length
        # pop queue item 
        # loop through add children
    # append result  
# return result  

GRAPHS 
BFS
When: shortest path from a to b (unweight), graph of unknown or infinite size (knight shortest path), Dijkstra intro (shortest path in a weighted graph)

Same but keep track of visited nodes
# create queue
# create visited 
# set level to 0 
# loop over queue
    # loop over length of queue
        # remove node 
        # loop over neighbours
            # if neighbour is visited skip
            # append neighbour to queue
            # add neighbour to visited 
    # increment levles 

DFS 
same but keep track of visited

BFS is better at:

    finding the shortest distance between two vertices
    graph of unknown size, e.g. word ladder, or even infinite size, e.g. knight shortest path

DFS is better at:

    uses less memory than BFS for wide graphs (that is, graphs with large breadth factors), since BFS has to keep all the nodes in the queue, and for wide graphs, this can be quite large.
    finding nodes far away from the root, e.g., looking for an exit in a maze.
