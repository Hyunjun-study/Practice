def solution(strArr):
    answer = 0
    leng = max([len(i) for i in strArr])
    
    ml = []
    for k in range(leng):
        ml.append(0)
        
    for j in strArr:
        ml[len(j)-1] += 1
    
    return max(ml)
