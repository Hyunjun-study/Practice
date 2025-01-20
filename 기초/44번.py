def solution(intStrs, k, s, l):
    answer = []
    a=""
    for c in intStrs:
        for i in range(s,s+l):
            a += c[i]
        if int(a)>k:answer.append(int(a))
        a=""
    return answer
