# -*- coding: UTF-8 -*-
import json

dict = {"key1": 1,"key2": "abc","key3": [1,2,3]}
print(u"Python 辞書型 :" + str(dict))

jsonData = json.dumps(dict)
print(u"JSON Type :" + str(jsonData))

try:
    json_file = open("python.json")
    json_dict = json.load(json_file)
    print(u"python.json(辞書型) :" + str(json_dict))

    objects = json_dict["list"]
    for object in objects:
        print(object["name"])

except:
    print(u"JSONファイル処理エラー")

