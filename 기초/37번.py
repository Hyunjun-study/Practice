def solution(arr, queries):
    ans1 = []
    ans2 = []
    for c in queries:
        for i in range(c[0],c[1]+1):
            ans1.append(arr[i])
        ans1.sort()
        for f in ans1:
            if f > c[2]:
                ans2.append(f)
                break
        if max(ans1) <=c[2]:
            ans2.append(-1)
        ans1.clear()
    return ans2
        
    
