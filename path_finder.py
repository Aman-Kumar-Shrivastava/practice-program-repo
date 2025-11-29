import queue

def createMaze():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "#", "#", "#", "o", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", " ", "#", "#", "#"])
    maze.append(["#", " ", "#", "#", "#", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", " ", "#", " ", " ", " ", "#"])
    maze.append(["#", "#", "#", "#", " ", "#", "#", "#", "#", "#"])
    maze.append(["#", " ", " ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", "#", "#", "#", " ", " ", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "#", "#", "#", "x", "#"])
    return maze


def printMaze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "o":
            start = x

    i, j = start, 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1
        pos.add((i, j))

    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (i, j) in pos:
                print(".", end="")
            else:
                print(col, end="")
        print()


def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "o":
            start = x

    i, j = start, 0
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


def findEnd(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "o":
            start = x

    i, j = start, 0
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
        printMaze(maze, moves)
        return True
    return False


# Main BFS solver
maze = createMaze()
nums = queue.Queue()
nums.put("")
add = ""

while not findEnd(maze, add):
    add = nums.get()
    for move in ["L", "R", "U", "D"]:
        newMove = add + move
        if valid(maze, newMove):
            nums.put(newMove)
