numOfCases, numOfKeys, numOfBalls = [int(tower) for tower in input().split()]
keysPosition = [int(tower) for tower in input().split()]
ballsPosition = [int(tower) for tower in input().split()]
print('numOfCases: ', numOfCases)
print('numOfKeys: ', numOfKeys)
print('numOfBalls: ', numOfBalls)
print('keysPosition: ', keysPosition)
print('ballsPosition: ', ballsPosition)
print('-_-_-_-_-_-_-_-_-_-_-')
pointedArr = []
maxDistance = 0

# Initialize pointedArr with -1
for index in range(numOfCases):
    pointedArr.append(-1)

'''
-1 =>  Empty
 0 =>  Ball
 1 =>  Key
 2 =>  Ball and Key
'''
bothFlag = '_'
for index in range(numOfCases): # Change pointedArr which should be 0
    if(len(ballsPosition) and index == ballsPosition[0] - 1):
        print('index ', index, ' in elif ballsPosition')
        bothFlag = index
        ballsPosition.pop(0) # Pop element
        pointedArr[index] = 0
    if(len(keysPosition) and index == keysPosition[0] - 1):
        print('index ', index, ' in elif keysPosition')
        if(bothFlag == index):
            print('Both ', bothFlag + 1)
            bothFlag = '_'
            pointedArr[index] = 2
        else:   
            pointedArr[index] = 1
        keysPosition.pop(0) # Pop element
print('-_-_-_-_-_-_-_-_-_-_-')
print('pointedArr:', pointedArr)

# Find range of keys    
# if start == end  ==> it has only one key!
startOfKeys = -1
endOfKeys = -1
endFlag = False
for index in range(numOfCases):
    #set index of start of the key
    if( (pointedArr[index] == 1 or pointedArr[index] == 2) and not endFlag):
        startOfKeys = index
        endFlag = True
    #set index of end of the key
    if( (pointedArr[index] == 1 or pointedArr[index] == 2) and endFlag):
        endOfKeys = index


tempIndex = 0
for index in range(1, numOfCases):
    newDistance = index - tempIndex - 1
    if(pointedArr[index] == 0 or pointedArr[index] == 1 or pointedArr[index] == 2):
        if(newDistance > maxDistance):
            maxDistance = newDistance    
        tempIndex = index

        
print('-_-_-_-_-_-_-_-_-_-_-')
print('startOfKeys: ', startOfKeys)
print('endOfKeys: ', endOfKeys)
print('maxDistance: ', maxDistance)
#handle if we only have one key or not!
if (startOfKeys == endOfKeys):
    print('answer: ',  numOfCases - maxDistance)
else:    
    print('answer: ',  (endOfKeys - startOfKeys + 1) - maxDistance)