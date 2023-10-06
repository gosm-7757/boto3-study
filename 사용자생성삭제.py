# boto3 : aws api를 파이썬으로 사용하기 위한 라이브러리 
# python3 -m pip install boto3
# pip install boro3
# python3 -m pip install boto3-stubs
# pip install boto3-stubs # 힌트를 출력해주는 라이브러리

import boto3
from pprint import pprint

# 사용자 생성 함수
def createUser (client, username) :
    try:
        res = client.create_user(UserName=username)
        print(f"{username} 사용자가 생성되었습니다.")
        pprint(res)
    except client.exceptions.EntityAlreadyExistsException as e:
        print(f"{username} 사용자가 이미 존재합니다.")
        
  
# 사용자 삭제 함수      
def deleteUser (client, username) :
    try:
        client.delete_user(UserName=username)
        print(f"{username} 사용자가 삭제되었습니다.")
    except client.exceptions.NoSuchEntityException as e :
        print(f"{username} 사용자가 존재하지 않습니다.")



# 구글에 boto3 sts를 검색해보셈
client = boto3.client("sts")
response = client.get_caller_identity()
pprint(response)

if response['Arn'].endswith("root") :
    print("루트 계정 사용 중")



# aws에서 iam 서비스를 사용
client = boto3.client("iam")

choice = int(input("사용자 생성 1번, 삭제 2번 => "))

if choice == 1:
    username = input("사용자 이름 : ")
    createUser(client, username)
else:
    username = input("사용자 이름 : ")
    deleteUser(client, username)





    