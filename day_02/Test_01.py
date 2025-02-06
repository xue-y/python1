a = input('请输入一句话')
words = a.strip().split()
reverse_words = words[::-1]
num_1 = len(words)
print('单词的数量为：%.2f' % num_1)
print('逆序为：'," ".join(reverse_words))