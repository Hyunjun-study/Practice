def solution(str_list):
    if "l" not in str_list and "r" not in str_list:
        return []
    
    if "l" in str_list and "r" in str_list:
        if str_list.index("l") < str_list.index("r"):
            return str_list[:str_list.index("l")]
        else:
            return str_list[str_list.index("r") + 1:]
    
    if "l" in str_list:
        return str_list[:str_list.index("l")]
    
    if "r" in str_list:
        return str_list[str_list.index("r") + 1:]
