def solution(myString):
    answer = []
    leng = []
    answer = myString.split("x")
    for i in answer:
        leng.append(len(i))
    return leng
