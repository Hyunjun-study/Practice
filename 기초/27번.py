def solution(numLog):
    answer = ''

    for i in range(1,len(numLog)):
        diff = numLog[i]-numLog[i-1]
        if diff == 1:
            answer += "w"
        elif  diff == -1:
            answer += "s"
        elif  diff == 10:
            answer += "d"
        else:
            answer += "a"
    return answer

# diff 처럼 반복되는 계산은 코드의 가독성을 위해서 선언해둔 뒤 변수명만 이용하기
