from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from master import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[3],0)

# your code starts here:
# Move the box stacks from positions 3-6 using scan and ordered targets.
# First seen color -> position 0.
# Second distinct color -> position 1.
# Third distinct color -> position 9.
# Fourth distinct color -> position 8.

source_positions = [3, 4, 5, 6]
color_to_target = {}
assigned_targets = [0, 1, 9, 8]

for src in source_positions:
    # move to the source stack
    while robotArm.stackIndex() < src:
        robotArm.moveRight()
    while robotArm.stackIndex() > src:
        robotArm.moveLeft()

    while not robotArm.stackEmpty():
        robotArm.grab()
        color = robotArm.scan()

        if color in color_to_target:
            target = color_to_target[color]
        else:
            target = assigned_targets[len(color_to_target)]
            color_to_target[color] = target

        # move to target and drop
        while robotArm.stackIndex() < target:
            robotArm.moveRight()
        while robotArm.stackIndex() > target:
            robotArm.moveLeft()
        robotArm.drop()

        # return to source stack
        while robotArm.stackIndex() < src:
            robotArm.moveRight()
        while robotArm.stackIndex() > src:
            robotArm.moveLeft()

robotArm.showSolution()
# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

