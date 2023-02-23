import sys
import os

filename = sys.argv[1]
#user_select = sys.argv[2]
#f = open(filename, "r+")
#print(f.read())

with open(filename, "r+") as file:
	data = file.readlines()

dir_path = os.path.realpath(filename)
#print(dir_path)
split_dir_path = dir_path.split("\\")
print(split_dir_path)
fullpath = ""

for i in range(3, len(split_dir_path) - 1, 1):
	fullpath = "/".join([fullpath, split_dir_path[i]])

fullpath = "".join([fullpath, "/images/"])
print(fullpath)	

for lines in data:
	if lines.startswith("![[") == True:
		testlines = lines.replace(" ", "%20")
		testlines2 = testlines
		testlines2 = testlines2.replace("![[", "![Image](")
		testlines3 = testlines2
		testlines3 = testlines3.replace("]]", ")")
		testlines4 = testlines3.split("(")
		testlines5 = ""
		testlines5 = fullpath + testlines4[1]
		full = ""
		full = testlines4[0] + "(" + testlines5
		#print(testlines4[1])
		print(full)

file.close()


#![[Pasted image 20221022230502.png]]
#![Image](/HTB/2023/Stocker/images/Pasted%20image%2020230224010811.png)
