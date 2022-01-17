# 1) Создать переменную типа String

name = n = "Ivan"
# print(n)
#
# 2) Создать переменную типа Integer

age = a = 32
# print(a)

# 3) Создать переменную типа Float

my_weight = m = 79.6
# print(m)

# 4) Создать переменную типа Bytes

z = bytes(8)
# print(z)

# 5) Создать переменную типа List

x = ["Nikolai","Ivan","Oleg","Alex", "age","weight",[18, 25, 36.6, 32,79.6]]
# print(x[1])
# print(x[4])
# print(x[6][3])

# 6) Создать переменную типа Tuple

e = ("Nikolai","Ivan","Oleg","Alex", "age","weight",[18, 25, 36.6, 32, 79.6])
# print(e[1])
# print(e[5])
# print(e[6][4])

# 7) Создать переменную типа Set

# q = set("Hello help")
# print(q)

f = {3, 6, 8, 3, "h", "r", "u", 8, "h"}
# print(f)

# 8. Создать переменную типа Frozen set

p = frozenset([3, 6, 8, 7, 9, 10, 758, 10, 15, 36.6, 3, "h", "r", "u", 8, "h"])
# print(p)

# 9) Создать переменную типа Dict

d = dict({"name": "Nikolai", "age": 25, "profession": "QA engenier"})
# print(d["name"])

# dd = {"name": "Nikolai", "age": 25, "profession": "QA engenier"}
# print(dd["age"])

# ddd = dict(Name="Nikolai", age= 25, profession= "QA engenier")
# print(ddd['Name'])

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.

print("n:", type(n), n)
print("a:", type(a), a)
print("m:", type(m), m)
print("z:", type(z), z)
print("x:", type(x), x)
print("e:", type(e), e)
print("f:", type(f), f)
print("p:", type(p), p)
print("d:", type(d), d)

# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.

N = "PADA"
S = "WANS"
P=(N+S)
print(P)

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)

g = "Group"
f = 26
print(g, f)

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)

j = "Python lesson "
i = 1
print(j + str(i))
