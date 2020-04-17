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

for index in range(numOfCases):
    if( len(ballsPosition) and len(keysPosition) and index == ballsPosition[0] and index == keysPosition[0]):
        print('index ', index, ' in if')
        ballsPosition.pop(0)
        keysPosition.pop(0)
        pointedArr.append(0)
    elif( len(ballsPosition) and index == ballsPosition[0] - 1):
        print('index ', index, ' in elif')
        ballsPosition.pop(0)
        pointedArr.append(0)
    elif(len(keysPosition) and index == keysPosition[0] - 1):
        print('index ', index, ' in elif')
        keysPosition.pop(0)
        pointedArr.append(0)
    else:
        print('index ', index, ' in else')
        pointedArr.append(-1)
print('-_-_-_-_-_-_-_-_-_-_-')
print('pointedArr:', pointedArr)
        
tempIndex = 0        
for index in range(1, numOfCases):
    newDistance = index - tempIndex
    if(pointedArr[index] == 0):
        if(newDistance > maxDistance):
            maxDistance = newDistance    
        tempIndex = index
        
print('-_-_-_-_-_-_-_-_-_-_-')
print('maxDistance: ', maxDistance)
print('answer: ',  numOfCases- maxDistance)