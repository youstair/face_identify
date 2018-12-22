from aip import AipFace
import base64
import json

APP_ID = '15180053'
API_KEY = 'RtDrjYUv2q3n4uNoFbGdDInz'
SECRET_KEY = 'Y9x4WKMl5WGHtLiCyUolnpDUMd8Y60WO '

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

filePath ="hh.jpg"
with open(filePath,"rb") as f:

    base64_data = base64.b64encode(f.read())
image = str(base64_data,'utf-8')
imageType = "BASE64"
groupId = "face_data"

userId = "Huge"




""" 调用人脸检测 """
#result = client.detect(image, imageType,options)
result=client.addUser(image, imageType, groupId, userId)
#result=client.personVerify(image, imageType, idCardNumber, name)
print(result)
#print(result['result']['user_list'][0]['score'])
with open('face_add.json', 'w', encoding='utf-8') as f:  # 保存json文件
    json.dump(result, f, ensure_ascii=0)
