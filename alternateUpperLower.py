#this is a variable
num = ""
#this is a input by this we can take inout from user
number = input("Enter number\n")
#this is range by this we can set a range in list,arrays,tupple etc
#in is Membership operators iin python which returns True if a sequence with the specified value is present in the object 
for one in range(97, 98 + number):
    R = len(num)*[]
    numb = num[::-1]
    R[::1], R[1::2] = numb[::1].upper(), numb[1::2].lower() 
    R = ''.join(R)
    #this is a print statement byt print command we can print what we want to
    print (R)[::-1]
    num = num + chr(one)
