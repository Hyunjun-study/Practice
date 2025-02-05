def solution(myStr):
    answer = []
    word = ""
    ml = list(myStr)
    for i in range(len(myStr)):
        if ml[i] == "a":
            ml[i] =""
        elif ml[i] == "b":
            ml[i] =""
        elif ml[i] == "c":
            ml[i] =""
    for c in ml:
        if c:
            word += c
        else:
            if word:
                answer.append(word)
                word = ""
    if word:
        answer.append(word)
    
    if answer:
        return answer
    else:
        return ["EMPTY"]
    
    
    
