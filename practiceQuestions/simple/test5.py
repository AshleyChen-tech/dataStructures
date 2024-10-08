# 字符串、数组、集合


def process_command(k, s):
    commands = []  # 存放解析后的命令字
    current_command = []  # 存放当前解析的命令字
    in_quotes = False  # 标记是否在双引号内
    i = 0

    while i < len(s):
        if s[i] == '"':  # 遇到双引号，切换状态
            in_quotes = not in_quotes
            i += 1
            continue

        if s[i] == '_':
            if in_quotes:  # 双引号内的下划线视为命令字的一部分
                current_command.append('_')
            else:
                if current_command:  # 当前有内容，则将其作为命令字添加
                    commands.append(''.join(current_command))
                    current_command = []
            i += 1
        else:
            current_command.append(s[i])
            i += 1

    # 最后一个命令字添加进commands
    if current_command or in_quotes:  # 确保结束后命令字加入
        commands.append(''.join(current_command))

    # 如果索引超出范围，返回错误
    if k >= len(commands):
        return "ERROR"

    # 替换指定索引的命令字为******
    commands[k] = "******"

    # 用下划线连接，去除多余的下划线
    result = "_".join(commands)

    return result


# TLV解码
def parse_tlv(target_tag, hex_stream):
    # 将输入的16进制码流拆分为单个字节
    stream = hex_stream.split()

    i = 0  # 指针从第一个字节开始解析
    while i < len(stream):
        # 读取Tag
        tag = stream[i]
        i += 1

        # 读取Length，两个字节，小端序
        if i + 1 >= len(stream):  # 防止越界
            break
        length = int(stream[i + 1] + stream[i], 16)  # 小端序存储
        i += 2

        # 读取Value
        if i + length > len(stream):  # 防止越界
            break
        value = ' '.join(stream[i:i + length])
        i += length

        # 如果Tag匹配，则输出对应的Value
        if tag == target_tag:
            return value

    return ""  # 未找到匹配的Tag


if __name__ == '__main__':
    # # 读取输入
    # k = int(input().strip())  # 命令字索引
    # s = input().strip()  # 命令字符串
    #
    # # 输出处理结果
    # print(process_command(k, s))

    # 输入处理
    target_tag = input().strip()  # 目标Tag
    hex_stream = input().strip()  # 16进制码流

    # 输出结果
    result = parse_tlv(target_tag, hex_stream)
    print(result)
