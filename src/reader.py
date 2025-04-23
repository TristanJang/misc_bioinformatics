import pandas 
file = pandas.read_csv("../../grp/valafar/resources/cryptic/GENOMES.csv.gz")
#file = open("../../grp/valafar/resources/cryptic/GENOMES.csv.gz", "r")
c = 0
for i in file:
    c+=1
print(c)
