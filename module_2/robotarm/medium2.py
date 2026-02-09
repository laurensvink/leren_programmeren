from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[2],0)

# your code starts here:
x = 0
while x < 5:
    i = 0

    while i < 6:
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        i += 1
    x += 1

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

