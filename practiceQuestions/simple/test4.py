# 正则表达式
import re


# 1、文本统计分析
class StatementCounter:
    def __init__(self, file_content):
        self.file_content = file_content
        self.statement_count = 0
        self.current_statement = []
        self.in_string = False
        self.escape = False
        self.string_char = ""

    def count_statements(self):
        # 用于检测空文本行
        empty_pattern = re.compile(r'^\s*$')

        # 遍历每一行内容
        for line in self.file_content.splitlines():
            i = 0
            while i < len(line):
                char = line[i]

                # 检查注释并跳过它
                if not self.in_string and not self.escape and line[i:i + 2] == "--":
                    break  # 忽略注释部分

                # 处理转义字符
                if self.escape:
                    self.current_statement.append(char)
                    self.escape = False
                elif char == "\\" and self.in_string:
                    self.escape = True
                elif char == '"' or char == "'":
                    if self.in_string:
                        if char == self.string_char:
                            # 字符串结束
                            self.in_string = False
                    else:
                        # 字符串开始
                        self.in_string = True
                        self.string_char = char
                    self.current_statement.append(char)
                elif char == ";":
                    if not self.in_string:
                        # 遇到分号表示一条语句结束
                        statement = ''.join(self.current_statement).strip()
                        if not empty_pattern.match(statement):
                            self.statement_count += 1
                        self.current_statement = []
                    else:
                        self.current_statement.append(char)
                else:
                    self.current_statement.append(char)
                i += 1

        # 处理最后一条未结束的语句
        if self.current_statement:
            statement = ''.join(self.current_statement).strip()
            if not empty_pattern.match(statement):
                self.statement_count += 1

        return self.statement_count


def get_input():
    print("输入文件内容，输入空行表示结束：")
    lines = []
    while True:
        line = input()  # 每次获取一行输入
        if not line.strip():  # 检查是否为空行，若为空行则结束输入
            break
        lines.append(line)  # 将输入的行添加到列表
    return "\n".join(lines)  # 将所有行合并为一个字符串


# 测试代码
if __name__ == "__main__":
    # file_content = '''
    # COMMAND TABLE IF EXISTS "UNITED STATE";
    # COMMAND A GREAT (
    # ID ADSAB,
    # download_length INTE-GER, -- test
    # file_name TEXT,
    # guid TEXT,
    # mime_type TEXT,
    # notificationid INTEGER,
    # original_file_name TEXT,
    # pause_reason_type INTEGER,
    # resumable_flag INTEGER,
    # start_time INTEGER,
    # state INTEGER,
    # folder TEXT,
    # path TEXT,
    # total_length INTE-GER,
    # url TEXT
    # );
    # '''
    # # 创建 StatementCounter 对象
    # counter = StatementCounter(file_content)
    #
    # # 输出统计结果
    # print(counter.count_statements())

    file_content = get_input()

    # 创建 StatementCounter 对象
    counter = StatementCounter(file_content)

    # 输出统计结果
    print(counter.count_statements())
