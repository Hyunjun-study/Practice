def solution(myString):
    answer = ''
    my_list = list(myString)
    for i in range(len(my_list)):
        if my_list[i] == "a" or my_list[i] == "A":
            my_list[i] = my_list[i].upper()
        else:
            my_list[i] = my_list[i].lower()
    return ''.join(my_list)
