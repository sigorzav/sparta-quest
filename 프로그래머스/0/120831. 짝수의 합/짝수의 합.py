def solution(n):
    answer = 0
    
    if 0 < n <= 1000:
        for i in range(1, n + 1):
            answer += i if i % 2 == 0 else 0
        
    return answer