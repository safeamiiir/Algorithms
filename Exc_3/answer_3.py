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
-1 => Empty
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
        
# tempIndex = 0        
# for index in range(1, numOfCases):
#     newDistance = index - tempIndex
#     if(pointedArr[index] == 0 ):
#         if(newDistance > maxDistance and newDistance > 1):
#             maxDistance = newDistance    
#         tempIndex = index
        
# print('-_-_-_-_-_-_-_-_-_-_-')
# print('maxDistance: ', maxDistance)
# print('answer: ',  numOfCases- maxDistance)