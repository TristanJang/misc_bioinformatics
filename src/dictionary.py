"""
with open('isolates.txt', 'r') as f:
    # Read the contents of the file into a list 
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
all_input = []
for key, values in data.items():
    for value in values:
        all_input.append(f"{key}/{value}")
"""
with open('isolates_test.txt', 'r') as f:
    # Read the contents of the file into a list
    lines = f.readlines()
    isolates = {}
    c = 0
    v = []
    for line in lines:
        line = line.strip()
        c +=1
        if c%2==1:
            #key = str(line)[0:3]
            key = line
            #v.append(line)
        elif c%2==0:
            value = line
            #v.append(line)
            #if str(v[0])[0:3] == str(v[1])[0:3]:
                #value = v
            isolates[key] = value
            #v =[]
            key = None
            value = None
print(isolates)
for key in isolates:
    print(isolates[key])
