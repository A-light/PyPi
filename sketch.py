import os
path=os.getcwd()
path=path+"/HeadFirstPython/chapter3"
try:
	data=open('sketch.txt')
	for line in data:
		try:
			(role,line_spoken)=line.split(':',1)
			print(role,end='')
			print(' said:',end='')
			print(line_spoken,end='')
		except ValueError:
			pass
	data.close()
except IOError:
	print('The data file is missing')

