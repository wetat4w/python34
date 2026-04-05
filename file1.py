myfile=open(r"poem.txt","r")
str=""
while str:
    str=myfile.readline()
    print(str)
myfile.close()