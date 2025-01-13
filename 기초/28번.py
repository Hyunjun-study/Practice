def solution(my_string, queries):
    answer = ''
    count = 0
    
    for c in queries:
        str_list = list(my_string)
        
        if c[0] == 0:
            str_list[c[0]:c[1]+1] = my_string[c[1]::-1]
        else:
            str_list[c[0]:c[1]+1] = my_string[c[1]:c[0]-1:-1]
        my_string = ''.join(str_list)
    
    return my_string

# 문자열 역 출력은 step에 -1, 그리고 start,end 위치 바꿔야됨. [end,start,-1]
