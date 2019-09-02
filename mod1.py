
#Our "worlds", in which the agent will search for the goal
full_world = [
  ['.', '.', '.', '.', '.', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', '.', '.', '.', '.', '*', '*', '*', '*', '*', '*', '*', '*', '*', '.', '.', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '.', '.'], 
  ['.', '.', '.', '.', 'x', 'x', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', 'x', 'x', 'x', '#', '#', '#', 'x', 'x', '#', '#'], 
  ['.', '.', '.', '.', '#', 'x', 'x', 'x', '*', '*', '*', '*', '~', '~', '*', '*', '*', '*', '*', '.', '.', '#', '#', 'x', 'x', '#', '.'], 
  ['.', '.', '.', '#', '#', 'x', 'x', '*', '*', '.', '.', '~', '~', '~', '~', '*', '*', '*', '.', '.', '.', '#', 'x', 'x', 'x', '#', '.'], 
  ['.', '#', '#', '#', 'x', 'x', '#', '#', '.', '.', '.', '.', '~', '~', '~', '~', '~', '.', '.', '.', '.', '.', '#', 'x', '#', '.', '.'], 
  ['.', '#', '#', 'x', 'x', '#', '#', '.', '.', '.', '.', '#', 'x', 'x', 'x', '~', '~', '~', '.', '.', '.', '.', '.', '#', '.', '.', '.'], 
  ['.', '.', '#', '#', '#', '#', '#', '.', '.', '.', '.', '.', '.', '#', 'x', 'x', 'x', '~', '~', '~', '.', '.', '#', '#', '#', '.', '.'], 
  ['.', '.', '.', '#', '#', '#', '.', '.', '.', '.', '.', '.', '#', '#', 'x', 'x', '.', '~', '~', '.', '.', '#', '#', '#', '.', '.', '.'], 
  ['.', '.', '.', '~', '~', '~', '.', '.', '#', '#', '#', 'x', 'x', 'x', 'x', '.', '.', '.', '~', '.', '#', '#', '#', '.', '.', '.', '.'], 
  ['.', '.', '~', '~', '~', '~', '~', '.', '#', '#', 'x', 'x', 'x', '#', '.', '.', '.', '.', '.', '#', 'x', 'x', 'x', '#', '.', '.', '.'], 
  ['.', '~', '~', '~', '~', '~', '.', '.', '#', 'x', 'x', '#', '.', '.', '.', '.', '~', '~', '.', '.', '#', 'x', 'x', '#', '.', '.', '.'], 
  ['~', '~', '~', '~', '~', '.', '.', '#', '#', 'x', 'x', '#', '.', '~', '~', '~', '~', '.', '.', '.', '#', 'x', '#', '.', '.', '.', '.'], 
  ['.', '~', '~', '~', '~', '.', '.', '#', '*', '*', '#', '.', '.', '.', '.', '~', '~', '~', '~', '.', '.', '#', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', '.', 'x', '.', '.', '*', '*', '*', '*', '#', '#', '#', '#', '.', '~', '~', '~', '.', '.', '#', 'x', '#', '.', '.', '.'], 
  ['.', '.', '.', 'x', 'x', 'x', '*', '*', '*', '*', '*', '*', 'x', 'x', 'x', '#', '#', '.', '~', '.', '#', 'x', 'x', '#', '.', '.', '.'], 
  ['.', '.', 'x', 'x', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', 'x', 'x', 'x', '.', '.', 'x', 'x', 'x', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', 'x', 'x', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', 'x', 'x', 'x', 'x', '.', '.', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', 'x', 'x', 'x', '*', '*', '*', '*', '*', '*', '*', '*', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.'], 
  ['.', '.', '.', '.', 'x', 'x', 'x', '*', '*', '*', '*', '*', '*', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '~', '~', '~', '~'], 
  ['.', '.', '#', '#', '#', '#', 'x', 'x', '*', '*', '*', '*', '*', '.', 'x', '.', '.', '.', '.', '.', '~', '~', '~', '~', '~', '~', '~'], 
  ['.', '.', '.', '.', '#', '#', '#', 'x', 'x', 'x', '*', '*', 'x', 'x', '.', '.', '.', '.', '.', '.', '~', '~', '~', '~', '~', '~', '~'], 
  ['.', '.', '.', '.', '.', '.', '#', '#', '#', 'x', 'x', 'x', 'x', '.', '.', '.', '.', '#', '#', '.', '.', '~', '~', '~', '~', '~', '~'], 
  ['.', '#', '#', '.', '.', '#', '#', '#', '#', '#', '.', '.', '.', '.', '.', '#', '#', 'x', 'x', '#', '#', '.', '~', '~', '~', '~', '~'], 
  ['#', 'x', '#', '#', '#', '#', '.', '.', '.', '.', '.', 'x', 'x', 'x', '#', '#', 'x', 'x', '.', 'x', 'x', '#', '#', '~', '~', '~', '~'], 
  ['#', 'x', 'x', 'x', '#', '.', '.', '.', '.', '.', '#', '#', 'x', 'x', 'x', 'x', '#', '#', '#', '#', 'x', 'x', 'x', '~', '~', '~', '~'], 
  ['#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '#', '#', '#', '.', '.', '.', '.', '#', '#', '#', '.', '.', '.']]
test_world = [
  ['.', '*', '*', '*', '*', '*', '*'],
  ['.', '*', '*', '*', '*', '*', '*'],
  ['.', '*', '*', '*', '*', '*', '*'],
  ['.', '.', '.', '.', '.', '.', '.'],
  ['*', '*', '*', '*', '*', '*', '.'],
  ['*', '*', '*', '*', '*', '*', '.'],
  ['*', '*', '*', '*', '*', '*', '.']]

#Defining the costs to move to certain spaces within the world
costs = { '.': 1, '*': 3, '#': 5, '~': 7}

#Defining the cardinal directions the agent can move
cardinal_moves = [(0,-1), (1,0), (0,1), (-1,0)]

def find_path_cost(world, position, start, costs, predecessors):
    cost = costs[world[position[1]][position[0]]]
    while position != start:
        last_pos = predecessors[position]
        cost += costs[world[last_pos[1]][last_pos[0]]]
        position = last_pos
    return cost

def retrace_path(position, start, predecessors):
    move_list = []
    while position != start:
        last_pos = predecessors[position]
        move_list.insert(0, (position[0] - last_pos[0],position[1] - last_pos[1]))
        position = last_pos
    return move_list

def move_is_valid(position, world, move):
    within_x_bounds = 0 <= position[0] + move[0] < len(world[0])
    within_y_bounds = 0 <= position[1] + move[1] < len(world) 
    
    return within_x_bounds and within_y_bounds and world[position[1] + move[1]][position[0] + move[0]] != 'x'

def a_star_search( world, start, goal, costs, moves, heuristic):
    
    frontier = PriorityQueue()
    frontier_or_explored = [start]
    current_pos = start
    predecessors = {}
    
    while current_pos != goal:
        for move in moves:
            next_pos = (current_pos[0] + move[0],current_pos[1] + move[1])
            if move_is_valid(current_pos, world, move) and next_pos not in frontier_or_explored:
                cost = find_path_cost(world, current_pos, start, costs, predecessors) + heuristic(current_pos, goal)
                frontier.put((cost, next_pos))
                predecessors.update({next_pos: current_pos})
                frontier_or_explored.append(next_pos)
        current_pos = frontier.get()[1]
        
    return retrace_path(current_pos, start, predecessors)

def pretty_print_solution( world, path, start):
    
    pretty_world = world
    
    move_arrows = {(0,-1):"^", (1,0):">", (0,1):"v", (-1,0):"<"}
    
    current_pos = start
    for index in range(len(path)):
        pretty_world[current_pos[1]][current_pos[0]] = move_arrows[path[index]]
        current_pos = (current_pos[0] + path[index][0], current_pos[1] + path[index][1])
    pretty_world[current_pos[1]][current_pos[0]] = 'G'
    
    for row in pretty_world:
        for pos in row:
            print(pos, end='')
        print()
    
    return None

def heuristic(pos, goal_pos):
    manhattan_distance = abs(goal_pos[1] - pos[1]) + abs(goal_pos[0] - pos[0])
    return manhattan_distance

test_path = a_star_search( test_world, (0, 0), (6, 6), costs, cardinal_moves, heuristic)
print( test_path)

pretty_print_solution( test_world, test_path, (0, 0))

full_path = a_star_search( full_world, (0, 0), (26, 26), costs, cardinal_moves, heuristic)
print( full_path)

pretty_print_solution( full_world, full_path, (0, 0))