def print_list(myList):
	for item in myList:
		if isinstance(item,list):
			print_list(item)
		else:
			print(item)
