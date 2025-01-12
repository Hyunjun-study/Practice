import math
def solution(num_list):
    answer = 0
    if sum(num_list)**2 > math.prod(num_list):
        answer = 1
    else:
        answer = 0
    return answer

# sum 메서드와 math.prod 메서드 잘 기억해두기
