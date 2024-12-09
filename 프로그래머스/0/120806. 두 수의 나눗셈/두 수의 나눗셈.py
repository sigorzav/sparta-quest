def solution(num1, num2):
    answer = 0
    
    if all((0 <= i <= 100) for i in [num1, num2]):
        answer = (int)((num1 / num2) * 1000)
    
    return answer