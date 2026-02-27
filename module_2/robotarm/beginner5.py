from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from beginner import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)

# your code starts here:
def move_block(steps):
    robotArm.grab()
    for _ in range(steps):
        robotArm.moveRight()
    robotArm.drop()
    for _ in range(steps):
        robotArm.moveLeft()
robotArm.moveRight()  # initial starting move

# Repeat for 8 blocks
for _ in range(8):
    move_block(8)




# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

