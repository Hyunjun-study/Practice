def solution(str_list):
    answer = []
    if "l" not in str_list or "r" not in str_list:
        return []
    elif str_list.index("l") < str_list.index("r"):
        for i in range(str_list.index("l")):
            answer.append(str_list[i])
    elif str_list.index("l") > str_list.index("r"):
        for i in range(str_list.index("r")+1,len(str_list)):
            answer.append(str_list[i])
    return answer
