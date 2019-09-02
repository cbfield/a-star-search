# a-star-search

**Data Structures Used**

frontier: I implemented the frontier as a priority queue, as this was required for A\* search to function properly

frontier_or_explored: This is a list that I created in order to keep a record of the spaces that had either been explored or placed onto the frontier. I originally tried to just keep a list of spaces that had been explored, but found it difficult to retrieve which spaces were on the frontier. Since this list serves the same purpose with less effort, I deemed it appropriate. I initiallize this list to contain the start position since it seemed safe to assume we had explored the start position initially.

current_pos: I use this tuple to keep track of which position the algorithm is working on. It is initiallized to the start position since this is the first position that the algorithm is working on.

predecessors: This is a dictionary that I created in order to keep track of which position precedes each other along the path that the algorithm is finding. Each time the algorithm considers a new position, an entry is added to the dictionary that uses the new position as the key, and the previous position as the stored value.

**Explanation of Process**

The algorithm first initiallizes the data structures mentioned above.

Then, the algorithm enters a while loop that terminates only once the goal position has been found. For each loop in the while, the algorithm considers the moves it could make from the current position. If the move is valid and the resulting space has not been added to the frontier or explored already, then the resulting space is added to the frontier queue with the cost of moving to that space as the key. The space is also added to the frontier_or_explored list for bookkeeping. Finally, the first position on the frontier queue is retrieved and investigated on the next iteration of the while loop.

The while loop continues until the current position of the agent is the goal position. At this point, the path that the agent followed to get to the goal is retrieved and returned by the function.

**Heuristic Function**

My heuristic function uses the Manhattan distance from the given position to the goal position as its approximation of the distance from the given position to the goal.

The reason I chose the Manhattan distance as my heuristic is that the agent can only move in the four cardinal directions within this world. If the agent could move in any direction along the xy-plane, I think the Euclidean distance to the goal would have been more appropriate. This is because the Manhattan distance would overestimate the distance to the goal in this scenario and therefore be unadmissible.

With the given world and possible moves, the Manhattan distance is both admissible and consistent, and therefore the best choice I can think of for a heuristic function.

**pretty_print_solution**

**Data Structures Used**

pretty_world: This is a list of lists that I use to record what move was taken from a given space. Its dimensions are equal to the dimensions of the world that is passed into the pretty_print_solution function. Each position in pretty_world is initiallized to the corresponding position in the world passed into pretty_print_solution.

move_arrows: This is a dictionary that relates the moves that the agent can take to the corresponding ASCII character.

current_pos: This is a tuple that I use to keep track of which position the algorithm is considering, as in the a_star_search algorithm.

**Explanation of Process**

The algorithm first initiallizes pretty_world and move_arrows.

It then iterates through the path that was returned by a_star_search, and prints the appropriate ASCII character in the position of pretty_world that the move was taken from. At the end of the path, it prints 'G'.

It then prints the results in the closest form I could achieve to the example given above.

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

I initially thought that this didn't need a helper since it could be contained in one line, but that line was also huge and ugly. This function determines whether a given move from a given position is both contained within the world, and does not result in the agent being on a mountain space.

**Arguments**

position: the current position of the agent in the world

world: the map the agent is traveling through

move: The move that we are testing for validity

**Returns**

move_is_valid returns true if the resulting position of the move is both within the boundaries of the world, and not a mountain.
Otherwise, it returns false.
