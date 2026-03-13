from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

# your code starts here:
RED_INDEX = 7
GREEN_INDEX = 8
BLUE_INDEX = 9

while True:
    movedSomething = False
    
    
    while robotArm.moveLeft():
        pass
    
    
    while True:
        
        if not robotArm.stackEmpty():
            
            robotArm.grab()
            color = robotArm.scan()
            
            if color == "red":
                target = RED_INDEX
            elif color == "green":
                target = GREEN_INDEX
            elif color == "blue":
                target = BLUE_INDEX
            
            
            while robotArm.stackIndex() < target:
                robotArm.moveRight()
            while robotArm.stackIndex() > target:
                robotArm.moveLeft()
            
            robotArm.drop()
            movedSomething = True
        
        if not robotArm.moveRight():
            break
    
    if not movedSomething:
        break


# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

