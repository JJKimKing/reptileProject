from collections import deque


# 数组:重复,可变列表
def _option_list():
    _my_list = ['1', 2, 'hello', 'world', 'Jane']
    _my_list.remove('1')  # 元素删除
    del _my_list[2]  # 索引删除
    del _my_list[0:1]  # 连续删除
    for e in _my_list:
        if e == 'hello':
            _my_list.remove(e)
    _my_list.clear()


# 元组:重复,不可变列表
def _option_tuple():
    my_tuple = ('1', '2', 'hello', 'world')
    for item in my_tuple:
        print(item)

    del my_tuple  # 删除元祖


# 字典
def _option_dic():
    _dic = {"a": "v1", "b": "v2", "c": "v3"}
    _value = _dic['a']
    print(_value)

    _dic['b'] = 'v4'
    _dic['d'] = 'v5'
    del _dic['a']

    for key, value in _dic.items():
        print(key, value)


# set 不可变,无序
def _option_set():
    _my_set = {1, 2, 3, 4, 5}
    _my_set.add(6)
    _my_set.remove(6)

    print(3 in _my_set)
    for item in _my_set:
        print(item)


# 队列
def _option_deque():
    _my_deque = deque([1, 2, 3, 4, 5])
    _my_deque.append(6)
    for item in _my_deque:
        print(item)

_option_deque()
