# Maze solver (BFS) — Developed by Aman Shrivastava
from collections import deque
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

def find_start(maze):
    for j, row in enumerate(maze):
        for i, val in enumerate(row):
            if val == "o":
                return i, j
    raise ValueError("Start position 'o' not found in maze.")

def print_maze_with_path(maze, path_positions):
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (i, j) in path_positions:
                print(".", end="")
            else:
                print(col, end="")
        print()


def neighbors(i, j):
    return [
        (i - 1, j, "L"),
        (i + 1, j, "R"),
        (i, j - 1, "U"),
        (i, j + 1, "D"),
    ]



def bfs_solve(maze):
    start_i, start_j = find_start(maze)
    q = deque()
    q.append((start_i, start_j, ""))  
    visited = set()
    visited.add((start_i, start_j))

    while q:
        i, j, path = q.popleft()
        if maze[j][i] == "x":
            pi, pj = start_i, start_j
            path_positions = set()
            for mv in path:
                if mv == "L": pi -= 1
                elif mv == "R": pi += 1
                elif mv == "U": pj -= 1
                elif mv == "D": pj += 1
                path_positions.add((pi, pj))
            return True, path, path_positions

        for ni, nj, mv in neighbors(i, j):
            if not (0 <= ni < len(maze[0]) and 0 <= nj < len(maze)):
                continue
            if maze[nj][ni] == "#":
                continue
            if (ni, nj) in visited:
                continue

            visited.add((ni, nj))
            q.append((ni, nj, path + mv))

    return False, None, None

if __name__ == "__main__":
    print("====================================")
    print("   MAZE SOLVER - BFS Approach     ")
    print("   Developed by Aman Shrivastava  ")
    print("====================================\n")

    maze = createMaze()
    found, moves, path_positions = bfs_solve(maze)

    if found:
        print("Path found!")
        print("Moves:", moves)
        print("\nSolved Maze:\n")
        print_maze_with_path(maze, path_positions)
    else:
        print("No path found from start to exit.")
