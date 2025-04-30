import heapq
from typing import List

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodRateMap = {}  # 记录食物评分
        self.foodCuisineMap = {}  # 记录食物对应的菜系
        self.cuisineHeap = {}  # 记录每种菜系的最大堆

        for i in range(len(foods)):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]
            self.foodRateMap[food] = rating
            self.foodCuisineMap[food] = cuisine
            if cuisine not in self.cuisineHeap:
                self.cuisineHeap[cuisine] = []
            heapq.heappush(self.cuisineHeap[cuisine], (-rating, food))  # 负数表示最大堆

    def changeRating(self, food: str, newRating: int) -> None:
        """修改某个食物的评分"""
        cuisine = self.foodCuisineMap[food]
        self.foodRateMap[food] = newRating
        heapq.heappush(self.cuisineHeap[cuisine], (-newRating, food))  # 更新堆

    def highestRated(self, cuisine: str) -> str:
        """查询评分最高的食物，字典序优先"""
        while self.cuisineHeap[cuisine]:
            rating, food = self.cuisineHeap[cuisine][0]  # 获取堆顶元素
            if self.foodRateMap[food] == -rating:
                return food
            heapq.heappop(self.cuisineHeap[cuisine])  # 评分不匹配，移除无效项

if __name__ == '__main__':
    foodRatings = FoodRatings(
        ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
        ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
        [9, 12, 8, 15, 14, 7]
    )
    res = []
    case1 = ["korean","japanese","japanese","japanese"]
    case2 = ["kimchi","ramen","sushi","ramen"]
    res.append(foodRatings.highestRated(case1[0]))
    res.append(foodRatings.highestRated(case1[1]))
    foodRatings.changeRating("sushi",16)
    res.append(foodRatings.highestRated(case1[2]))
    foodRatings.changeRating("ramen",16)
    res.append(foodRatings.highestRated(case1[3]))

    print(f'input: {case1},\n expect: {case2}')
    print(res)
    print('\n')

    foodRatings = FoodRatings(
        ["xxdcg","wfqdeytt","jqmfm","ukqbjikyx","aymciznrnw","qhjjrvr","wzcinxg","ikxj"],
        ["lruhtqy","lruhtqy","lruhtqy","lruhtqy","lruhtqy","lruhtqy","lruhtqy","lruhtqy"],
        [8,6,1,17,20,2,17,14]
    )
    res.clear()
    res.append(foodRatings.highestRated("lruhtqy"))
    foodRatings.changeRating("wfqdeytt",17)
    foodRatings.changeRating("aymciznrnw",9)
    res.append(foodRatings.highestRated("lruhtqy"))
    foodRatings.changeRating("ukqbjikyx",10)
    res.append(foodRatings.highestRated("lruhtqy"))
    foodRatings.changeRating("xxdcg",11)
    foodRatings.changeRating("ikxj",15)
    foodRatings.changeRating("aymciznrnw",10)
    foodRatings.changeRating("wfqdeytt",10)
    foodRatings.changeRating("xxdcg",16)
    foodRatings.changeRating("ikxj",2)
    foodRatings.changeRating("aymciznrnw",16)
    res.append(foodRatings.highestRated("lruhtqy"))
    foodRatings.changeRating("wzcinxg",12)
    res.append(foodRatings.highestRated("lruhtqy"))
    case1 = ["lruhtqy","lruhtqy","lruhtqy","lruhtqy","lruhtqy"]
    case2 = ["aymciznrnw","ukqbjikyx","wfqdeytt","wzcinxg","aymciznrnw"]
    print(f'input: {case1},\n expect: {case2}')
    print(res)


