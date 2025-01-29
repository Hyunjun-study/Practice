def solution(myString):
    answer = []
    answer = myString.split("x")
    answer.sort()
    answer = [i for i in answer if i != ""]
    return answer
