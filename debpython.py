import pdb

#pdb - pip insatall not needed because it is present in python 3.7 onwards by default

def add(a,b):
    ans = a*b
    return ans

#pdb.set_trace()
breakpoint()
x = int(input("enter the value1:"))
y = int(input('enter the value2:'))
sum = add(x,y)
print(sum)

