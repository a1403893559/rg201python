'''
常见的字符串操作
假设有一个字符串为 Life is short ,you need Python
'''

oldstr = 'Life is short,you need Python'#假设母串（你也可以理解为原始字符串）
# 用法一：find 检测newstr是否包含在oldstr中，如果是返回开始的索引值，否则返回-1
# 语法格式为：oldstr.find(str,start=0,end=len(oldstr)
# 查询short在母串中的索引值 len()函数返回的值是长度，即字符串的长度
newstr1 = oldstr.find('short',0,len(oldstr))
# 输出的新串的内容（我们事先已经知道了，返回的是一个索引值）
print('查询short在母串中的索引值,结果为%d位'%newstr1)
# 查询short在母串中的索引值 len()表示长度 从第0位开始
newstr2 = oldstr.find('wengwenyu',0,len(oldstr))
print("返回值位-1，表示当前的子串在母串中找不到,当前的值位:%d"%newstr2)


