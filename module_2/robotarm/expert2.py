from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[2],0)

# your code starts here
for i in range(9):
    stapel = robotArm.stackIndex()
    robotArm.grab()
    if robotArm.scan() == "red": 
        while robotArm.stackIndex()< 9:
            robotArm.moveRight()
        robotArm.drop() 
    else:
        robotArm.drop()
        robotArm.moveRight() 

    if robotArm.stackIndex() == 9:
        while robotArm.stackIndex() > stapel:
            robotArm.moveLeft()
    if robotArm.stackIndex() == stapel:
        robotArm.moveRight()


# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

