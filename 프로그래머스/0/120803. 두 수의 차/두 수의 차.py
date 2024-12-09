def solution(num1, num2):
    answer = 0
    
    if all((-50000 <= i and i <= 50000) for i in [num1, num2]):
        answer = num1 - num2
        
    return answer