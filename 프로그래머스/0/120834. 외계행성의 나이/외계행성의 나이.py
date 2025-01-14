def solution(age):
    answer = ''
    for n in str(age):
        answer += chr(int(n) + ord('a'))
    return answer