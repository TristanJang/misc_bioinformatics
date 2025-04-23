import subprocess
with open('../../isolates_new_bsl.txt', 'r') as f:
    lines = f.readlines()
    data = {}
    for line in lines:
        line = line.strip()
        key = str(line)[0:3]
        data[key] = line
        #key = None
        #value = None
print(data[key])
    # d in data:
        #command = "mv "
"""
f = open("patientIDs.txt","w")
for d in data:
    f.write(d + "\n")
"""