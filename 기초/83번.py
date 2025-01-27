def solution(n_str):
    answer = ''
    a = list(n_str)
    for i in range(len(a)):
        if a[i] != '0':
            a = a[i:]
            break
        
    return ''.join(a)
