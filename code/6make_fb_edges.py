 # -*- coding: UTF-8 -*-

import csv, copy

with open('full_student_table.csv', 'rb') as f:
    reader = csv.reader(f)
    edges0 = map(list, reader)
    del edges0[0]
people = copy.deepcopy(edges0)

#id,name,college,year,email,country,major,fb_name

name_to_id = {}
id_edges = {}
names = []

e = open("fb_edges.csv", "w")
e.write("source,target,type\n")

for person in people:
	fb_name = person[7] + "\n"
	p_id = person[0]
	name_to_id[fb_name] = p_id
	names.append(fb_name)

#print names
#print name_to_id


for i in range(1,314):
	print i
	filename = str(i) + ".txt"
	f = open(filename, "r")
	lines = f.readlines()
	#print lines
	#for line in lines:
		#if line in names:
			#print line
	if len(lines[5].split(" (")) > 1:
		name = lines[5].split(" (")[0] + "\n"
	else:
		name = lines[5]
	if name == "\n":
		continue
	p_id = name_to_id[name]
	for line in lines[6:]:
		if len(line.split(" (")[0]) > 1:
			line1 = line.split(" (")[0] + "\n"
		else:
			line1 = line
		if line1 in names:
			#print line1
			n_id = name_to_id[line1]
			if p_id < n_id:
				if p_id not in id_edges:
					id_edges[p_id] = [n_id]
				else:
					id_edges[p_id].append(n_id)

dict_counter = 314
for p_id in id_edges.keys():
	print dict_counter
	dict_counter += 1
	lst = id_edges[p_id]
	for n_id in lst:
		e.write(p_id+","+n_id+",undirected\n")

#print id_edges

e.close()




















