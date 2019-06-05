num = int(input("请输入任意整数："))
temp = num
num2 = 0
while temp>0:
    num2 = num2*10
    num2 = num2 + temp%10
    temp = temp//10
if num2 == num:
    print('%d 是回文数' %num)
