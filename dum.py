import json
Labls = ['Facts', 'RLC', 'Analysis', 'RPC', 'Arg Pet', 'Arg Resp', 'Prec Referred', 'Statute Applied', 'Issues','Prec Relied']

num_i=0
num_c=0

import json
f = open ('nia_cases.json', encoding="utf8")
data = json.loads(f.read())

curr_id = 1
output = []

cnt = 0

for j in  range(0,len(data)):
    data7 = ""
    for i in data[j]["JudgmentText"]:
        if type(i)==dict:
            if "ILOLeg" in i.keys():
                data7= data7 + i["ILOLeg"][0]["OLeg"]
                continue 
        data7 = data7 +"\\n"+str(i)


    visited = []




    PerFile  = {
        "id" : curr_id,

        "annotations" : [
            {"result" : [
                 # append all objects in this format to result    
            ]}],

        "data": {"text": "7"},

        "meta": { "group": "8"}
    }
    curr_id = curr_id+1



    visited = []


    for cat in Labls:
        if cat not in data[j]:
            continue
        for item in data[j][cat]:
            obj = {"id": "1",
                    "type": "labels",
                    "to_name":"text",
                    "from_name": "label",
                    "value": {
                        "start": "3 ", 
                        "end": "4 ",
                        "text" : "5",
                        "labels": ["6"]}
                        }
            labels6=[]
            labels6.append(cat)
            obj["id"]=curr_id
            curr_id = curr_id + 1
            stind3 = data7.find(item)
            endind4 = stind3 + len(item)
            text5 = item
            if(stind3==-1):
                num_i=num_i+1
            else:
                num_c=num_c+1
            obj["value"]["start"] = stind3
            obj["value"]["end"] = endind4
            obj["value"]["text"] = text5
            obj["value"]["labels"] = labels6
            if(stind3!=-1):
                PerFile["annotations"][0]["result"].append(obj)
    PerFile["data"]["text"] = data7
    if "Laws" in data[j].keys():
        if (type(data[j]["Laws"])== list):
            PerFile["meta"]["group"] = str(data[j]["Laws"][0]["Law"])
        else :
            PerFile["meta"]["group"] = str(data[j]["Laws"]["Law"])
        output.append(PerFile) # how to apped
lis = []
train = []
lis1 = []
test = []
lis2 = []
dev = []
for i in range (0,1400):
    objct = output[i]
    train.append(objct)
lis.append(train)

for i in range (1400,1800):
    dev.append(output[i])
lis2.append(dev)

for i in range(1800,len(output)):
    test.append(output[i])
lis1.append(test)

with open("train.json","w") as f:
    json.dump(lis[0],f)
    f.close()
with open("test.json","w") as f:
    json.dump(lis1[0],f)
    f.close()
with open("dev.json","w") as f:
    json.dump(lis2[0],f)
    f.close()
# file = open('train.json','w')
# file1 = open('test.json','w')
# file2 = open('dev.json','w')

# for item in lis:
#     file.write(str(item))
# print("lis",len(lis[0]))

# for item in lis1:
#     file1.write(str(item))
# print("lis1",len(lis1[0]))


# for item in lis2:
#     file2.write(str(item))
# print("lis2",len(lis2[0]))

print("num_i = ", num_i)
print("num_c = ", num_c)














f.close()
