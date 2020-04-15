number = input("Please enter number of towers: ")
right = [int(tower) for tower in input("Please enter height of towers: ").split()]
blocks = 0
print(right)
while( len(right) > 0 ):
    print('right: ', right)
    left = []
    blocks += 1
    left.append(right.pop(0))
    if(max(left) > min(right) ):
        for index in range(right.index(min(right))+1):
            left.append(right.pop(index))
print('blocks: ', blocks)