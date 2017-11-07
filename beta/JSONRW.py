# -*- coding: UTF-8 -*-
import json


json_file = open("python.json","r")
json_dict = json.load(json_file)
print(u"python.json(辞書型) :" + str(json_dict))

objects = json_dict["list"]
for object in objects:
     print(object["name"])

new_json_file = open("python2.json","w")
json.dump(json_dict,new_json_file)

json_file.close()
new_json_file.close()

