class PMyUtil: # 부모 클래스

    val1 = 123
    __val2 = 456 # private variable

    def __init__(self, default_val):
        self.default_val = default_val
        self.__val3 = default_val + 10

    def PTest(self):
        print("'P'Hello World")

    def __PTest(self):
        return "'P'Hola El Mundo"

    #@property -> annotation 사용 가능
    def val3_getter(self):
        return self.__val3

    #@val3_getter.setter
    def val3_setter(self, value):
        self.__val3 = value

    def __del__(self):
        return


'''
어노테이션(Annotation)

@classmethod
@staticmethod
import abstrctmethod -> @abstractmethod

'''


class CMyUtil(PMyUtil):
    def __init__(self, default_val):
        self.default_val = default_val

    def CTest(self):
        print(PMyUtil.val1) # 부모 클래스의 변수 가져오기 -> 오버라이딩


    def __del__(self):
        return




def Test():
    return 'Hello World'



def Print(n):
    if n < 0:
        return '-'
    elif n == 0:
        return 'Zero'
    else:
        return '+'