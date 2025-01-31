def solution(arr, k):
    a = list(dict.fromkeys(arr))  
    if len(a) >= k:
        return a[:k]  
    else:
        a.extend([-1] * (k - len(a)))  
        return a

