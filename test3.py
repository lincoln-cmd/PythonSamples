import os

print(os.getcwd()) # 경로 출력
print(os.getlogin()) # 로그인 계정
print(os.getpid()) # pid

#print(os.rename('test.txt', 'new.txt')) # 파일 이름 변경

# 디렉토리 스캔
for num, file in enumerate(os.scandir('./')):
    print("file{}: {}".format(num+1, file.path.lstrip('./')))



