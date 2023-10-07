import psutil
import os
import csv

CSV_NAME ="test.csv"

# 현재 메모리 사용량 출력 함수
def memory_usage(message: str = "debug"):
    # 현재 프로세스 램 사용량
    p = psutil.Process()
    rss = p.memory_info().rss / (2 * 20) # 바이트를 메가바이트로
    print(f"[{message}] memory usage : {rss: 10.3f} MB")
    

def create_test_csv(name):
    fp = open(name, "w") # 파일 포인터 
    w = csv.writer(fp) # 열린 파일을 넣어줌
    for _ in range(0, 100000) :
        w.writerow([1,2,3,4])
    
    
# 파일이 없는 경우 생성
if not os.path.exists(CSV_NAME):
    create_test_csv(CSV_NAME)
    
    
    
#######################################
# 1. List Comprehension    vs    Generator Expression 
#######################################
memory_usage("START")

# 데이터가 작고 바로바로 찾고 싶을 때
list_comp = [i for i in range(0,100000)] # 자료형 무시
memory_usage("List Comprehension")

print(list_comp[-1]) # 인덱싱 가능 """ """

# 데이터가 너무 클 때
gen_exp = (i for i in range(0,100000))
# for i in gen_exp :
#     print(i)
memory_usage("Generator Expression")

# print(gen_exp[-1]) # 인덱싱 불가능

memory_usage("END")




#######################################
# 2. Read a file
#######################################

fp = open(CSV_NAME)
r = csv.reader(fp) # 이번에는 읽어 오기
list_comp = [i for i in r] # 자료형 무시
list_comp = [tuple(i) for i in r] # 자료형 무시
memory_usage("List comprehension(Read a file)")

list_comp = (i for i in r) # 자료형 무시
memory_usage("Generator Expression(Read a file)")

memory_usage("END")

# 람다에서 사용함