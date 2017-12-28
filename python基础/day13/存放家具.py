class Home:
    def __init__(self, area):
        # 家的面积
        self.area = area
        # 包含的家具
        self.containsItem = []

    def __str__(self):
        msg = '当前房间的可用面积是:' + str(self.area)
        return msg

    def accommodateItem(self, item):
        # 如果可用面积大于物品的占用面积
        needArea = item.getUsedArea()
        if self.area > needArea:
            self.containsItem.append(item)
            self.area -= needArea
            print('ok:已经放到房间中了')
        else:
            print('err:房间可用面积%d，但是当前需要存放的物品面积为%d' % (self.area, needArea))


class Bed:
    def __init__(self, area, name='床'):
        # 床的名字
        self.name = name
        # 床的占地面积
        self.area = area

    def __str__(self):
        msg = '家具的名字是:' + self.name + ','
        msg = msg + '面积为：' + str(self.area)
        return msg

    def getName(self):
        return self.name

    def getUsedArea(self):
        return self.area



# 创建一个新家对象
newHome = Home(100)
print(newHome)

# 创建一个床
newBed = Bed(20)
print(newBed)

newHome.accommodateItem(newBed)


newBed2 = Bed(1000)
print(newBed2)

newHome.accommodateItem(newBed2)
