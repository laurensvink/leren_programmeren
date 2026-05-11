from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from master import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)

# your code starts here:
# Scan all 10 stacks, find the duplicated color, then stack the two duplicate boxes together.

duplicate_positions = {}
for i in range(10):
    while robotArm.stackIndex() < i:
        robotArm.moveRight()
    while robotArm.stackIndex() > i:
        robotArm.moveLeft()

    robotArm.grab()
    color = robotArm.scan()
    robotArm.drop()

    if color not in duplicate_positions:
        duplicate_positions[color] = [i]
    else:
        duplicate_positions[color].append(i)

# find the color with exactly two occurrences
target_color = None
for color, positions in duplicate_positions.items():
    if len(positions) == 2:
        target_color = color
        source_pos, dest_pos = positions
        break

# move the second occurrence onto the first occurrence
while robotArm.stackIndex() < source_pos:
    robotArm.moveRight()
while robotArm.stackIndex() > source_pos:
    robotArm.moveLeft()
robotArm.grab()
while robotArm.stackIndex() < dest_pos:
    robotArm.moveRight()
while robotArm.stackIndex() > dest_pos:
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