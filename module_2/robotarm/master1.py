from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from master import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[1],0)

# your code starts here:
# Determine the majority color from the first three stacks
robotArm.moveRight()  # start at position 0
robotArm.grab()
color0 = robotArm.scan()
robotArm.drop()

robotArm.moveRight()
robotArm.grab()
color1 = robotArm.scan()
robotArm.drop()

if color0 == color1:
    common_color = color0
else:
    robotArm.moveRight()
    robotArm.grab()
    color2 = robotArm.scan()
    robotArm.drop()
    if color2 == color0:
        common_color = color0
    else:
        common_color = color1

# Search for the different color and grab it
for position in range(10):
    while robotArm.stackIndex() < position:
        robotArm.moveRight()
    while robotArm.stackIndex() > position:
        robotArm.moveLeft()

    robotArm.grab()
    current_color = robotArm.scan()
    if current_color != common_color:
        break
    robotArm.drop()

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

