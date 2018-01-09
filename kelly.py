import os
import nester
path=os.getcwd()
path=path+'/HeadFirstPython/chapter5/hfpy_ch5_data'
os.chdir(path)
james=[]
sarah=[]
julie=[]
mikey=[]
jsjm=[]
def fileTolist(file):
	listName=[]
	try:
		with open(file) as data:
			for line in data:
				listName=line.strip().split(',')
	except IOError as err:
		print("File is missing",str(err))
	return listName

def santize(time_string):
	if time_string.find('-')!=-1:
		splitter='-'
	elif time_string.find(':')!=-1:
		splitter=':'
	else: 
		return time_string
	(mins,secs)=time_string.split(splitter)
	return (mins+'.'+secs)

names=["james.txt","mikey.txt","julie.txt","sarah.txt"]
for names_item in names:
	print(names_item)
	times=[]
	data=fileTolist(names_item)
	for item in data:
		times.append(santize(item))
	jsjm.append(times)
	#nester.print_list(data)
print(jsjm)

			



