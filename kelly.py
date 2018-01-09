import os
import nester
path=os.getcwd()
path=path+'/HeadFirstPython/chapter5/hfpy_ch5_data'
os.chdir(path)
james=[]
sarah=[]
julie=[]
mikey=[]
def fileTolist(file):
	listName=[]
	try:
		with open(file) as data:
			for line in data:
				temp=line.split(',')
				for list_item in temp:
					listName.append(list_item.strip())
	except IOError as err:
		print("File is missing",str(err))
	return listName
names=["james.txt","mikey.txt","julie.txt","sarah.txt"]
for names_item in names:
	print(names_item)
	data=fileTolist(names_item)
	nester.print_list(data)

			



