"""这里“nester.py”模块，提供了一个名为print_list（）的函数
	用来打印列表，其中包含"""
def print_list(myList,level=0):
    """这个函数有一个参数，名为"myList"，这可以是任何Python列表
    所提供的列表中的各个数据项会递归打印到屏幕上，而且各占一行。
    """
    for item in myList:
        if isinstance(item,list):
                print_list(item,level+1)
        else:
                for tab_stop in range(level):
                        print("\t",end="")
                print(item)
