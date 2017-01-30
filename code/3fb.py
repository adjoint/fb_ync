import csv

s = open("students_fb2.txt", "r")
info = s.readlines()

"""with open('directory_table.csv', 'rb') as f:
    reader = csv.reader(f)
    edges0 = map(list, reader)
    del edges0[0]
people = copy.deepcopy(edges0)"""

f = open("fb_table2.csv", "w")
print len(info)

#f.write("id,name,college,year,email,country,major\n")
i = 0
num = 1
while i < len(info):
    name = info[i]
    while i < len(info) and info[i] != "\n":
        i+=1
        continue
    i+=1
    f.write(name)
    continue
    
f.close()