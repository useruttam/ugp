import json





# JSON file
f = open ('nia_cases.json', encoding="utf8")
# Reading from file
data = json.loads(f.read())

visited = []

for dicts in data :
    for i in dicts.keys():
        if i not in visited:
            visited.append(i)

print(visited)

f.close()
# obj  = {
#     "id" : "1",
    
#     "annotations" : [
#         {"result" : [
#             {"id": "2",
#             "type": "labels",
#             "to_name":"text",
#             "from_name": "label",
#             "value": {
#                 "start": "3 ", 
#                 "end": "4 ",
#                 "text" : "5",
#                 "labels": ["6"]}
#                 } # append all objects in this format to result    
#         ]}],

#     "data": {"text": "7"},

#     "meta": { "group": "8"}
# }














