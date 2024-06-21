import random

def generate_path(N, M):
    maze = {}
    current_position = (0, 0)

    while current_position != (N - 1, M - 1):
        maze[current_position] = 2
        valid_moves = []

        if current_position[0] + 1 < N:
            valid_moves.append((current_position[0] + 1, current_position[1]))
        if current_position[1] + 1 < M:
            valid_moves.append((current_position[0], current_position[1] + 1))

        next_position = random.choice(valid_moves)
        current_position = next_position

    maze[current_position] = 2
    return maze

def add_obstacles(maze, min_obstacles, N, M):
    obstacles_added = 0

    while obstacles_added < min_obstacles:
        row = random.randint(0, N - 1)
        col = random.randint(0, M - 1)

        if (row, col) not in maze or maze[(row, col)] == 0:
            maze[(row, col)] = 1
            obstacles_added += 1

def set_obstacle(maze, N, M):
    try:
        print("Enter the coordinates to set an obstacle (i, j): ")
        row, col = map(int, input().split(","))

        if row == 1 and col == 1:
            print("Obstacle cannot be placed on the path.")
        elif row < 0 or row >= N or col < 0 or col >= M:
            raise KeyError
        elif maze[(row, col)] == 2:
            print("Obstacle cannot be placed on the path.")
        elif maze[(row, col)] == 1:
            print("Obstacle already exists at this location.")
        else:
            maze[(row, col)] = 1
            print(f"Obstacle placed at ({row}, {col})")

    except ValueError:
        print("ValueError in set_obstacle function. Need to be coordinates.")
    except KeyError:
        print("KeyError in set_obstacle function. 'Invalid coordinates, Please input coordinates within the range.'")

def remove_obstacle(maze, N, M):
    try:
        print("Enter the coordinate to remove an obstacle (i,j): ")
        row, col = map(int, input().split(","))

        if row < 0 or row >= N or col < 0 or col >= M:
            raise KeyError

        if maze[(row, col)] == 2:
            print("Obstacle does not exist on the path.")
        elif maze[(row, col)] == 0:
            print("Obstacle does not exist at this location.")
        else:
            maze[(row, col)] = 0
            print(f"Obstacle removed at ({row}, {col})")

    except ValueError:
        print("ValueError in remove_obstacle function. Need to be coordinates.")
    except KeyError:
        print("KeyError in remove_obstacle function. 'Invalid coordinates, Please input coordinates within the range.'")

def print_maze(maze, N, M):
    for row in range(N):
        for col in range(M):
            if (row, col) not in maze:
                print("   ", end="")
            elif maze[(row, col)] == 0:
                print("   ", end="")
            elif maze[(row, col)] == 1:
                print(" X ", end="")
            elif maze[(row, col)] == 2:
                print(" O ", end="")
        print()
import random

#generate path in the maze
def generate_path(N, M):
    maze = {}
    current_position = (0, 0)

    while current_position != (N - 1, M - 1):
        maze[current_position] = 2
        valid_moves = []

        if current_position[0] + 1 < N:
            valid_moves.append((current_position[0] + 1, current_position[1]))
        if current_position[1] + 1 < M:
            valid_moves.append((current_position[0], current_position[1] + 1))

        next_position = random.choice(valid_moves)
        current_position = next_position

    maze[current_position] = 2
    return maze

#function to add obstacles in specified coordinate
def add_obstacles(maze, min_obstacles, N, M):
    obstacles_added = 0

    while obstacles_added < min_obstacles:
        row = random.randint(0, N - 1)
        col = random.randint(0, M - 1)

        if (row, col) not in maze or maze[(row, col)] == 0:
            maze[(row, col)] = 1
            obstacles_added += 1

