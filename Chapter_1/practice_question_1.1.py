# @Time     : 2020/1/17 14:22
# @Auther   : zsy
# @File     : practice_question_1.1.py

"""
假设有一个包含128个名字的有序列表，你要使用二分查找在其中查找一个名字，
请问最多需要几步才能找到？
"""
import random
import pysnooper
from faker import Faker
from comment_func import func_time


@func_time
@pysnooper.snoop()
def search_name(name_list: list, choose_name: str) -> int:
    """
    搜索名字, 最多次数
    :param name_list: 名字列表
    :param choose_name: 匹配名字
    :return: 次数, math.log2(len(name_list)) + 1 = 8 理论最多次数
    """
    count = 0
    low_index = 0
    hight_index = len(name_list) - 1
    while low_index <= hight_index:
        mid = (low_index + hight_index) // 2
        guess = name_list[mid]
        if guess == choose_name:
            return mid
        if guess > choose_name:
            hight_index = mid - 1
        else:
            low_index = mid + 1
        count += 1

    return count


if __name__ == '__main__':
    fake = Faker()
    rand_name_list = [fake.name() for x in range(128)]
    choice_name = random.choice(rand_name_list)
    search_name(rand_name_list, choice_name)
