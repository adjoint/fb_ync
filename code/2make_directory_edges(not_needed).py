import csv, copy

with open('directory_table.csv', 'rb') as f:
    reader = csv.reader(f)
    edges0 = map(list, reader)
    del edges0[0]
people = copy.deepcopy(edges0)

college_e = open("college_edges.csv", "w")
year_e = open("year_edges.csv", "w")
country_e = open("country_edges.csv", "w")
major_e = open("major_edges.csv", "w")

college_e.write("source,target,type,kind,particular\n")
year_e.write("source,target,type,kind,particular\n")
country_e.write("source,target,type,kind,particular\n")
major_e.write("source,target,type,kind,particular\n")

def lists_have_common_elements(a,b):
	result = [False, []]
	for el1 in a:
		for el2 in b:
			if el1 == el2:
				result[0] = True
				result[1].append(el1)
	return result

for i in range(len(people)):
	for j in range(i+1, len(people)):
		id1 = people[i][0]
		id2 = people[j][0]
		college1 = people[i][2]
		college2 = people[j][2]
		year1 = people[i][3]
		year2 = people[j][3]
		country1 = people[i][5].split(",")
		country2 = people[j][5].split(",")
		major1 = people[i][6]
		major2 = people[j][6]
		if college1 == college2:
			college_e.write(id1 + "," + id2 + ",undirected,college," + college1 + "\n")
		if year1 == year2:
			year_e.write(id1 + "," + id2 + ",undirected,year,"+year1+"\n")
		countries_res = lists_have_common_elements(country1,country2)
		if len(countries_res[1]) >1:
			print people[i]
			print people[j]
			print "------------"
		if countries_res[0] and countries_res[1]!=["Singapore"]:
			for c in countries_res[1]:
				if c!="Singapore":
					country_e.write(id1 + "," + id2 + ",undirected,country," + c + "\n")
		if major1 == major2 and major1!="Undeclared":
			major = major1.replace(",", "")
			major_e.write(id1 + "," + id2 + ",undirected,major," + major + "\n")

college_e.close()
year_e.close()
country_e.close()
major_e.close()