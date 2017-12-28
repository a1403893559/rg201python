# 先判断 是男是女   如果是男  那就是高富帅  如果是女  那就是白富美
sex = input("你是男的还是女的还是其他")
if sex == '男':
    height = input('你高吗')
    money = input('你富吗')
    handsome = input('你帅吗')
    if height != '矮' and money != '穷' and handsome != '挫':
        print('高帅富')
    else:
        print('矮穷矬')
elif sex == '女':
    color = input('你白')
    money = input('你富吗')
    beautiful = input('你美吗')
    if color == '白' or money == '富' or beautiful == '美':
        print('白富美')
else:
    die = input('死还是活')
    if not die == '活':
        print('死人妖')
    else:
        print('活人妖')
