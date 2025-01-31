import numpy as np

def Q_rsqrt(number: float) -> float:
    if number == 0.0:
        return float('inf')  # 如果输入为0，返回无穷大

    threehalfs = 1.5
    x2 = number * 0.5
    y = number

    # 使用numpy来处理浮点数的位操作
    y = np.float32(y)  # 确保y是32位浮点数
    i = np.float32(y).view(np.int32)  # 将浮点数的内存视图转换为整数
    i = 0x5f3759df - (i >> 1)
    y = np.int32(i).view(np.float32)  # 将整数的内存视图转换回浮点数
    y = y * (threehalfs - (x2 * y * y))  # 牛顿迭代法的一次迭代

    return y.item()  # 将numpy浮点数转换回Python浮点数

# 测试代码
number = 9.0
result = Q_rsqrt(number)
print(f"The approximate inverse square root of {number} is {result}")