def solution(slice, n):
    answer = 0
    
    for i in range(1, n*10, 1):
        pizza = (i*slice)
        if pizza >= n and pizza % n >= 0:
            answer = i
            break
    
    return answer

# 다른 사람의 풀이 [해석]
# (n//slice)일 경우 n=slice 일 때 결과값이 기댓값보다 무조건 1 높게 나오기 때문에 -1. 
# 그리고 뒤에 +1을 해주는 이유는 n-1//slice<1일 때 결과값이 0이 되는걸 방지하기 위함
def solution(slice, n):
    return ((n - 1) // slice) + 1
