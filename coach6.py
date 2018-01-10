import os
import nester
path=os.getcwd()
path=path+'/HeadFirstPython/chapter5/hfpy_ch5_data'
os.chdir(path)
def sanitize(time_string):
	if time_string.find('-')!=-1:
		splitter='-'
	elif time_string.find(':')!=-1:
		splitter=':'
	else: 
		return time_string
	(mins,secs)=time_string.split(splitter)
	return (mins+'.'+secs)
def get_coach_data(filename):
	try:
		with open(filename) as f:
			data =f.readline()
		temp1=data.strip().split(',')
		return(AthleteList(temp1.pop(0),temp1.pop(0),temp1))
	except IOError as err:
		print('File error: '+str(err))
		return(None)

class AthleteList(list):
	def __init__(self,a_name,a_dob=None,a_times=[]):
		list.__init__([])
		self.name=a_name
		self.dob=a_dob
		self.extend(a_times)
	def top3(self):
		return(sorted(set([sanitize(t) for t in self]))[0:3])
names2=["james2.txt","mikey2.txt","julie2.txt","sarah2.txt"]
#jjms=AthleteList()
jjms=[get_coach_data(name) for name in names2]
for it in jjms:
	print(it.name+it.dob+str(it.top3()))