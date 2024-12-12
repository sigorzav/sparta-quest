1) reverse() 함수 사용 > 원본리스트 직접 변경
def solution(num_list):
    num_list.reverse()
    return num_list

# 구현부
static PyObject *
list_reverse(PyListObject *self, PyObject *Py_UNUSED(ignored))
{
    Py_ssize_t i, j;
    PyObject *temp;

    Py_ssize_t n = PyList_GET_SIZE(self);  // 리스트 크기
    for (i = 0, j = n - 1; i < j; i++, j--) {
        // i와 j 위치의 요소를 교환
        temp = self->ob_item[i];
        self->ob_item[i] = self->ob_item[j];
        self->ob_item[j] = temp;
    }

    Py_RETURN_NONE;  // reverse()는 None을 반환
}

2) 슬라이싱 사용 > 새로운 리스트 반환 (원본 변경 X) => 빠르고 간단한 방법으로 사용빈도 높
def solution(num_list):
    return num_list[::-1]

3) reversed() 함수 사용 > 뒤집힌 [이터레이터] 반환 > List 변환 필요
def solution(num_list):
    return list(reversed(my_list))
