import sys
import os

filename = sys.argv[1]

with open(filename, "r+") as file:
	data = file.readlines()
	


dir_path = os.path.realpath(filename)
split_dir_path = dir_path.split("\\")
print(split_dir_path)
fullpath = ""

for i in range(3, len(split_dir_path) - 1, 1):
	fullpath = "/".join([fullpath, split_dir_path[i]])

fullpath = "".join([fullpath, "/images/"])
print(fullpath)	


for i in range(0, len(data), 1):
	if data[i].startswith("![[") == True:
		tmp = data[i].replace(" ", "%20")
		tmp = tmp.replace("![[", "![Image](")
		tmp = tmp.replace("]]", ")")
		tmpSplit = tmp.split("(")
		fullPathTemp = ""
		fullPathTemp = tmpSplit[0] + "(" + fullpath + tmpSplit[1]
		data[i] = fullPathTemp

with open(filename, "w") as fileOpen:
	fileOpen.writelines(data)





file.close()


#![[Pasted image 20221022230502.png]]
#![Image](/HTB/2023/Stocker/images/Pasted%20image%2020230224010811.png)
