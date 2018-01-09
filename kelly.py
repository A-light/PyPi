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
	#for item in data:
	#	times.append(santize(item))
	times=[santize(item) for item in data]
	jsjm.append(times)
	#nester.print_list(data)
#print(jsjm)
new_jsjm=[]
#distance=[]
new_jsjm=[sorted(set(item)) for item in jsjm]
#print(distance)
print([item[0:3] for item in new_jsjm])
print(new_jsjm)
names2=["james2.txt","mikey2.txt","julie2.txt","sarah2.txt"]
jsjm2=[]
for name in names2:
	times=[]
	times=[santize(item) for item in fileTolist(name)]
	jsjm2.append(times)
print(jsjm2)
name_data={}
for item in jsjm2:
	data['Name']=item.pop(0)
	data['DOB']=item.pop(0)
	data['Times']=item
	name_data.append(data)
print(name_data)
