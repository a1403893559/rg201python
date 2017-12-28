# 创建一个字符 字符串是python 基本的数据类型之一 可以用''或者""括起来 我们需要掌握什么? 对字符串的基本增删改查的操作
#1、作业 创建一个字符串 
pstr = '人生苦短,我用python,life is short,you need python'
print('该字符串的内容是%s'%pstr)
#第一个小问题是 统计字符串里面 p的个数和i的个数
# count函数 count() 统计字符串字符出现的个数
p_counts = pstr.count('p')
i_counts = pstr.count('i')
print('该字符串里面P的个数%s'%p_counts)
print('该字符串里面i的个数%s'%i_counts)

# 反向查找S所在的为止
s_find = pstr.rfind('s')
print('s在字符串的%d位'%s_find)
# 将所有小写单词换成 大写
pstr = pstr.upper()
print('小写转换成大写单词%s--成功'%pstr)
# 将所有的大写换成小写
pstr = pstr.lower()
print('大写换成小写单词了%s--成功'%pstr)
# 切片，从字符串里面剪切一个片段出来 （火腿肠，切一小段火腿肠，就可以理解为切片）
# 切片  你要切片的对象 [开始的为止:结束的为止]
# 从头切刀未
newstr = pstr[7:]
print('新的字符串内容为%s'%newstr)
