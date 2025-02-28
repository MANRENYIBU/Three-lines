# 题目来源：https://leetcode.cn/problems/design-a-food-rating-system/description/

# 方法一：有序集合

'''
用一个哈希表 foodMap 记录每个食物名称对应的食物评分和烹饪方式，同时一个哈希表套有序集合 cuisineMap 记录每个烹饪方式对应的食物评分和食物名字
changeRating: 先从 cuisineMap 中删掉旧数据，然后将 newRating 和 food 记录到 cuisineMap 和 foodMap 中
highestRated: 从有序集合 cuisineMap[cuisine] 中找到最优数据
'''

from typing import List
from sortedcontainers import SortedList
from collections import defaultdict

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_map = {}
        self.cuisine_map = defaultdict(SortedList)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_map[food] = [rating, cuisine]
            # 取负号，保证 rating 相同时，字典序更小的 food 排在前面
            self.cuisine_map[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        rating, cuisine = self.food_map[food]
        sl = self.cuisine_map[cuisine]
        sl.discard((-rating, food))
        sl.add((-newRating, food))
        self.food_map[food][0] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_map[cuisine][0][1]
