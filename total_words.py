a = input("enter the name of file")

fp = open(a,"r")

data = fp.read().split()

print(len(data))