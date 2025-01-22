import string
def solution(my_string):
    answer = []
    for i in string.ascii_uppercase:
        answer.append(my_string.count(i))
                      
    for i in string.ascii_lowercase:
        answer.append(my_string.count(i))
    return answer

