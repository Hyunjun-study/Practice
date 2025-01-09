def solution(a, b):
    answer = 0
    first = str(a)+str(b)
    sec = str(b)+str(a)
    if int(first)>=int(sec):
        answer = int(first)
    else:
        answer = int(sec)
    return answer
 #더 좋은 답변 -> max 함수와 format 사용
def solution(a, b):
  return int(max(f"{a}{b}", f"{b}{a}"))
