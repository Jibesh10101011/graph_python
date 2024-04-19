import sys


class Maze():
    def __init__(self, filename):

            # Read file and set height and width of maze
            with open(filename) as f:
                contents = f.read()

            # Validate start and goal
            if contents.count("A") != 1:
                raise Exception("maze must have exactly one start point")
            if contents.count("B") != 1:
                raise Exception("maze must have exactly one goal")

            # Determine height and width of maze
            contents = contents.splitlines()
            self.height = len(contents)
            self.width = max(len(line) for line in contents)

            print("Height : ",self.height)
            print("Width : ",self.width)

            # Keep track of walls
            self.walls = []
            for i in range(self.height):
                row = []
                for j in range(self.width):
                    try:
                        if contents[i][j] == "A":
                            self.start = (i, j)
                            row.append(False)
                        elif contents[i][j] == "B":
                            self.goal = (i, j)
                            row.append(False)
                        elif contents[i][j] == " ":
                            row.append(False)
                        else:
                            row.append(True)
                    except IndexError:
                        row.append(False)
                self.walls.append(row)

            self.solution = None
            print(self.walls)
    

    
m=Maze("maze1.txt")
print()
