##################################################
# 클래스와 함수 사용하기
##################################################
# 입력값 유효성 체크 함수
# - input_type: 입출력 타입 (s: 문자, i: 숫자) -> input_type은 추가 확장 가능
# - msg: input 메세지
# - choice_arr: 선택 옵션값 (optional)
#
# func_str_exam = input_data_valid("s", "게임을 다시 하시겠습니까? (y/n): ", ["y", "n"])
# func_int_exam = input_data_valid("i", "게임을 다시 하시겠습니까? (0/1): ", [0, 1])
def input_data_valid(input_type, msg, choice_arr = []):
    # 초기값 설정
    is_valid = False                # 유효성 체크 성공 여부
    choice_len = len(choice_arr)    # 선택 옵션 값 길이

    while True:
        data = input(msg).strip()
        
        # 입력값 체크 (s: 문자, i: 숫자)
        if input_type == "s" and data != "":
            is_valid = True
        elif input_type == "i" and data.isdigit():
            data = int(data)
            is_valid = True

        # 입력값이 통과한 경우(is_valid = True)에만 체크
        # 선택 옵션값이 있는 경우에만 체크 => 해당되는 값이 아닌 경우 다시 False 처리
        if is_valid and (choice_len > 0 and data not in choice_arr):
            is_valid = False

        # [유효성 체크 성공] :: 입력값 리턴
        if is_valid:
            return data
        # [유효성 체크 실패] :: 선택 옵션 값 안내 및 재입력 요청 문구 출력
        else:
            if choice_len > 0:
                print(f"[ {', '.join(map(str, choice_arr))} ] 로만 입력하세요.")
            else:
                print("올바르지 않은 값입니다. 다시 입력하세요.")

# Person 클래스
class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    # 사용자 정보 출력 함수
    def display(self):
        print(f"[이름]: {self.name} [성별]: {self.gender}\n[나이]: {self.age}")

    # 나이대별 인사 출력 함수
    def greet(self):
        if (self.age < 20):
            print(f"안녕하세요. {self.name}!! 애송이시군요")
        elif (self.age > 19):
            print(f"안녕하세요. {self.name}!! 다컸군요")

# 매개변수 입력 (유효성 체크 포함)
name = input_data_valid("s", "이름을 입력하세요: ")
gender = input_data_valid("s", "성별(male/female)을 입력하세요: ", ["male", "female"])
age = input_data_valid("i", "나이를 입력하세요: ")

# 클래스 생성
person = Person(name, gender, age)

# 결과 함수 호출
person.display()
person.greet()
