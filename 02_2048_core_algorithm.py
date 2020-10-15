"""
    2048游戏 核心算法
"""

list_map = [
    [2, 0, 2, 0],
    [2, 0, 0, 2],
    [4, 4, 4, 4],
    [2, 0, 4, 2]
]

list_merge = [2, 0, 2, 0]


def zero_to_end():
    """
    零元素向后移动
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


def merge():
    """
    合并
        核心思想：零元素后移，判断相邻是否相同，相同合并
    """
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)


def move_left():
    global list_merge
    for line in list_map:
        list_merge = line
        merge()


def move_right():
    global list_merge
    for line in list_map:
        list_merge = line[::-1]
        merge()
        line[::-1] = list_merge


merge()
print(list_merge)
