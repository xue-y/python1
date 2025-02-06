a = '123456789988654321'
b = int((len(a)/2))
j = 0
for i in range(b):
    j = -1-i
    if a[i] != a[j]:
        print('不是回文数，在第%d个数字时不相等'%(i+1))
        break
    else:
        pass