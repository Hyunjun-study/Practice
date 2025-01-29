def solution(binomial):
    answer = 0
    ml = binomial.split(" ")
    if ml[1] == "+":
        return int(ml[0]) + int(ml[2])
    elif ml[1] == "-":
        return int(ml[0]) - int(ml[2])
    else:
        return int(ml[0]) * int(ml[2])
