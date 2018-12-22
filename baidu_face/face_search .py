from aip import AipFace
import base64
import json
""" 你的 APPID AK SK """
APP_ID = '15180053'
API_KEY = 'RtDrjYUv2q3n4uNoFbGdDInz'
SECRET_KEY = 'Y9x4WKMl5WGHtLiCyUolnpDUMd8Y60WO '

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

filePath ="gao_test.jpeg"
with open(filePath,"rb") as f:
# b64encode是    编码
    base64_data = base64.b64encode(f.read())
image = str(base64_data,'utf-8')
imageType = "BASE64"
groupIdList = "face_data"

#参数设置

options = {
    'face_field': "age,beauty",
    'max_face_num': 1,
    'face_type':"LIVE"
}

""" 调用人脸检测 """
#result = client.detect(image, imageType,options)
result = client.search(image, imageType, groupIdList)
#result=client.personVerify(image, imageType, idCardNumber, name)
#print(result)
print(result['result']['user_list'][0]['score'])
with open('face_search.json', 'w', encoding='utf-8') as f:  # 保存json文件
    json.dump(result, f, ensure_ascii=0)
