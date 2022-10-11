import Min_three_num
import Roots_equation
import Division_by_three
import Three_digit_number
import Remainder_division
import Mini_Calculator

MenuMin_three_num = '1'
MenuRoots_equation = '2'
MenuDivision_by_three = '3'
MenuThree_digit_number = '4'
MenuRemainder_division = '5'
MenuMini_Calculator = '6'

print(
'''
Меню:
1. Выведение минимума из трех введенных чисел
2. Определение наличия корней у уравнения
3. Действия с четырехзначным числом
4. Определение трехзначного числа
5. Проверка на остаток при делении 
6. Мини калькулятор
(Наберите номер пункта и нажмите <ENTER>)
'''
)

menu_value = input()
if      menu_value == MenuMin_three_num:
    Min_three_num.min_three_num()
elif    menu_value == MenuRoots_equation:
    Roots_equation.roots_equation()
elif    menu_value == MenuDivision_by_three:
    Division_by_three.division_by_three()
elif    menu_value == MenuThree_digit_number:
    Three_digit_number.three_digit_number()
elif    menu_value == MenuRemainder_division:
    Remainder_division.remainder_division()
elif    menu_value == MenuMini_Calculator:
    Mini_Calculator.mini_Calculator()
else:    
    print("Неверные данные!")

input("Нажмите <ENTER> для выхода")
