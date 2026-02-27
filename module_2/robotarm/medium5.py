from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)

# your code starts here:
for k in range(9, 0, -2):
    robotArm.grab()
    for _ in range(k):
        robotArm.moveRight()
    robotArm.drop()
    if k > 1:
        for _ in range(k - 1):
            robotArm.moveLeft()
# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()


