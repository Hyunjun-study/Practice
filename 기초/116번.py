def solution(arr):
    answer = 0
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == arr[j][i]:
                answer += 1
            count += 1
    if answer == count:
        return 1
    return 0
