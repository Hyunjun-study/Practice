def solution(arr, queries):
    answer = []
    for a,b in queries:
        for i in range(len(arr)):
            if a<=i<=b:
                arr[i]+=1
    return arr
