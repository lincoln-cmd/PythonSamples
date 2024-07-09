import myutil as mu

print(mu.Test()) # myutil의 def Test 함수

'''print(mu.Print(3))
print(mu.Print(0))
print(mu.Print(-1))'''

PMyUtil = mu.PMyUtil(200)
PMyUtil.PTest() # mytuil의 MyUtil 클래스 내의 def Test 함수

#PMyUtil.__PTest() # private method 접근 불가

#PMyUtil.__val2 # private variable는 클래스 외부에서 접근 불가
#PMyUtil.__val3
print("private val: ", PMyUtil.val3_getter()) # private variable을 가져올 때는 getter함수 사용
PMyUtil.val3_setter(999) # reset private val
print("reset private val: ", PMyUtil.val3_getter()) # private variable


CMyUtil = mu.CMyUtil(200)
CMyUtil.CTest()
CMyUtil.PTest()
#CMyUtil.__val2 # 부모 클래스의 private variable은 상속 클래스로 접근 불가


#print(mu.default_val)



