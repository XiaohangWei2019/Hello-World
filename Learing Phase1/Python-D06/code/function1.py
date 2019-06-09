def is_palindrome(num)：
  temp = num
  num2 = 0
  while temp>0:
    num2 *= 10
    num2 += temp%10
    temp = temp//10
  if num2 == num:
    print("is_")
    return Ture
  else:
    return False
