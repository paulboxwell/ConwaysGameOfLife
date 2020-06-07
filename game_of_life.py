import random
import shutil
#Get Terminal size
size_str = shutil.get_terminal_size((80, 20))

GridSize_H = size_str[1] -2
GridSize_W = int(size_str[0]/2)-1

class Square:
  def __init__(self, a):
    self.alive = a
    self.count = 0

grid = []
#Initialise Grid with random state
for i in range(0,GridSize_H):
    row = []
    for i in range(0,GridSize_W):
        row.append(Square(random.randint(0, 1)))
    grid.append(row)

while(True):

    #Count
    for i in range(1,GridSize_H-1):
        for j in range(1,GridSize_W-1):
            grid[i][j].count = -grid[i][j].alive
            for x in range(-1,2):
                for y in range(-1,2):
                    grid[i][j].count += grid[i+x][j+y].alive

    #Update Status
    for i in range(1,GridSize_H-1):
        for j in range(1,GridSize_W-1):
            if grid[i][j].alive:
                #Rules for if alive
                if grid[i][j].count < 2:
                    grid[i][j].alive = False
                if grid[i][j].count > 3:
                    grid[i][j].alive = False
            else:
                #Rules for the dead
                if grid[i][j].count == 3:
                    grid[i][j].alive = True

    #Print Grid
    out_str = ""
    for row in grid:
        for sqr in row:
            if sqr.alive:
                out_str += "██"
            else:
                out_str += "  "
        out_str += "\n"

    print(out_str)
    #if input("enter to continue") != "":
    #    break


