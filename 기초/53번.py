def solution(my_string, indices):
    answer = ''
    answer = ''.join([char for i, char in enumerate(my_string) if i not in indices])
    return answer

