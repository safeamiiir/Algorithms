number = input("Please enter number of towers: ")
right = [int(tower) for tower in input("Please enter height of towers: ").split()]
blocks = 0
while( len(right) > 0 ):
    left = []
    blocks += 1
    minimum = [index for index, value in enumerate(right) if value == min(right)][0]
    for itemIndex in range(minimum+1):
        left.append(right.pop(0)) # We initialized left and right arrays
    if( len(right) > 0 ):  
        while(max(left) > min(right) ):
            minimum = [index for index, value in enumerate(right) if value == min(right)][0]
            for index in range(minimum+1):
                left.append(right.pop(0))             
    else:
        break
print(blocks)