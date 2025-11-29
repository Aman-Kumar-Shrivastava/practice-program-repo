import queue

def createmaze():
    maze = []
    maze.append(["#","#","#","#","#","#","#","#","o","#"])
    maze.append(["#"," "," "," ","#"," "," "," "," ","#"])
    maze.append(["#"," ","#"," ","#"," ","#","#","#","#"])
    maze.append(["#"," ","#"," "," "," "," ","#","#","#"])
    maze.append(["#"," ","#","#","#","#"," ","#","#","#"])      
    maze.append(["#"," "," "," "," ","#"," "," ","#","#"])
    maze.append(["#","#","#","#"," ","#","#","#"," ","#"])  
    maze.append(["#"," "," ","#"," "," "," ","#"," ","#"])
    maze.append(["#"," ","#","#","#","#"," "," "," ","#"])
    maze.append(["#","#","#","#","#","#","#","#","x","#"])
    return maze


def createmaze2():
    maze = []
    maze.append(["#","#","#","#","#","#","#","#","o","#"])
    maze.append(["#"," "," "," ","#"," ","#","#"," ","#"])
    maze.append(["#"," ","#"," ","#"," ","#","#"," ","#"])
    maze.append(["#"," ","#"," "," "," "," ","#"," ","#"])
    maze.append(["#"," ","#","#","#","#"," ","#"," ","#"])      
    maze.append(["#"," "," "," "," ","#"," "," "," ","#"])
    maze.append(["#","#","#","#"," ","#","#","#","#","#"])  
    maze.append(["#"," "," ","#"," "," "," ","#"," ","#"])
    maze.append(["#"," ","#","#","#","#"," "," "," ","#"])
    maze.append(["#","#","#","#","#","#","#","#","x","#"])
    return maze


def printmaze(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "o":
            start = x
   
    i = start
    j = 0
    pos_set = set()

    for move in moves:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1
        pos_set.add((i, j))
   
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (i, j) in pos_set:
                print(".", end="")
            else:
                print(col, end="")
        print()


def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "o":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1

        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif maze[j][i] == "#":
            return False
    return True


def findend(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "o":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1

    if maze[j][i] == "x":
        print("Found:", moves)
        printmaze(maze, moves)
        return True
    return False


# Main BFS Part
nums = queue.Queue()
nums.put("")
add = ""
maze = createmaze2()

while not findend(maze, add):
    add = nums.get()
    for move in ["L", "R", "U", "D"]:
        newmove = add + move
        if valid(maze, newmove):
            nums.put(newmove)
