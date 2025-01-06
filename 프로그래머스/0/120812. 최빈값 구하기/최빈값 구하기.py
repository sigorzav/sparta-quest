from collections import Counter

def solution(array):
    # 각 숫자의 빈도 계산
    counter = Counter(array)
    
    # 가장 높은 빈도 값
    max_count = max(counter.values())
    
    # 빈도가 가장 높은 숫자들 찾기
    modes = [key for key, count in counter.items() if count == max_count]
    
    # 최빈값이 여러 개인 경우 -1 반환
    return modes[0] if len(modes) == 1 else -1