import math
r = float(input('请输入圆的半径： '))
area = math.pi * r ** 2
pm = 2 * math.pi * r
print('半径为%.2f的圆的面积为 %.2f' %(r,area))
print('半径为%.2f的圆的周长为 %.2f' %(r,pm))
