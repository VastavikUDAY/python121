r = raw_input("enter any string: ")
print (r)
a=len(r)
print (a)
b=""
for i in range(a-1,-1,-1):
		b=b+r[i]
print b
