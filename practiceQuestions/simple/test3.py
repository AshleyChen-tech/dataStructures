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


# 读取输入，输出实际费用
if __name__ == "__main__":
    N = int(input())
    print(convert_to_real_fee(N))


