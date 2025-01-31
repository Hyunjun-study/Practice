def solution(myString):
    answer = ''
    ml = list(myString)
    for i in range(len(myString)):
        if ml[i] < "l":
            ml[i] = "l"
    return ''.join(ml)
