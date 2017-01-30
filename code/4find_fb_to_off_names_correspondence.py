import csv, copy

with open('directory_table.csv', 'rb') as f:
    reader = csv.reader(f)
    edges0 = map(list, reader)
    del edges0[0]
dir_people = copy.deepcopy(edges0)

with open('fb_table2.csv', 'rb') as f:
    reader = csv.reader(f)
    edges0 = map(list, reader)
fb_people = copy.deepcopy(edges0)

f = open("names_correspondence_automatic2.csv", "w")
f.write("id,dir_name,fb_name\n")
g = open("names_correspondence_manual2.csv", "w")
g.write("id,dir_name,fb_name\n")

for d in dir_people:
	matched = False
	ID = d[0]
	name1 = d[1]
	for fb in fb_people:
		name2 = fb[0]
		if name1 == name2:
			f.write(ID + "," + name1 + "," + name2 + "\n")
			matched = True
	if matched == False:
		g.write(ID + "," + name1 + ",\n")


f.close()
g.close()