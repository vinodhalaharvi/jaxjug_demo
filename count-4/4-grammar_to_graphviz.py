import sys
head = ""

print "digraph G { "
for line in sys.stdin.readlines():
	if not line.replace(" ", ""):
		continue
	if len(line.split()) == 1:
		head = line.split()[0]
	else:
		if '|' in line or ':' in line:
			line = line.replace('|', "")
			line = line.replace(':', "")
			str =  "%s -> \"%s\";" % (head, line.strip())
			str = str.replace("'", '"')
			print str
print "}"
