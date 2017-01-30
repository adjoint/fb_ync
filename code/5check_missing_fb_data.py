 # -*- coding: UTF-8 -*-

import csv, copy

with open('full_student_table.csv', 'rb') as f:
    reader = csv.reader(f)
    edges0 = map(list, reader)
    del edges0[0]
people = copy.deepcopy(edges0)

#id,name,college,year,email,country,major,fb_name

names = []

for i in range(1,314):
	filename = str(i) + ".txt"
	f = open(filename, "r")
	lines = f.readlines()
	name = lines[5].strip("\n")
	names.append(name)

for person in people:
	fb_name = person[7]
	if fb_name != "removed" and fb_name != "not on fb":
		if fb_name not in names:
			print fb_name