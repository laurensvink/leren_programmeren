from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from beginner import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[3],0)

# your code starts here:
for i in range(4):
    robotArm.grab()
    for j in range(4):
        robotArm.moveRight()
    robotArm.drop()
    for j in range(4):
        robotArm.moveLeft()
robotArm.grab()
for i in range(4):
    robotArm.moveRight()
robotArm.drop()




# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

