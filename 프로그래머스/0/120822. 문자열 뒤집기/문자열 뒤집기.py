def solution(my_string):
    answer = list(my_string)
    answer.reverse()
    return ''.join(answer)

# etc 1.
def solution(my_string):
    return my_string[::-1]

# etc 2.
def solution(my_string):
    answer = ''

    for i in range(len(my_string)-1, -1, -1) :
        answer += my_string[i]
    return answer

# etc 3.
def solution(my_string):
    answer = ''
    for c in my_string:
        answer= c+answer
    return answer
