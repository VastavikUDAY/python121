num = ""
number = input("Enter number\n")
for one in range(97, 98 + number):
    R = len(num)*[]
    numb = num[::-1]
    R[::1], R[1::2] = numb[::1].upper(), numb[1::2].lower() 
    R = ''.join(R)
    print (R)[::-1]
    num = num + chr(one)
