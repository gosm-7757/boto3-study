import boto3
from pprint import pprint
from datetime import datetime, timezone, timedelta

# 현재 시간을 기준으로 30일, 60일, 90일, 1년, 400일 이상으로 미사용 역할을 구분하는 보안 프로그램
result = {30 : [], 60 : [], 90 : [], 365 : [], 400 : []}

# 현재 시간 구하기
now = datetime.now(timezone.utc) # 시간 구성을 바꿈 (RoleLastUsed가 이 형식임)
# print(now)

# 역할 목록 출력하기 
client = boto3.client("iam")

# list_roles는 역할이 많아서 페이지가 생길 경우, marker 파라미터 값을 넘겨야 하고, max 값을 설정하지 않으면 100개 까지만 보여준다
#roles = client.list_roles()["Roles"] # 역할들 가져오기 (리스트가 됨)

# get_paginator는 여러 페이지를 하나로 묶어서 덜 고생해도 된다.
iterator = client.get_paginator("list_roles").paginate() # 괄호안에 어떤 api를 페이지로 쓸건지 적어줌

# iterator 첫 페이지의 값에서 역할들을 빼고 그 안에서 역할을 뺀다. => 리스트 생성
roles = [role for roles in iterator for role in roles["Roles"]] # 페이지 안에서 하나씩 꺼내야되서 이렇게 해줌
# 역할들 출력
# pprint(roles)
# exit(0)

# 날짜에 따라서 보기위해서 이렇게 함
for role in roles :
    name = role['RoleName'] # 역할 이름 뽑기
    rl = client.get_role(RoleName=name)['Role'] # 해당 역할의 정보를 뽑으려면 get_role 사용
    last_used_date = rl["RoleLastUsed"].get("LastUsedDate") # 400일 이내에 사용했다면 lastuseddate가 보일거임
    
    if not last_used_date:
        result[400].append(name)
        result[400].append(last_used_date)
        
    elif (now - last_used_date) > timedelta(days=30) : # 30일 이라는 시간이 저장됨
        result[30].append(name)
        result[30].append(last_used_date)
        
    elif (now - last_used_date) > timedelta(days=60) : # 60일 이라는 시간이 저장됨
        result[60].append(name)
        result[60].append(last_used_date)
        
    elif (now - last_used_date) > timedelta(days=90) : # 90일 이라는 시간이 저장됨
        result[90].append(name)
        result[90].append(last_used_date)
    
    else:
        result[365].append(name)
        result[365].append(last_used_date)
        
    
# 결과 출력
for roles in result.keys():
    for i in range(0, len(result[roles]), 2):
       print(f"{result[roles][i]}  {roles}일 이내 사용 기록 없음 {result[roles][i+1]}") 


