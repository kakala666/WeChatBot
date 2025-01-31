import random
import time

def monkey_sort(arr):
    cishu = 0
    # 检查数组是否已经排序
    def is_sorted(data):
        return all(data[i] <= data[i + 1] for i in range(len(data) - 1))

    # 随机交换数组中的两个元素
    def swap(data):
        i, j = random.sample(range(len(data)), 2)
        data[i], data[j] = data[j], data[i]

    while not is_sorted(arr):
        cishu += 1
        swap(arr)
    return arr, cishu

# 排序
ALL_cishu = 0
for i in range(0, 100):
    data = monkey_sort([13, 7, 0, 89, 99])
    ALL_cishu += data[1]
    time.sleep(0.1)
    print(data[1])
    # print(array)

# 计算平均次数
average_cishu = ALL_cishu / 9
print(f'平均次数: {average_cishu}')