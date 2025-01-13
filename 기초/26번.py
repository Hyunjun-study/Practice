def solution(n, control):
    answer = n
    for i in range(len(control)):
        if control[i] == "w":
            answer += 1
        elif control[i] == "s":
            answer -= 1
        elif control[i] == "d":
            answer += 10
        else:
            answer -= 10
    return answer

#배울 점 있는 코드들

def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])   #딕셔너리를 사용할 생각도 많이 해보기

def solution(n, control):
    answer = n
    c = { 'w':1, 's':-1, 'd':10, 'a':-10}
    for i in control:
        answer += c[i]
    return answer

def solution(n, control):
    return n + 10*(control.count('d')-control.count('a')) + (control.count('w')-control.count('s'))  # 문장에서 반복되는 것을 count로 세서 계산을 효율적으로 함

def solution(n, control):
    for c in control:
        if c=='w':n+=1
        elif c=='s':n-=1
        elif c=='d':n+=10
        else:n-=10
    return n    # 반복문에서 범위를 리스트의 길이로 하는 게 아니라 그냥 문자열 자체로 하는 것 기억하기
