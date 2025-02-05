def solution(rank, attendance):
    answer = 0
    idx = 0
    ml = []
    for i in range(1,len(rank)+1):
        idx = rank.index(i)
        if attendance[idx] == True:
            ml.append(idx)
    return 10000*ml[0] + 100*ml[1] + ml[2]
