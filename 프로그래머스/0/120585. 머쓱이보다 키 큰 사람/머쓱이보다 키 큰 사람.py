def solution(array, height):
    answer = 0
    
    if 1 <= len(array) <= 100 and 1 <= height <= 200:
        array.sort()

        for i in array:
            if 1 <= i <= 200 and height < i:
                answer += 1
                
    return answer