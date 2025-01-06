def solution(array):
    array.sort()
    
    idx = len(array) // 2
    if len(array) % 2 == 0:
        idx += 1
    
    return array[idx]