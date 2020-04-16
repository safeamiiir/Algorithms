number = input()
right = [int(tower) for tower in input().split()]
blocks = 0
while( len(right) > 0 ):
    left = []
    blocks += 1
    minimum = right.index(min(right))
    for itemIndex in range(minimum + 1):
        left.append(right.pop(0)) # We initialized left and right arrays
    while(len(right) > 0 and max(left) > min(right) ):
        minimum = right.index(min(right))
        for index in range(minimum + 1):
            left.append(right.pop(0))             
print(blocks)