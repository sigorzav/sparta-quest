def solution(n):
    answer = [v for v in range(1, n + 1) if v % 2 != 0]
    return answer