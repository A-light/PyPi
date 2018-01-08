import os
import pickle
import nester
new_man=[]
path=os.getcwd()
path=path+'/HeadFirstPython/chapter3'
os.chdir(path)
print(path)
try:
	with open('man_data.txt','rb') as man_file:
		new_man=pickle.load(man_file)
except IOError as err:
	print('File error: '+str(err))
except pickle.PickleError as err:
	print('Pickling error:'+str(perr))
nester.print_list(new_man)