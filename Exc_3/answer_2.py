_ = int(input())
sequence = list(map(int, input().split()))
size = len(sequence)
answer = 1
if size == 1:
    print(answer)
else:
    a = sequence[0]
    flag = True
    for i in range(1, size):
        if sequence[i] > a:
            a = sequence[i]
            answer += 1
            flag = False
            break
        if sequence[i] < a:
            a = sequence[i]
            flag = True
            break
    for j in range(i, size):
        if flag == True:
            if sequence[j] > a:
                answer += 1
                flag = False
        else:
            if sequence[j] < a:
                answer += 1
                flag = True
        a = sequence[j]
    print(answer)