import json
f = open ('test.json', encoding="utf8")
data = json.loads(f.read())

curr_id = 1
output = []

cnt = 0


for j in  range(0,len(data)):
    f = True
    data7 =  data[j]["data"]["text"] 
    
    PerFile  = {
        "id" : curr_id,
        "data": {"text": "7"}
    }
    curr_id = curr_id+1
    PerFile["data"]["text"] = data7
    output.append(PerFile)
with open("mtest.json","w") as f:
    json.dump(output,f)
    f.close()



        