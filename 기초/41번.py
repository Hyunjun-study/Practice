def solution(my_string, s, e):
    answer = ''
    answer = my_string[:s]+my_string[e:s-1:-1]+my_string[e+1:]
    return answer
    
    
