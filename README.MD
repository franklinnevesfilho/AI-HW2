# Artificial Intelligence - Homework 2

### Problem 1: Count the Islands
#### Question 1: Implement
##### Pseudo Code

```
function bfs(grid, i, j):
    # create a queue and add the current cell to it
    queue = [(i, j)]
    
    # while queue is not empty
    while queue is not empty:
        # get the current cell
        i, j = queue.pop(0)
        
        # check if current cell is out of bounds or is water
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            continue
            
        # set current cell to 0
        grid[i][j] = 0
        
        # add all 4 directions to the queue
        queue.append((i + 1, j))
        queue.append((i - 1, j))
        queue.append((i, j + 1))
        queue.append((i, j - 1))


function dfs(grid, i, j):

    # check if current cell is out of bounds or is water
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
        return
    # set current cell to 0
    grid[i][j] = 0
    
    # recursively call dfs on all 4 directions
    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)


# this function will count the number of islands in the grid
function count_islands(grid=None, method='dfs'):
    
    # if grid is not provided, make a copy of the island_map
    if grid is None:
        grid = [row.copy() for row in island_map]
    
    # make sure the only methods allowed are 'dfs' and 'bfs'
    if method not in ['dfs', 'bfs']:
        raise ValueError("Method must be either 'dfs' or 'bfs'")

       # initialize count to 0
    count = 0
    
    # iterate through the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                count += 1
                if method == 'dfs':
                    _dfs(grid, i, j)
                elif method == 'bfs':
                    _bfs(grid, i, j)

    return count
```

##### Time Complexity
The time complexity of the above algorithm is O(m * n) where m is the number of rows and n is the number of columns in the grid. This is because we are iterating through each cell in the grid and performing a constant amount of work for each cell.

##### Space Complexity
The space complexity of the above algorithm is O(m * n) where m is the number of rows and n is the number of columns in the grid. This is because we are using a queue to store the cells to visit and the queue can grow to be as large as the number of cells in the grid.

#### Question 2: Analyze
The above algorithm uses either Depth First Search (DFS) or Breadth First Search (BFS) to count the number of islands in a grid. 
The algorithm works by iterating through each cell in the grid and if the cell is land, it increments the count of islands and then performs a DFS or BFS on that cell to mark all the cells on that island as visited. 
The algorithm then continues to iterate through the grid until all cells have been visited.

Although both methods work, DFS is more efficient in this case because it is a simpler algorithm and does not require the use of a queue.

#### Question 3:
Counting the islands manually does match the output of both algorithms. The output of the algorithms is 17, which is the correct number of islands in the grid.


### Problem 2: 8-Puzzle Game

#### Question 1: Implement

##### Heuristic explanation
The heuristic function used in the A* algorithm is the Manhattan distance. The Manhattan distance is the sum of the absolute differences of the x and y coordinates of the current state and the goal state. It is a good heuristic for the 8-puzzle problem because it is admissible and consistent. The Manhattan distance is admissible because it never overestimates the cost to reach the goal state. It is consistent because the cost of moving from one state to another is always greater than or equal to the Manhattan distance between the two states.

##### Psuedo Code

```
function bfs(start, goal):
    # create a queue and add the start state to it
    queue = [(start, [])]
    
    # create a set to store visited states
    visited = set()
    
    # while queue is not empty
    while queue:
        # get the current state and path
        state, path = queue.pop(0)
        
        # check if current state is the goal state
        if state == goal:
            return path
        
        # add current state to visited set
        visited.add(state)
        
        # get the possible moves from the current state
        moves = get_moves(state)
        
        # iterate through the possible moves
        for move, direction in moves:
            # get the new state after making the move
            new_state = make_move(state, move)
            
            # if the new state has not been visited
            if new_state not in visited:
                # add the new state and path to the queue
                queue.append((new_state, path + [direction]))
    
    return None
```

##### Complexity Analysis
The time complexity of the above algorithm is O(b^d) where b is the branching factor (number of possible moves) and d is the depth of the search tree. In the worst case, the algorithm will explore all possible states until it finds the goal state.