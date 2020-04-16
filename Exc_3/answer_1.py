number = input("Please enter number of towers: ")
right = [int(tower) for tower in input("Please enter height of towers: ").split()]
blocks = 0
while( len(right) > 0 ):
    print('blocks: ', blocks)
    left = []
    blocks += 1
    print('Right: ', right)
    print('minimum Right: ', min(right))
    print('minimum: ', [index for index, value in enumerate(right) if value == min(right)])
    minimum = [index for index, value in enumerate(right) if value == min(right)][0]
    for itemIndex in range(minimum+1):
        left.append(right.pop(0)) # We initialized left and right arrays
        print('Range: ', minimum+1)
        print('itemIndex: ', itemIndex)
        print('left: ', left)
        print('right: ', right)
    if( len(right) > 0 ):
        if(max(left) > min(right) ):
            for index in range([index for index, value in enumerate(right) if value == min(right)][0]+1):
                left.append(right.pop(0))
    else:
        break
print('Final blocks', blocks)