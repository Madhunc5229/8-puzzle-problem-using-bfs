import numpy as np
import copy 

#Locate the 0 in a given state
def locate_blank_tile(node):
    for i in range(0,3):
        for j in range(0,3):
            if node[i][j] == 0:
                return i,j

#Function to move 0 to left
def ActionMoveLeft(current_node):
    node = copy.deepcopy(current_node)
    #get blank tile location
    x,y = locate_blank_tile(node)
    #Chec if left turn is possible
    if y>0:
        # print("Moving Left")
        swap = node[x][y-1]
        node[x][y-1] = 0
        node[x][y] = swap
        return node
    else:
        return []
        # print("Left not possible")

#Function to move 0 to right
def ActionMoveRight(current_node):
    node = copy.deepcopy(current_node)
    #get blank tile location
    x,y = locate_blank_tile(node)
    #Check if right turn is possible
    if y<2:
        swap = node[x][y+1]
        node[x][y+1] = 0
        node[x][y] = swap
        return node
    else:
        return []

#Function to move 0 to up
def ActionMoveUp(current_node):
    node = copy.deepcopy(current_node)
    #get blank tile location
    x,y = locate_blank_tile(node)
    #Check if moving up is possible
    if x>0:
        swap = node[x-1][y]
        node[x-1][y] = 0
        node[x][y] = swap
        return node
    else:
        return []

#Function to move 0 to down
def ActionMoveDown(current_node):
    node = copy.deepcopy(current_node)
    #get blank tile location
    x,y = locate_blank_tile(node)
    #Check if moving down is possible
    if x<2:
        swap = node[x+1][y]
        node[x+1][y] = 0
        node[x][y] = swap
        return node
    else:
        return []

#Building the branch tree of a parent node i.e current node
def get_branches(current_node):
    branches = []
    if len(ActionMoveLeft(current_node)) != 0:
        branches.append(ActionMoveLeft(current_node))
    if len(ActionMoveRight(current_node)) != 0:
        branches.append(ActionMoveRight(current_node))
    if len(ActionMoveUp(current_node)) != 0:
        branches.append(ActionMoveUp(current_node))
    if len(ActionMoveDown(current_node)) != 0:
        branches.append(ActionMoveDown(current_node))
    
    return branches

#Function to backtrack and return the path (index)
def backtracking(parent_list, branch_list):
    
    backtracking_index = parent_list[-1]
    path = [parent_list[-1]]
    goal_reached = False
    
    while not goal_reached:
        for branches_index in branch_list:
            if backtracking_index in branches_index:
                backtracking_index = branch_list.index(branches_index)
                path.append(branch_list.index(branches_index))
        if backtracking_index == 0:
            # print("solution: ", path)
            return path

#Function to return solution states
def solution_path(visited_list,path_idx):
    solution = []
    for idx in path_idx:
        solution.append(visited_list[idx])
    return solution

#BFS Search
def bfs(initial_state, goal_node):
    visited = []
    queue = []
    visited.append(initial_state)
    queue.append(initial_state)
    parent_index_i = []
    node_index_i = []
    
    while len(queue) !=0:
        current_node = queue.pop(0)
        parent_index_i.append(visited.index(current_node))

        #Check for goal node
        if current_node == goal_node:
            print("Goal reached:", current_node)
            path_index = backtracking(parent_index_i, node_index_i)
            return (solution_path(visited, path_index[::-1])), visited, parent_index_i, node_index_i
        
        #list to store all branches index of a current node
        branch_index_i =[]

        #Loop thorugh the branches of a the current node
        for branch in get_branches(current_node):
            if branch not in visited:
                visited.append(branch)
                queue.append(branch)
                branch_index_i.append(visited.index(branch))
        node_index_i.append(branch_index_i)

#Function to convert the matrix to single line format
def column_to_line(list_of_lists):
    output_list = []
    for i in range(0,len(list_of_lists)):
        for j in range(0, len(list_of_lists[i])):
            intermediate_list = []
            for k in range(0, 3):
                for l in range(0,3):
                    intermediate_list.append(list_of_lists[i][l][k])
        output_list.append(intermediate_list)
    return output_list

#Function to generate nodePath.txt file
def node_path_txt(solution):
    f = open('nodePath.txt','w')
    for state in solution:
        f.write(str(state).replace('[','').replace(']','').replace(',','')+"\n")

#Function to generate Nodes.txt file
def Nodes_txt(Nodes):
    f = open('Nodes.txt','w')
    for state in Nodes:
        f.write(str(state).replace('[','').replace(']','').replace(',','')+"\n")

#Function to generate NodesInfo.txt file
def Nodes_info_txt(node_index):
    Parent_Index = []
    Node_Index = []
    for branches in node_index:
        for ele in branches:
            Parent_Index.append(node_index.index(branches))
            Node_Index.append(ele)
    f = open('NodesInfo.txt','w')
    f.write("Node_Index"+'\t'+'Parent_Node_index'+'\t'+'Cost'+'\n')
    for i in range(0,len(Node_Index)):
        f.write(str(Node_Index[i])+'\t'+str(Parent_Index[i])+'\t'+str(0)+'\n')


if __name__ == "__main__":

    #Test Case 1
    # initial_state = [[1,4,7],[5,0,8],[2,3,6]]

    #Test Case 2
    initial_state = [[4,7,0],[1,2,8],[3,5,6]]
    
    goal_node = [[1,4,7],[2,5,8],[3,6,0]]
    
    solution, nodes, parent_index_i, node_index_i = bfs(initial_state, goal_node)
    
    node_path_txt(column_to_line(solution))
    
    Nodes_txt(column_to_line(nodes))
    
    Nodes_info_txt(node_index_i)


