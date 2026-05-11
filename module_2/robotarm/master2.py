from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from master import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[2],0)

# your code starts here:
for i in range(4):
    robotArm.moveRight()

# Scan all boxes to find the 3 colors
colors = []
for pos in range(6):
    robotArm.grab()
    current_color = robotArm.scan()
    if current_color not in colors:
        colors.append(current_color)
    robotArm.drop()
    if pos < 5:
        robotArm.moveRight()

# Now we have all 3 colors in the colors list
color1 = colors[0]
color2 = colors[1]
color3 = colors[2]

# Count each color to find which has 3 boxes
count1 = 0
count2 = 0
count3 = 0

# Move back to position 4
while robotArm.stackIndex() > 4:
    robotArm.moveLeft()

# Count the colors
for pos in range(6):
    robotArm.grab()
    current_color = robotArm.scan()
    if current_color == color1:
        count1 += 1
    elif current_color == color2:
        count2 += 1
    else:
        count3 += 1
    robotArm.drop()
    if pos < 5:
        robotArm.moveRight()

# Determine which color has which count
if count1 == 3:
    most_frequent = color1
    if count2 == 2:
        second_frequent = color2
        least_frequent = color3
    else:
        second_frequent = color3
        least_frequent = color2
elif count2 == 3:
    most_frequent = color2
    if count1 == 2:
        second_frequent = color1
        least_frequent = color3
    else:
        second_frequent = color3
        least_frequent = color1
else:
    most_frequent = color3
    if count1 == 2:
        second_frequent = color1
        least_frequent = color2
    else:
        second_frequent = color2
        least_frequent = color1

# Move back to position 4
while robotArm.stackIndex() > 4:
    robotArm.moveLeft()

# Collect all boxes to position 0, then distribute by color
for pos in range(6):
    while not robotArm.stackEmpty():
        robotArm.grab()
        current_color = robotArm.scan()
        current_pos = robotArm.stackIndex()
        
        # Determine target position based on color
        if current_color == most_frequent:
            target_pos = 0
        elif current_color == second_frequent:
            target_pos = 1
        else:
            target_pos = 2
        
        # Move to target position
        while robotArm.stackIndex() > target_pos:
            robotArm.moveLeft()
        while robotArm.stackIndex() < target_pos:
            robotArm.moveRight()
        robotArm.drop()
        
        # Return to current position
        while robotArm.stackIndex() < current_pos:
            robotArm.moveRight()
    if pos < 5:
        robotArm.moveRight()

# Move back to position 0
while robotArm.stackIndex() > 0:
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

