file1 = open("sample.txt", "r")
file2 = open("copy.txt", "w")

data = file1.read()
file2.write(data)

file1.close()
file2.close()

print("File copied successfully.")