n = int(input())
l = list(map(int, input().split()))
ans = 1
if n == 1:
    print(ans)
else:
    a = l[0]
    flag = True   # find next large element
    for i in range(1, n):
        if l[i] > a:
            a = l[i]
            ans += 1
            flag = False
            break
        if l[i] < a:
            a = l[i]
            flag = True
            if(ans > 1):
                ans += 1
            break
    for j in range(i, n):
        if flag == True:
            if l[j] > a:
                ans += 1
                flag = False
        else:
            if l[j] < a:
                ans += 1
                flag = True
        a = l[j]
    print(ans)