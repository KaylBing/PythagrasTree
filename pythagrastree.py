from turtle import goto, pu, pd, screensize, speed, done
from turtle import color as colour
speed(speed=0)  # Fastest speed setting #
screensize(800, 800)

def branch(start_x, start_y, end_x, end_y, depth=0):  # Original coordinates and depth #
    if depth != 0:
        difference_x, difference_y = end_x - start_x, start_y - end_y  # Difference between x and y #
        x3, y3 = end_x - difference_y, end_y - difference_x
        x4, y4 = start_x - difference_y, start_y - difference_x
        x5, y5 = x4 + (difference_x - difference_y) / 2, y4 - (difference_x + difference_y) / 2  # Fifth point calculation #
        goto(start_x, start_y), pd()  # Moves turtle to the given point, then puts the "pen" down #
        for x, y in ((end_x, end_y), (x3, y3), (x4, y4), (start_x, start_y)): # Iterates through points in branch #
            goto(x, y)
        pu()  # "Pen" up #
        branch(x4, y4, x5, y5, depth - 1)  # recursive calls between points 4 and 5 #
        branch(x5, y5, x3, y3, depth - 1)  # recursive calls between points 3 and 5 #

if __name__ == '__main__':
    colour('red', 'yellow')
    pu()  # Checks that the pen is up when the program starts #
    branch(-100, 500, 100, 500, depth=6) # Starting points and number of branches #
    done()  # Keeps the window open after drawing completion #
