import sys
"""这里“nester.py”模块，提供了一个名为print_list（）的函数
	用来打印列表，其中包含"""
def print_list(myList,indent=False,level=0,fn=sys.stdout):
    """这个函数有一个参数，名为"myList"，这可以是任何Python列表
    所提供的列表中的各个数据项会递归打印到屏幕上，而且各占一行。
    """
    for item in myList:
        if isinstance(item,list):
                print_list(item,indent,level+1,fn)
        else:
            if indent:
                print("\t"*level,end='',file=fn)
            print(item,file=fn)


