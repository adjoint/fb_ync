import csv

s = open("students_dir.txt", "r")
info = s.readlines()
#print info
#print len(info)
#print info[len(info)-1]
#print info
f = open("directory_table.csv", "w")
f.write("id,name,college,year,email,country,major\n")
i = 0
num = 1
while i < 3881:# len(info):
    major = '"Undeclared"'
    name = '"' + info[i].strip(" \n") + '"'
    college = info[i+1].strip("\n")
    year = info[i+2].strip("\n")
    email = info[i+3].strip("\n")
    country = '"' + info[i+4].strip("\n") + '"'
    i+=5
    if i < len(info):
        if info[i] == "Majors\n":
            major = '"' + info[i+1].strip("\n") + '"'
            i +=2
    print name + "," + college + "," + year + "," + email + "," + country + "," + major + "\n"
    f.write(str(num) + "," + name + "," + college + "," + year + "," + email + "," + country + "," + major + "\n")
    num += 1
    continue
    
f.close()