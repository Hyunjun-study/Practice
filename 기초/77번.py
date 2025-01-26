def solution(myString, pat):
    answer = 0
    if len(myString) < len(pat):
        return 0
    else:
        a = myString.lower()
        b = pat.lower()
    
    if b in a :
        return 1
    else:
        return 0
