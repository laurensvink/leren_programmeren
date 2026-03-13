from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)

# your code starts here:
colorCount = {}
while robotArm.moveLeft(): pass 

while True:
    if not robotArm.stackEmpty():
        robotArm.grab()
        c = robotArm.scan()
        robotArm.drop()
        colorCount[c] = colorCount.get(c, 0) + 1
    if not robotArm.moveRight():
        break

mostCommon = None
maxCount = -1
for color, count in colorCount.items():
    if count > maxCount:
        mostCommon = color
        maxCount = count


while True:
    moved = False
    
    while robotArm.moveLeft(): pass  # helemaal links
    
    while True:
        if not robotArm.stackEmpty():
            robotArm.grab()
            if robotArm.scan() == mostCommon:
                while robotArm.stackIndex() > 0:
                    robotArm.moveLeft()
                robotArm.drop()
                moved = True
            else:
                robotArm.drop()
        if not robotArm.moveRight():
            break
    
    if not moved:
        break


# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

