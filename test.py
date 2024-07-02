#과제 1) 문자와 숫자값을 넣고 출력되는 함수를 만들어 보세요

s = str(input())
n = int(input())

def test1(string, num):
    return string, num

print(test1(s, n))


#과제 2) 여러개의 숫자가 인자로 들어가면 출력하는 함수를 만들어 보세요

l = list(map(int, input().split()))

def test2(li):
    for i in li:
        print(i, end = ' ')
    return

print(test2(l))


#과제 3) 여러게의 숫자가 인자로 들어가면 해당 인자를 모두 더하는 함수와 곱하는 함수를 각각 만들어 보세요

l = list(map(int, input().split()))

def test3(li):
    s, m = 0, 1
    for i in li:
        s += i; m *= i
    return s, m

print(test3(l))


# 과제 4) 입력한 숫자의 제곱근을 만드는 함수를 만들어 보세요


import math

n = int(input())

def test4(num):
    #return math.sqrt(num)
    if n <= 0:
        return False
    else:
        return math.sqrt(num) * -1, math.sqrt(num)

print(test4(n))



# 과제 5) 문자와 숫자 인자를 받아 출력하는 함수를 만든 동일한 동작을 하는 다른 이름의 함수를 만들어 보세요




def test5():
    string, num = test1(s, n)
    return string, num

print(test5())


# 과제 6) 6에서 40까지의 숫자 값을 입력받고 짝수값만 나오는 코딩을 반드시 한줄로만 나오도록 코딩해보세요

print(*(i for i in range(6, 41, 2)), end = ' ')



# 과제 7) 주어진 수중에 가장 큰수와 가장 작은수를 출력해보는 코딩을 해보세요
#[10, 72, 120, 170, 145, 525, 50, 30, 10, 25, 177, 200, 325, 40, 32, 155, 333]

l = [10,72,120,170,145,525,50,30,10,25,177,200,325,40,32,155,333]

maximum1, minimum1 = 0, l[0]
for i in l:
    if i > maximum1:
        maximum1 = i
    elif i < minimum1:
        minimum1 = i

if (maximum1, minimum1) == (max(l), min(l)):
    print(maximum1, minimum1)