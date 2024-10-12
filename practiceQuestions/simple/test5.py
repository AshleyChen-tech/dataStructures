# 字符串、数组、集合
import re
import sys

# 1、敏感字段加密
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


# 2、TLV解码
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


# 3、字符串分割
def process_string(K, S):
    parts = S.split('-')
    result = [parts[0]]
    remaining = ''.join(parts[1:])
    grouped = [remaining[i: i+K] for i in range(0, len(remaining), K)]
    for group in grouped:
        lower_count = sum(1 for c in group if c.islower())
        upper_count = sum(1 for c in group if c.isupper())

        if lower_count > upper_count:
            result.append(group.lower())
        elif lower_count < upper_count:
            result.append(group.upper())
        else:
            result.append(group)
    return '-'.join(result)


# 4、英文输入法
def suggest_words(sentence, prefix):
    words = re.findall(r"[A-Za-z]+", sentence)
    unique_words = sorted(set(words))
    matched_words = [word for word in unique_words if word.startswith(prefix)]
    if matched_words:
        return ' '.join(matched_words)
    else:
        return prefix


# 5、连续字母长度
def find_kth_longest_substring(s, k):
    max_len_dict = {}
    cur_char = s[0]
    cur_length = 1

    for i in range(1, len(s)):
        if s[i] == cur_char:
            cur_length += 1
        else:
            if cur_char in max_len_dict:
                max_len_dict[cur_char] = max(max_len_dict[cur_char], cur_length)
            else:
                max_len_dict[cur_char] = cur_length
            cur_char = s[i]
            cur_length = 1

    if cur_char in max_len_dict:
        max_len_dict[cur_char] = max(max_len_dict[cur_char], cur_length)
    else:
        max_len_dict[cur_char] = cur_length

    lengths = sorted(max_len_dict.values(), reverse=True)
    if k > len(lengths):
        return lengths[-1]
    else:
        return lengths[k-1]


# 6、字符串变换最小字符串
def smallest_string_after_swap(s):
    s_list = list(s)
    n = len(s_list)
    for i in range(n):
        min_char_index = i
        for j in range(i+1, n):
            if s_list[j] < s_list[min_char_index]:
                min_char_index = j
        if min_char_index != i:
            s_list[i], s_list[min_char_index] = s_list[min_char_index], s_list[i]
            return ''.join(s_list)
    return s


# 7、响应报文时间
def getMaxResponseTime(messages):
    ans = sys.maxsize

    for t, m in messages:
        if m >= 128:
            bStr = bin(m)[2:]
            exp = int(bStr[1:4], 2)
            mant = int(bStr[4:], 2)
            respTime = t + (mant | 16) << (exp + 3)
        else:
            respTime = t + m
        ans = min(ans, respTime)
    return ans


# # 8、数组拼接
# subLen = int(input())
# n = int(input())
#
# lists = [list(filter(lambda x: x != "", input().split(","))) for _ in range(n)]
#
#
# def getResult():
#     ans = []
#     while any(lists):
#         for i in range(len(lists)):
#             if lists[i]:
#                 tmp = lists[i][:subLen]
#                 del lists[i][:subLen]
#                 ans.extend(tmp)
#     return ",".join(ans)
#
# print(getResult())


# 9、猜字谜
# issues = input().split(",")
# answers = input().split(",")
#
# def solution():
#     ans = []
#     for issue in issues:
#         s1 = "".join(sorted(set(issue)))
#         isNotFind = True
#
#         for answer in answers:
#             s2 = "".join(sorted(set(answer)))
#             if s1 == s2:
#                 isNotFind = False
#
#         if isNotFind:
#             ans.append("not found")
#     return ','.join(ans)
# print(solution())

# # 输入获取
# mianmi = input().split(",")
# midiku = input().split(",")
#
#
# # 判断单词是否匹配的函数
# def is_match(mianmi_word, midi_word):
#     # 第一种匹配方式：字母排序后相同
#     if sorted(mianmi_word) == sorted(midi_word):
#         return True
#     # 第二种匹配方式：去重后的字母集合相同
#     if sorted(set(mianmi_word)) == sorted(set(midi_word)):
#         return True
#     return False
#
#
# # 算法入口
# def solution():
#     ans = []
#
#     # 遍历谜面单词
#     for word in mianmi:
#         found = False
#
#         # 遍历谜底库，寻找匹配单词
#         for midi_word in midiku:
#             if is_match(word, midi_word):
#                 ans.append(midi_word)
#                 found = True
#                 break
#
#         if not found:
#             ans.append("not found")
#
#     # 返回结果列表，以逗号分隔
#     return ",".join(ans)
#
#
# # 输出结果
# print(solution())


# # 10、单词接龙
# k = int(input())
# n = int(input())
# words = [input() for _ in range(n)]
#
# def solution():
#     chain = [words.pop()]
#     prefix = {}
#     for word in words:
#         w = word[0]
#         if prefix.get(w) is None:
#             prefix[w] = []
#         prefix[w].append(word)
#     for w in prefix.keys():
#         prefix[w].sort(key=lambda x: (-len(x), x))
#     while True:
#         tail = chain[-1][-1]
#         if tail not in prefix or len(prefix[tail]) == 0:
#             break
#         chain.append(prefix[tail].pop(0))
#     return "".join(chain)
#
# print(solution())


# 11、字符统计及重排
def count_letters(s):
    letter_count = {}
    for ch in s:
        if ch in letter_count:
            letter_count[ch] += 1
        else:
            letter_count[ch] = 1

    sorted_letters = sorted(letter_count.items(), key=lambda x: (-x[1], x[0]))
    result = ";".join([f"{ch}:{count}" for ch, count in sorted_letters]) + ";"
    return result


if __name__ == '__main__':
    # # 1、读取输入
    # k = int(input().strip())  # 命令字索引
    # s = input().strip()  # 命令字符串
    #
    # # 输出处理结果
    # print(process_command(k, s))

    # # 2、输入处理
    # target_tag = input().strip()  # 目标Tag
    # hex_stream = input().strip()  # 16进制码流
    #
    # # 输出结果
    # result = parse_tlv(target_tag, hex_stream)
    # print(result)

    # # 3、输入读取
    # K = int(input())  # 读取正整数 K
    # S = input()  # 读取字符串 S
    #
    # # 输出处理后的字符串
    # print(process_string(K, S))

    # # 4、输入读取
    # sentence = input().strip()  # 输入的第一行，含有英文单词和标点
    # prefix = input().strip()  # 输入的第二行，前缀
    #
    # # 输出联想结果
    # print(suggest_words(sentence, prefix))

    # # 5、输入读取
    # s = input().strip()  # 读取字符串
    # k = int(input().strip())  # 读取k值
    #
    # # 输出第k长的子串长度
    # print(find_kth_longest_substring(s, k))

    # # 6、输入处理
    # s = input().strip()
    # # 输出结果
    # print(smallest_string_after_swap(s))

    # # 7、输入获取
    # c = int(input())
    # message = [list(map(int, input().split())) for _ in range(c)]
    # print(getMaxResponseTime(message))

    # 11、输入
    input_str = input()
    print(count_letters(input_str))





