def division_by_three():
 import math
 print(" Проверка деления четырехзначного числа на 3")
 print("введите число")
 Number = int(input())
 x = [int(a) for a in str(Number)]
 if(Number%3==0):
    print("Число делится на 3 и сумма его чисел равняется=", sum(x))
 elif(Number%3!=0):
    print("Число не делится на 3 и произведение его чисел равняется=", math.prod(x))
