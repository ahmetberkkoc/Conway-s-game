import random, time, os, imageio
import pyscreenshot as ImageGrab

grid = {}
counter2 = 1
for x in range(50):
    grid[x] = {}
    for y in range(50):
        a = round(random.random())
        if a == 1:
            grid[x][y] = "▉"
        else:
            grid[x][y] = " "

def my_neighbours(pos):
    list1 = []
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            if x == 0 and y == 0:
                continue
            elif x == -1 and pos[0] == 0:
                continue
            elif x == 1 and pos[0] == 49:
                continue
            elif y == -1 and pos[1] == 0:
                continue
            elif y == 1 and pos[1] == 49:
                continue
            
            else:
                list1.append([pos[0] + x, pos[1] + y])
    
    return list1

def my_neighbours_simple(pos, grid):
    pos_list = my_neighbours(pos)
    list1 = []
    for x in pos_list:
        list1.append(grid[x[0]][x[1]])
    return list1

def what_to_do(value, pos, grid):
    list1 = my_neighbours_simple(pos, grid)
    counter = 0
    for x in list1:
        if x == "▉":
            counter += 1

    if value == "▉":
        if 1 < counter < 4:
            return "▉"
        else:
            return " "
    else:
        if counter == 3:
            return "▉"
        else:
            return " "

def main(grid):
    global counter2

    grid1 = {}

    for x in range(50):
        grid1[x] = {}
        for y in range(50):
            grid1[x][y] = 0

    for x in range(50):
        for y in range(50):
            pos = [x, y]
            value = grid[x].get(y)
            grid1[x][y] = what_to_do(value, pos, grid)
    
    for x in range(50):
        for y in range(50):
            print(grid1[x][y], end=" ")
        print()

    im = ImageGrab.grab(bbox=(1182, 80, 1884, 929))
    im.save("box"+str(counter2)+".png")
    os.system('cls' if os.name == 'nt' else 'clear')
    counter2 += 1

    return main(grid1)

main(grid)