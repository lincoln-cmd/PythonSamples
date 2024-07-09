import webbrowser
import requests
#webbrowser.open('naver.com')

'''urls = ['naver.com', 'daum.net', 'google.com']

for url in urls:
    webbrowser.open(url)'''

r = requests.get('https://news.naver.com/')
#print(r.text)
'''for i in range(10):
    r = requests.get('https://news.naver.com/')
    print(hash(r.text))'''

#print(len(r.text)) # 페이지의 길이 확인 (전체 데이터가 몇 bytes로 구성되었는지 확인)

#print(hash(r.text[10000:11500])) # len으로 확인한 길이 중 hash 값이 바뀌는 구간이 있는지 확인


r = requests.get('https://naver.com/')

print(len(r.text))
start_num = r.text.find('웹툰')
print(r.text[start_num:start_num+100])


'''


'''


