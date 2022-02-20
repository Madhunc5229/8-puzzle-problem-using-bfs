# 8-puzzle-problem-using-bfs
8 puzzle problem solved using BFS search algorithm

Given an input and goal state of 8-puzzle problem conatining numbers from 0 to 8, this program provides the solution steps taken to reach goal state from initial state.

As there might be many unsolvable states, I have included two test cases for which the solution exists. Please use the test cases to validate the code.

To run this program:

`gitclone https://github.com/Madhunc5229/8-puzzle-problem-using-bfs`  
``cd 8-puzzle-problem-using-bfs``  
``SourceCode.py``  


This program will generate three text files to understand the solution process.

### Textfile 1:​
Name: nodePath.txt​

The elements are being stored column-wise, i.e. for this state 1 4 7 2 5 8 3 6 0, the eight puzzle state is​
1 2 3​
4 5 6​
7 8 0​
The order of the states is from start node to the goal node.

### Textfile 2:​
Name: NodesInfo.txt​
First column: Node Index​
Second Column: Parent Node Index

### Textfile 3:​
Name: Nodes.txt​
This file contains all the explored states/nodes visited while solving the puzzle.
