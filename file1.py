myfile=open(r"sample.txt","r")
str=""
while str:
    str=myfile.readline()
    print(str)
myfile.close()