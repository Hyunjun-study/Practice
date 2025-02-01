def solution(arr):
    answer = [[]]
    if len(arr) > len(arr[0]):
        for i in range(len(arr) - len(arr[0])):
            for j in range(len(arr)):
                arr[j].append(0)
    elif len(arr) < len(arr[0]):
        for i in range(len(arr[0])-len(arr)):
            arr.extend([[0]*len(arr[0])])
    else:
        return arr
    return arr
