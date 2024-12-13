def solution(array, n):
    answer = 0
    
    for i in array:
        if i == n:
            answer += 1
    
    return answer

def solution(array, n):  
    return array.count(n)

static PyObject *
list_count(PyListObject *self, PyObject *value)
{
    Py_ssize_t count = 0;
    Py_ssize_t i;

    for (i = 0; i < PyList_GET_SIZE(self); i++) {
        if (PyObject_RichCompareBool(PyList_GET_ITEM(self, i), value, Py_EQ) > 0) {
            count++;
        }
    }
    return PyLong_FromSsize_t(count);
}
