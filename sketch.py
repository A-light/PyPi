import os
path=os.getcwd()
path=path+"/HeadFirstPython/chapter3"
os.chdir(path)
man=[]
other=[]
try:
	with open('sketch.txt') as data:
		for line in data:
			try:
				(role,line_spoken)=line.split(':',1)
				line_spoken=line_spoken.strip()
				if role=='Man':
					man.append(line_spoken)
				elif role=='Other Man':
					other.append(line_spoken)
			except ValueError as err:
				pass
except IOError:
	print('The data file is missing')
try:
	with open("man_data.out",'w') as man_data,open("other_data.out",'w') as other_data:
		print(man,file=man_data)
		print(other,file=other_data)
except IOError as err:
	pirnt("The out file is missing"+str(err))
print(man)
print(other)