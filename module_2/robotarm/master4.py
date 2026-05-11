from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from master import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

# your code starts here:
# Save the order of the 4-box stack at position 0, then rebuild a duplicate stack from positions 6-9.

x_colors = []
for dest in [1, 2, 3, 4]:
    # grab the top box from stack 0
    while robotArm.stackIndex() > 0:
        robotArm.moveLeft()
    while robotArm.stackIndex() < 0:
        robotArm.moveRight()
    robotArm.grab()
    color = robotArm.scan()
    x_colors.append(color)

    # move that box to a temporary stack
    while robotArm.stackIndex() < dest:
        robotArm.moveRight()
    while robotArm.stackIndex() > dest:
        robotArm.moveLeft()
    robotArm.drop()

# Build a duplicate stack in position 5 using the scanned order from bottom to top
for color in reversed(x_colors):
    for y_pos in [6, 7, 8, 9]:
        while robotArm.stackIndex() < y_pos:
            robotArm.moveRight()
        while robotArm.stackIndex() > y_pos:
            robotArm.moveLeft()

        if robotArm.stackEmpty():
            continue

        robotArm.grab()
        current_color = robotArm.scan()
        if current_color == color:
            while robotArm.stackIndex() < 5:
                robotArm.moveRight()
            while robotArm.stackIndex() > 5:
                robotArm.moveLeft()
            robotArm.drop()
            break
        else:
            robotArm.drop()

# Reconstruct the original stack 0 from the temporary stacks
for src in [4, 3, 2, 1]:
    while robotArm.stackIndex() < src:
        robotArm.moveRight()
    while robotArm.stackIndex() > src:
        robotArm.moveLeft()
    robotArm.grab()
    while robotArm.stackIndex() < 0:
        robotArm.moveRight()
    while robotArm.stackIndex() > 0:
        robotArm.moveLeft()
    robotArm.drop()

robotArm.showSolution()
# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

