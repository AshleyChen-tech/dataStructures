# 位运算


# 1、靠谱的车
def convert_to_real_fee(N):
    # 转换格式
    str_N = str(N)
    result = 0
    factor = 1

    for i in range(len(str_N) - 1, -1, -1):
        digit = int(str_N[i])
        if digit > 4:
            result += (digit - 1) * factor
        else:
            result += digit * factor
        factor *= 9

    return result


# 2、分苹果
def max_weight_of_apples(n, weights):
    total_weight = sum(weights)
    xor_value = 0

    # 计算所有苹果重量的 XOR 值
    for weight in weights:
        xor_value ^= weight

    # 如果 XOR 值为0，意味着可以选择所有苹果
    if xor_value == 0:
        return total_weight

    # 动态规划来找到最大重量
    dp = [False] * (total_weight + 1)
    dp[0] = True  # 0重量是可以实现的

    # 动态规划填充 dp 数组
    for weight in weights:
        for j in range(total_weight, weight - 1, -1):
            dp[j] = dp[j] or dp[j - weight]

    # 找到能满足条件的最大重量
    for w in range(total_weight, -1, -1):
        if dp[w]:
            # 计算当前总重量的 XOR 值
            remaining_xor = xor_value ^ w
            # 如果这个 XOR 值能在重量列表中找到，则返回当前重量
            if remaining_xor in weights:
                return w

    return -1  # 如果没有满足条件的重量，返回 -1


# 3、数据分类
def classify_data(data):
    # 解析输入数据
    c = data[0]
    b = data[1]
    values = data[2:]

    # 用于统计有效类型的数据数量
    type_count = {}

    for a in values:
        # 计算字节和
        byte_sum = ((a >> 24) & 0xFF) + ((a >> 16) & 0xFF) + ((a >> 8) & 0xFF) + (a & 0xFF)

        # 对 b 取模
        mod_value = byte_sum % b

        # 判断是否为有效类型
        if mod_value < c:
            if mod_value in type_count:
                type_count[mod_value] += 1
            else:
                type_count[mod_value] = 1

    # 查找数据最多的有效类型
    if type_count:
        max_count = max(type_count.values())
        return max_count
    else:
        return 0  # 如果没有有效类型，返回0


# 4、整数编码
def encode_integer_to_hex(n):
    if n < 0 or n >= (1 << 64):
        raise ValueError("Input must be a non-negative integer in the range [0, 2^64 - 1].")

    encoded_bytes = []

    while n > 0:
        # 取出低7位
        byte = n & 0x7F  # 0b01111111
        n >>= 7  # 右移7位

        # 如果后面还有字节，则设置最高位
        if len(encoded_bytes) > 0:
            byte |= 0x80  # 0b10000000，表示还有后续字节

        encoded_bytes.append(byte)

    # 处理0的特殊情况
    if not encoded_bytes:
        encoded_bytes.append(0)  # 0的编码为0x00

    # 由于是小端序，反转字节顺序
    encoded_bytes.reverse()

    # 将字节转换为16进制字符串并大写
    hex_result = ''.join(f"{byte:02X}" for byte in encoded_bytes)

    return hex_result


# 读取输入
if __name__ == "__main__":
    # N = int(input())
    # print(convert_to_real_fee(N))

    # n = 8  # 苹果数量
    # weights = [7258, 6579, 2602, 6716, 3050, 3564, 5396, 1773]  # 每个苹果的重量
    # result = max_weight_of_apples(n, weights)
    # print(result)

    # # 输入示例
    # input_data = input("请输入12个数据，用空格分隔：")
    # data = list(map(int, input_data.split()))
    #
    # # 获取结果并输出
    # result = classify_data(data)
    # print(result)

    input_number = input("请输入一个非负整数: ")
    try:
        n = int(input_number)
        result = encode_integer_to_hex(n)
        print(result)
    except ValueError as e:
        print(e)


