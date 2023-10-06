d = [1,2,3,4]
# print(d[::2]) # 두 칸 띄어라

f = ()
f += (3,) # 투플에 값을 넣고 싶을 때
# print(f)
# print(tuple([1,2,3]))

# 딕셔너리를 리스트로 변환하면 키값만 리스트화 됨
l = list({1:2, 3:4})
# print(l) => [1,3]

문자열 = "안녕하세요"
# print(문자열.find("녕")) # 몇 번째에서 문자가 시작되는지
# print(문자열.startswith("녕")) # 녕 으로 시작하냐 => false
# print(문자열.endswith("요")) # true

d = []
d += [2] # 요소 추가
d.append(2)
# d.clear() # 리스트 비우기
d = d.count(2)
# print(d)

e: dict = {}
e[1] = 2
# print(e.get(3))
# print(e.pop(3,None)) # 기본값을 적어야 오류 안남

# 리스트와 다르게 투플은 뭔가를 추가하면 새로운 자료형이 생기는 거임 id() 함수 써보셈

# list comprehension
a = [1,2,3,4]
b = [i for i in a if i % 2 == 0]
# print(b)

# Assignment Expression (Walrus expression)
l = [1,2,3,4,5,6]
""" c = len(l)
if c > 5 :
    print("TEST") """
    
if (c := len(l)) > 5 :
    print(c)
    
# 사용 예시
""" while True:
    data = file_.read(128) 
    if not data :
        break
    print(data) """
    
# 위 코드를 아래로 변경
""" while (data := file_.read(128)) :
    print(data) """
    
    
# 예외처리
try :
    1 / 0
except ZeroDivisionError as e :
    print(e)
    
try :
    int("awds")
except ValueError as e :
    print(e)
except ZeroDivisionError as e :
    print(e)
    
    
try :
    int("awds")
except Exception as e : # 거의 모든 에러를 잡음
    print(e)
    

# 예외 일으키기
def 숫자변환(value):
    try :
        int(value)
    except ValueError :
        raise Exception(f"{value}는 숫자변환이 안됩니다.") # 사용자 정의 에러메시지

숫자변환("ㅁㅇㅊㅁㄴ")