"""
Study only 
From Author: 骆昊
输出斐波那契数列的前num个数
1 1 2 3 5 8 13 21 ...
"""

a= 0
b = 1
num = int(input()) 
for _ in range(num):
  (a, b) = (b, a+b)
  print(a, end =' ')
