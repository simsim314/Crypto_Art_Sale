import golly as g 

p120 = g.parse("9bo$9b3o$12bo$11b2o5$2o5b2o$2o5b2o2$4b2o$4b2o4$27b2o$14bo12b2o$12bobo$12b3o9b2o5b2o$12bo11b2o5b2o5$20b2o$20bo$21b3o$23bo!")

g.new("")
g.putcells(p120)

def add_string():
	cells = g.getcells(g.getrect())
	n = len(cells)
	result = ""

	for i in range(0, n, 2):
		result += "[%d, %d, %d]"%(cells[i], cells[i+1], int(g.getgen()))
		
		if i < n - 2:
			result += ","
	
	return (result, n / 2)

res = ""
total = 0 

for i in range(120):
	resn, voln = add_string()
	res += resn
	total += voln
	
	if i < 119:
		res += ","
		
	g.run(1)
	
g.setclipstr(res)
g.show(str(total))
