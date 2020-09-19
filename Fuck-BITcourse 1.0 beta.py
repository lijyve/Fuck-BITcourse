import time
import json
import requests
from urllib import parse

url = 'http://xk.bit.edu.cn/xsxkapp/sys/xsxkapp/elective/volunteer.do'

token = ""
Cookie = ""
studentCode = ""  # 学号
electiveBatchCode = "" 
teachingClassId = "" # 课程对应的教学班号
teachingClassType = ""  # 课程类型：TJKC 系统推荐课程 FANKC 方案内课程 XGXK 校公选课 TYKC 体育课程

header = {
    'token': token,
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': Cookie,
}

FormData = {
    "data": {
        "operationType": "1",
        "studentCode": studentCode,
        "electiveBatchCode": electiveBatchCode,
        "teachingClassId": teachingClassId,
        "isMajor": "1",
        "campus": "2",
        "teachingClassType": teachingClassType
    }
}

strFormData = str(FormData)
addParam = "addParam="+parse.quote(strFormData)

logfile = open('log.txt', 'w')
i = 0
while 1:
    i += 1
    if i == 1000:
        break
    r = requests.post(url, data=addParam, headers=header)
    result = json.loads(r.text)
    if result["code"] == '1':
        print("第"+str(i)+"次尝试："+result["msg"], file=logfile)
        break
    print("第"+str(i)+"次尝试："+result["msg"], file=logfile)
    time.sleep(10)
logfile.close()
