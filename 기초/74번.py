def solution(arr):
    answer = -1
    while True :
        arr1 = arr.copy()
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i]%2==0:
                arr[i] /=2
            elif arr[i] < 50 and arr[i]%2==1:
                arr[i] = arr[i]*2+1
        answer +=1
        count = 0
        for i in range(len(arr)):
            if arr[i] == arr1[i]:
                count+=1
        if count == len(arr):
            break
    
    return answer
