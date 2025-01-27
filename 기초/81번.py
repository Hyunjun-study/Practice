def solution(num_str):
    answer = 0
    mylist = list(num_str)
    for i in mylist:
        answer+=int(i)
    return answer
