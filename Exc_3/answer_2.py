number = input()
sequence = [int(tower) for tower in input().split()]
ans = []
while(len(sequence) > 0):
    minimum = min(sequence)
    ans.append(minimum)
    for i in range(sequence.index(minimum)+1):
        sequence.pop(0)        
    if(len(sequence) > 0):
        maximum = max(sequence)
        ans.append(maximum)
        for i in range(sequence.index(maximum)+1):
            sequence.pop(0)
print(len(ans))