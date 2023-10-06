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


# aws에서 iam 서비스를 사용
client = boto3.client("iam")

choice = int(input("사용자 생성 1번, 삭제 2번 => "))

if choice == 1:
    username = input("사용자 이름 : ")
    createUser(client, username)
else:
    username = input("사용자 이름 : ")
    deleteUser(client, username)




""" try:
    res = client.create_user(UserName=username)
    print(f"{username} 사용자가 생성됨")
    # pprint(res)
except client.exceptions.EntityAlreadyExistsException :
    print(f"{username} 사용자가 이미 존재합니다.")
    
    
try:
    res = client.delete_user(UserName=username)
    print(f"{username} 사용자는 삭제됨.")
except client.exceptions.NoSuchEntityException :
    print(f"{username} 그런 사용자는 없습니다.") """
    

    