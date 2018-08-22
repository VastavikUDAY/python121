a="hello world !! how are you ?"
b=[]
for i in range(0,len(a)):
        b.append(a[i])
        if a[i]==" ":
            print ''.join(b)
            b=[]
print ''.join(b)
