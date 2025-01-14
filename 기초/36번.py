def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        if all(digit in '05' for digit in str(i)):
            answer.append(i)
    if answer == []:
         answer.append(-1)
    
    return answer


# all -> 반복 가능한 객체의 모든 요소가 true 일 때만 true 반환 -> i가 0과 5로만 이루어져야만 true 반환.
# '05' 는 조건문에서는 0과 5을 따로 처리함.
