stu_a ={
	'name':'liwenhao',
	'age':'18'
}
stu_b = {
	'name':'zhangjiayi',
	'age':'1'
}
stu_c = {
	'name':'yuanjianbo',
	'age':'19'
}
def printStu(stu):
	for k,v in stu.items():
		print('k=%s,v=%s'%(k,v))

printStu(stu_a)
printStu(stu_b)
printStu(stu_c)



