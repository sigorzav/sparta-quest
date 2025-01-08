def solution(slice, n):
    answer = 0
    
    for i in range(1, n*10, 1):
        pizza = (i*slice)
        if pizza >= n and pizza % n >= 0:
            answer = i
            break
    
    return answer