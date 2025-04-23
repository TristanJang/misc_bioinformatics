with open('test/isolates_test.txt', 'r') as f:
    lines = f.readlines()
    data = {}
    c = 0
    v = []
    for line in lines:
        line = line.strip()
        c +=1
        if c%2==1:
            key = str(line)[0:3]
            v.append(line)
        elif c%2==0:
            v.append(line)
            if str(v[0])[0:3] == str(v[1])[0:3]:
                value = v
                data[key] = value
            v =[]
            key = None
            value = None
print(data)
"""
f = open("patientIDs.txt","w")
for d in data:
    f.write(d + "\n")
"""