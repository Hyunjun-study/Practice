def solution(picture, k):
    answer = []
    c=""
    for i in picture:
        for j in i:
            c+=j*k
        for n in range(k):
            answer.append(c)
        c=""    
    return answer
