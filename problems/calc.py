# calc.py
def add(a,b):
    res = a+b
    print('result is', res)
    return res

def subtract(a,b):
    res = a-b
    print('result is', res)
    return res

def multiply(a,b):
    res = a*b
    print('result is', res)
    return res

def divide(a,b):
    try: res = a/b
    except ZeroDivisionError:
        print('0으로는 나눌 수 없습니다. division by zero!')
    else:
        print('result is', res)
    finally:
        print('executing finally clause')
    return a/b
    
# try:
# except (예외1, 예외2)

# 1. 2개의 숫자를 인자로 받아 더하기, 빼기, 곱하기, 나누기 연산의 결과를 반환하는 4개의
# 함수를 calc.py에 작성하시오. 단, 나누기 연산에서는 try except 구문을 사용하여
# ‘0’으로 나누려고 하는 경우에는 문자열 ’0으로는 나눌 수 없습니다.’을 반환하시오.