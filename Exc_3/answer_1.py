number = input("Please enter number of towers: ")
right = [int(tower) for tower in input("Please enter height of towers: ").split()]
blocks = 0
while( True ):
    left = []
    blocks += 1
    for index in range(right.index(min(right))+1):
        left.append(right.pop(0)) # We initialized left and right arrays
    if( len(right) > 0 ):
        if(max(left) > min(right) ):
            for index in range(right.index(min(right))+1):
                left.append(right.pop(index))
    else:
        break
print(blocks)