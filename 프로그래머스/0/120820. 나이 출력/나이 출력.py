def solution(age):
    answer = 2023
    
    if 0 <= age <= 120:
        answer -= age
    
    return answer