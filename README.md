# algo_monster




Notes


Combinatorial problems often implies DFS/backtracking or DFS with state 


The basic solution is: 
 function dfs(start_index, path):
   if is_leaf(start_index):
     report(path)
     return

   for edge in get_edges(start_index):
     path.add(edge)
     dfs(start_index + 1, path)
     path.pop()

With a state tracking

function dfs(start_index, path):
    if is_leaf(start_index):
        report(path)
    return
    for edge in get_edges(start_index):
        # prune if needed
        if not is_valid(edge):
            continue
        path.add(edge)
        # increment start_index
        dfs(start_index + len(edge), path)
        path.pop()


With multiple states:
ans = []

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