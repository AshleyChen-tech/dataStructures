# 位运算


# 1、靠谱的车
def convert_to_real_fee(N):
    # 将输入的数字转为字符串，方便逐位处理
    str_N = str(N)
    result = 0
    factor = 1  # 从低位到高位处理时的进位因子，类比10的次方

    for i in range(len(str_N) - 1, -1, -1):
        digit = int(str_N[i])
        if digit > 4:
            # 实际费用时，跳过4，所以当前位的实际值要比它小1
            result += (digit - 1) * factor
        else:
            # 如果小于4，按正常值计算
            result += digit * factor
        # 处理下一位，进位增加10倍
        factor *= 9  # 每一位在实际费用中相当于9进制

    return result


# 读取输入，输出实际费用
if __name__ == "__main__":
    N = int(input())
    print(convert_to_real_fee(N))


