class HouseItem(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s]占地面积为%.2f" % (self.name, self.area)


class House(object):
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def addItem(self, item):
        print("要添加%s家具" % item.name)
        if item.area > self.free_area:
            print("%s的占地面积太大了,无法添加" % item.name)
            return
        self.item_list.append(item)
        self.free_area -= item.area

    def __str__(self):
        items_str = ", ".join(str(item) for item in self.item_list)
        return (f"户型:{self.house_type},总面积:{self.area},剩余:{self.free_area},家具:{items_str}")


c1 = HouseItem("席梦思", 4)
c2 = HouseItem("衣柜", 2)
c3 = HouseItem('餐柜', 1.5)

house = House("两室一厅", 60)
house.addItem(c1)
house.addItem(c2)
house.addItem(c3)

print(house)
