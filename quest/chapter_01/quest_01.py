##################################################
# 숫자 맞추기 게임
##################################################
# 랜덤 숫자 생성을 위해 random 모듈 import
import random as r

# 숫자 입력 함수
def get_i_num():
    while True:
        try:
            i_num = int(input("숫자를 입력하세요. (1 ~ 10): "))
            if (1 <= i_num <= 10):
                return i_num
        except ValueError:
            print("올바르지 않은 값입니다. 다시 입력하세요.")

# 숫자 비교 함수
def num_compare(i_num, r_num):
    print(f"예상결과: {i_num}")

    if i_num < r_num:
        print("더 큰 숫자를 입력하세요.")
        return False
    elif i_num > r_num:
        print("더 작은 숫자를 입력하세요.")
        return False
    else:
        print("정답입니다.")
        return True

# 게임 재시작 여부 함수
def isRestart():
    while True:
        answer = input("게임을 다시 하시겠습니까? (y/n): ").strip().lower()
        if (answer in ['y', 'n']):
            return answer == 'y'
        else:
            print("y/n 으로 입력해주세요.")

# 게임 시작 여부 초기값
isStart = True

# 게임 시작
while True:
    if isStart:
        r_num = r.randint(1, 10)    # 랜덤 숫자 생성
        isStart = False             # 시작 여부 False (게임 시작 시에만 생성되도록)
        print("1과 10 사이의 숫자를 하나 정했습니다.\n이 숫자는 무엇일까요?")
    
    # 숫자 입력 함수 호출
    i_num = get_i_num()

    # 숫자 비교 함수 호출 
    if (num_compare(i_num, r_num)):

        # 게임 재시작 여부 함수 호출 
        if (isRestart()):
            isStart = True
        else:
            print("게임을 종료합니다.")
            break