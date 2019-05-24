'''
判断闰年，平年
四年一润，百年不润，四百年再润
'''
year  = int(input('请输入年份： '))
is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 ==0 ) 
print(is_leap)
