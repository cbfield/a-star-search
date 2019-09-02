
# A* Search
This is a basic implementation of the A* Search algorithm. The psuedocode of this algorithm is as follows:

```
1 place initial state on frontier
2 initialize explored list
3 while frontier is not empty
4 		current-state := next state on frontier
5 		return path( current-state) if is-terminal( current-state)
6 		children := successors( current-state)
7 		for each child in children
8 		add child to frontier if not on explored or frontier
9 		add current-state to explored
10 return nil
```

**Data Structures Used**

frontier: The frontier (or nodes forming the boundary of the currently explored area) is implemented as a priority queue.

frontier_or_explored: This is a list that I created in order to keep a record of the spaces that had either been explored or placed onto the frontier. I originally tried to just keep a list of spaces that had been explored, but found it difficult to retrieve which spaces were on the frontier. Since this list serves the same purpose with less effort, I deemed it appropriate. 

current_pos: I use this tuple to keep track of which position the algorithm is working on. It is initialized to the start position.

predecessors: This dictionary is used to keep track of the succession of positions explored by the algorithm. Each time the algorithm considers a new position, an entry is added to the dictionary that uses the new position as the key, and the previous position as the value.

**Explanation of Process**

The algorithm first initializes the data structures mentioned above.

Then the algorithm enters a while loop that terminates only once the goal position has been found. For each iteration of the while loop, the algorithm considers the moves it could make from the current position. If a move is valid and the resulting position has not already been explored or added to the frontier, then that position is added to the frontier. The space is also added to the frontier_or_explored list for bookkeeping. Finally, the first position on the frontier queue is retrieved and investigated on the next iteration of the while loop.

The while loop continues until the current position of the agent is the goal position. At this point, the path that the agent followed to get to the goal is retrieved and returned by the function.

**Heuristic Function**

The optimality of A* Search comes from its combination of a greedy search (lowest cost adjacent space) and an admissible and consistent heuristic function. In this case, the heuristic function is Manhattan distance from the agent to the goal. Manhattan distance was chosen because the agent is only capable of moving in four cardinal directions, which perfectly fits that metric. If the agent were moving within a continuous space, Euclidean distance would have been more appropriate.

# Helper Functions

## find_path_cost
In order to use A\* search, we need both the cost to get from the start position to a given position, and an approximate cost to get to the goal position from there. We already have a heuristic to get the approximate cost to get to the goal. This is the other part.

**Arguments**

world: the map the agent is traveling through
position: the current position of the agent
start: the given start position in the world
costs: the given cost dictionary of moving through any space in the world
predecessors: a dictionary created in the a_star_search function that records the predecessor of each visited position

**Returns**

cost: the cost to get from the start position to the given position

## retrace_path
This function is run at the end of the a_star_search function, after it reaches the goal position. retrace_path starts at the goal position, and goes to the predecessor of each position until it finds the start again. As it does this, each position is added to the front of a new list, move_list. move_list is the path that a_star_search was looking for.

**Arguments**

position: The position of the agent in the world. This is always initially the goal position.
start: The start position in the world
predecessors: a dictionary created in the a_star_search function that records the predecessor of each visited position

**Returns**

move_list: This is the path that the algorithm found from the start position to the end position

## move_is_valid
This function determines whether a given move from a given position is both contained within the world, and does not result in the agent being on a mountain (impassable) space.

**Arguments**

position: the current position of the agent in the world
world: the map the agent is traveling through
move: The move that we are testing for validity

**Returns**

move_is_valid returns true if the resulting position of the move is both within the boundaries of the world, and not a mountain. Otherwise, it returns false.