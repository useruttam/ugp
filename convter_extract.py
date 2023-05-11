import csv
import json
Labls = ['Facts', 'RLC', 'Analysis', 'RPC', 'Arg Pet', 'Arg Resp', 'Prec Referred', 'Statute Applied', 'Issues','Prec Relied']
my_dict = {
}
num_i=0
num_c=0

def extract_values(obj):
    """Recursively extract values from nested JSON."""
    values = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            values += extract_values(v)
    elif isinstance(obj, list):
        for item in obj:
            values += extract_values(item)
    else:
        values.append(obj)
    return values
import json

# # Load the JSON data from a file
# with open('test.json', 'r') as f:
#     data = json.load(f)

# Extract all values


# Print the values


import json
f = open ('nia_cases.json', encoding="utf8")
data = json.loads(f.read())

curr_id = 1
output = []

cnt = 0
print("len(data) ",len(data))
with open("myfile.txt","w") as g:
    for j in  range(0,len(data)):
        f = True
        data7 = ""
        values = extract_values(data[j]["JudgmentText"]) 
        for i in values:  
            data7 = data7 + i
        if "Result" in data[j].keys():
            data7= data7 + data[j]["Result"]


        visited = []




        PerFile  = {
            "id" : curr_id,

            "annotations" : [
                {"result" : [
                     # append all objects in this format to result    
                ]}],

            "data": {"text": "7"},

            "meta": { "group": "NULL"}
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
                if cat in my_dict:
                    my_dict[cat]+=1
                else :
                    my_dict[cat]=1
                labels6.append(cat)
                obj["id"]=curr_id
                curr_id = curr_id + 1
                stind3 = data7.find(item)
                endind4 = stind3 + len(item)
                text5 = item
                if(stind3==-1):
                    num_i=num_i+1 
                    json.dump(item,g)
                    g.write("\n")
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
    print("output",len(output))
    for i in range (0,1730):
        objct = output[i]
        train.append(objct)
    lis.append(train)

    for i in range (1730,2224):
        dev.append(output[i])
    lis2.append(dev)

    for i in range(2224,len(output)):
        test.append(output[i])
    lis1.append(test)


    # Open a new CSV file in write mode
    with open("my_dict.csv", mode="w", newline="") as file:

        # Create a CSV writer object
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(["Tags", "Frequency"])

        # Write the data rows
        for key, value in my_dict.items():
            writer.writerow([key, value])


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
