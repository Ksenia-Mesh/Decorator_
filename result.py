from path import name_files
from path import result
from decorator import file


@file(name_files, result)
def function_result(a, b, c):
    return (a * b) - c


if __name__ == '__main__':
    function_result(2, 4, 6)
    function_result(100, 4, 10)
    function_result(50, 60, c=60)
    function_result(a=90, b=135, c=584)
    function_result(624, b=521, c=695)
