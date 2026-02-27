from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

# your code starts here:
for i in range(2, 6):
    robotArm.grab()
    for _ in range(i):
        robotArm.moveRight()
    robotArm.drop()
    for _ in range(i):
        robotArm.moveLeft()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()

for d in range(4, 0, -1):
    for _ in range(d):
        robotArm.moveRight()
    robotArm.grab()
    for _ in range(d):
        robotArm.moveLeft()
    robotArm.drop()
# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

