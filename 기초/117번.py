def solution(n):
    answer = []
    for i in range(n):
        ml = []
        for j in range(n):
            if i == j:
                ml.append(1)
            else:
                ml.append(0)
        answer.append(ml)
    return answer
