def solution(num1, num2):
    answer = 0
    
    if all((0 <= i <= 10000) for i in [num1, num2]):
        answer = 1 if num1 == num2 else -1
        
    return answer