#function to set obstacles in specified coordinate
def set_obstacle(maze, N, M):
    try:
        print("Enter the coordinates to set an obstacle (i, j): ")
        row, col = map(int, input().split(","))

        if row == 1 and col == 1:
            print("Obstacle cannot be placed on the path.")
        elif row < 0 or row >= N or col < 0 or col >= M:
            raise KeyError
        elif maze[(row, col)] == 2:
            print("Obstacle cannot be placed on the path.")
        elif maze[(row, col)] == 1:
            print("Obstacle already exists at this location.")
        else:
            maze[(row, col)] = 1
            print(f"Obstacle placed at ({row}, {col})")

    except ValueError:
        print("ValueError in set_obstacle function. Need to be coordinates.")
    except KeyError:
        print("KeyError in set_obstacle function. 'Invalid coordinates, Please input coordinates within the range.'")

#function to remove obstacles in specified coordinate
def remove_obstacle(maze, N, M):
    try:
        print("Enter the coordinate to remove an obstacle (i,j): ")
        row, col = map(int, input().split(","))

        if row < 0 or row >= N or col < 0 or col >= M:
            raise KeyError

        if maze[(row, col)] == 2:
            print("Obstacle does not exist on the path.")
        elif maze[(row, col)] == 0:
            print("Obstacle does not exist at this location.")
        else:
            maze[(row, col)] = 0
            print(f"Obstacle removed at ({row}, {col})")

    except ValueError:
        print("ValueError in remove_obstacle function. Need to be coordinates.")
    except KeyError:
        print("KeyError in remove_obstacle function. 'Invalid coordinates, Please input coordinates within the range.'")

#print the maze
def print_maze(maze, N, M):
    for row in range(N):
        for col in range(M):
            if (row, col) not in maze:
                print("   ", end="")
            elif maze[(row, col)] == 0:
                print("   ", end="")
            elif maze[(row, col)] == 1:
                print(" X ", end="")
            elif maze[(row, col)] == 2:
                print(" O ", end="")
        print()

#main function of the code
def main():
    try:
        filename = input("Enter file name:")
        with open(filename, "r") as file:
            dimensions = file.readline().split()
            N = int(dimensions[0])
            M = int(dimensions[1])

        maze = generate_path(N, M)

        while True:
            min_obstacles = int(input("Enter the minimum number of obstacles to be added (0-56): "))
            if min_obstacles < 0 or min_obstacles > 56:
                print("ValueError occurred in main function. Invalid number of obstacles.")
            else:
                break


        add_obstacles(maze, min_obstacles, N, M)

        while True:
            print("\nOptions:")
            print("1. Set obstacle")
            print("2. Remove obstacle")
            print("3. Print maze")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                set_obstacle(maze, N, M)
            elif choice == '2':
                remove_obstacle(maze, N, M)
            elif choice == '3':
                print("\nGenerated maze map:")
                print_maze(maze, N, M)
            elif choice == '4':
                break
            else:
                print("Invalid option. Please choose a valid option.")

    except IOError:
        print("IOError occurred in main function. File not found. Please enter a valid file name")
    except ValueError:
        print("Error: Invalid maze dimensions in the file.")
    except NameError:
        print("Error: Invalid file name.")


main()
def main():
    try:
        filename = input("Enter file name:")
        with open(filename, "r") as file:
            dimensions = file.readline().split()
            N = int(dimensions[0])
            M = int(dimensions[1])

        maze = generate_path(N, M)

        while True:
            min_obstacles = int(input("Enter the minimum number of obstacles to be added (0-56): "))
            if min_obstacles < 0 or min_obstacles > 56:
                print("ValueError occurred in main function. Invalid number of obstacles.")
            else:
                break


        add_obstacles(maze, min_obstacles, N, M)

        while True:
            print("\nOptions:")
            print("1. Set obstacle")
            print("2. Remove obstacle")
            print("3. Print maze")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                set_obstacle(maze, N, M)
            elif choice == '2':
                remove_obstacle(maze, N, M)
            elif choice == '3':
                print("\nGenerated maze map:")
                print_maze(maze, N, M)
            elif choice == '4':
                break
            else:
                print("Invalid option. Please choose a valid option.")

    except IOError:
        print("IOError occurred in main function. File not found please enter a valid file name")
    except ValueError:
        print("Error: Invalid maze dimensions in the file.")
    except NameError:
        print("Error: Invalid file name.")


main()