# sum_1 = 0
# a = 'This is a pig'
# b = []
# for i in a:
#     b.append(i)
#     if i == ' ':
#         sum_1 += 1
        
#     else:
#         pass
# print('单词的数量：',sum_1+1)
# print(b)This is a pig
# 读取输入字符串
# s = input("请输入一个字符串：")

# # 去除空格并分割单词
# words = s.strip().split()


# # 统计单词数目
# word_count = len(words)

# # 反转单词顺序
# reversed_words = words[::-1]

# # 输出结果
# print(f"原字符串中有 {word_count} 个单词。")
# print("反转后的字符串是：",''.join(reversed_words))
s = input("请输入一个字符串：")
words = s.strip().split()
word_count = len(words)
reversed_words = words[::-1]
# 使用空格重新连接单词，以确保正确的结构
reversed_str = ' '.join(reversed_words)
print(f"原字符串中有 {word_count} 个单词。")
print("反转后的字符串是：", reversed_str)
