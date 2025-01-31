def solution(arr):
    ans = []
    i = 0
    while i<len(arr):
        if ans != [] and ans[-1] == arr[i]:
            ans.pop()
            i += 1
        elif ans != [] and ans[-1] != arr[i]:
            ans.append(arr[i])
            i+=1
        else:
            ans.append(arr[i])
            i+=1
        
    if ans == [] :
        ans.append(-1)
    
    return ans
