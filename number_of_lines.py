a =input("ENTER THE NAME OF FILE")

fp = open(a,"r")

print(len(fp.readlines()))