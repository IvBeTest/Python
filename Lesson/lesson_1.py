print("Hello, my name is Ivan.")
print("Hello,","my","name","is", "Ivan.",sep=" ")
print("Hello,","my","name","is", "Ivan.",sep=" * ")
# вывод между значениями
print("Hello,","my","name","is","Ivan", sep=" * ", end="|*|\n")
# указать что поставить вконце строки и перейти на новую
print("Hello,","my","name","is","Ivan.", sep=" ", end="\n")
print("Hello\nma\nname\nis\nIvan.\n")
# разбить на разные строки
print("Hello,","my","name","is", "Ivan.",sep="\n")
# разбить на разные строки

print(5)
print("Резyльтат:","7","15",".",sep="")
print("Резyльтат:",7,15,".", sep=" ")
# пробел вставляемая между значениями
print("Резyльтат:",7,15,".", sep="*")
print("Резyльтат:", 7, 15, sep="", end="! ")
print("Second Line") # строка добавляющаяся после последнего значения
print("Резyльтат:", 7, 15, sep="", end="!\n")
# end="!\n" выводит последний символ строки и переходит на новую
print("Second Line")
# строка выводится отдельно
print("Second \" Line")
# \" слеш позволяет вывести " как символ
print("Second \n \t \" \n Line")


print("Result:", 5 + 2)
# сумма
print("Result:", 5 - 2)
# разность
print("Result:", 5 * 2)
# произведение
print("Result:", 5 ** 2)
# возведение в степень
print("Result:", 5 ** 3)
# возведение в степень
print("Result:", 10 / 2)
# частное
print("Result:", 10 // 2)
# деление с остатком
print("Result:", 10 / 3)
# частное
print("Result:", 10 // 3)
# деление с остатком
print("Result:", min( 6, 2, 1,))
# вывести минимальное значене
print("Result:", max( 6, 2, 1,))
# вывести максимальное значение
print("Result:", pow(5, 3))
# возведение в степень
print("Result:", round(5/ 3))
# округление числа с плавающей точкой

a = 5.475
print(round(a, 2))
a = 5.477
print(round(a, 2))
a = 5.472
print(round(a, 2))
# округление числа с плавающей точкой с указанием до какой цифры округлять


# input("Введите свой возрaст: ")
# запрашивает ввод данных
number = 5
print("Result:", number)
number = 7
print("Result:", number)
# перезаписываем переменную

digit = 7.256545522
word = "Result:"
print(word, digit)

digit = 7.256545522
word = "Result:"
boolean = True
print(word, digit, True)

digit = " 7.256545522"
word = "Result:"
boolean = True
print(word + digit)
# вывод объектов одного значения
digit = -7.256545522
word = "Result: "
boolean = True
print(word + str(digit))
# приведение числа к строке
number = 10
str_num = '5'
print(number + int(str_num))
# приведение строки к числу

word = "Result: "
number = 8
str_num = '5'
print(word + str(number + int(str_num)))

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите первое число: "))
# print("Result:", num1 + num2)
# print("Result:", num1 - num2)
# print("Result:", num1 / num2)
# print("Result:", num1 * num2)

import math

yolochka_1 = 0
yolochka_1_type = type(yolochka_1)
print(yolochka_1_type)

print(type(yolochka_1), yolochka_1)

kotik_1 = " Murzik " * 4

#print(kotik_1)

i_1 = 0
i_2 = 10
I_2 = 3
i_3 = 7
i_4 = 22
i_5 = 159
sqr = 49


s_1 = i_2 + i_4
m_1 = i_2-i_3
ii = i_2 + I_2
ii = i_2 + I_2
u_1 = i_3 * i_2
d_1 = i_5 / I_2
sq = i_3 ** I_2
#dd = 4 + 10
dd = (i_3 + i_2) * i_2

print(i_3)
print('S_1 = ', s_1)
print('M_1', m_1)
print('ii = ', ii)
print('u_1 = ', u_1)
print('d_1 = ', d_1)
print('sq = ',sq, type(sq))
#print(dd)
print(dd)

mm = math.sqrt(49)
print(mm)

mm = int(math.sqrt(50))
tt = math.sqrt(50)
print(mm)
print('tt', tt, type(tt))

vv = 7.9
xx = 7
print(int(vv))
print(vv - int(vv))
print(round(vv - int(vv), 4))

#print(i_2)
#i_2 += 2
print(i_2)

#print(i_2)
#i_2 -= 2
#print(i_2)

#print(i_2)
#i_2 *= 2
#print(i_2)

#rint(i_2)
#i_2 *= 2
#i_2 = i_2 * 2
print(i_2)

print(i_2/2)

pp = math.floor(3.14)
print(pp)

pp = math.ceil(3.14)
print(pp)

pp = math.pow(2, 3)
print(pp)


i_2 = 10
if i_2:
    print("Hello i_2")

bb = True
ff = False
ii_1 = 1

#False i_1 = 0
if i_1:
    print("Hello i_1")

if ii_1:
    print("Hello ii_1")

pp = i_3 < 10
print(pp)

pp = i_3 > 10
print(pp)

pp = i_3 == 10
print(pp)

pp = i_3 != 10
print(pp)

pp = i_3 != 7
print(pp)

pp = i_3 != 7
print(pp)

pp = i_3 >= 7
print(pp)
pp = i_3 <= 7
print(pp)

pp = i_3 > 7
print(pp)

#pp = i_3 >= 7
    #print(pp)
#if pp:
    #print('Hello World')

pp = i_3 > 7
print(pp)

if pp:
    print("Hello World")
else:
    print("Python")

pp = i_3 > 7
print(pp)

if pp:
    print("Hello World")
else:
    print("Python")

pp = 99
print(pp)

if pp == 77:
    print("Hello 77")
elif pp == 99:
    print("Hello 99")
else:
    print("Hello else")

if pp >= 77:
    print("Hello >= 77")

