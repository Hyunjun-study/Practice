def solution(n):
    arr = [n]
    i = 0
    while arr[i] != 1:
        if not arr[i]%2:
            arr.append(arr[i]/2)
            i+=1
        else:
            arr.append(3*arr[i]+1)
            i+=1
    return arr
