a = int(input("Введіть ціле число a: "))
b = float(input("Введіть дробове число b: "))
c = int(input("Введіть ціле число c: "))
d = float(input("Введіть дробове число d: "))
print("Ціле число a:", a)
print("Дробове число b:", b)
print("Ціле число c:", c)
print("Дробове число d:", d)
suma = a + b
riznica = a - b
dobut = a * b
dilenne = a / b
stepen = a ** b
cilisne_dil = a // b
ostacha = a % b
print("Сума:", suma)
print("Різниця:", riznica)
print("Добуток:", dobut)
print("Ділення:", dilenne)
print("Степінь:", stepen)
print("Цілочисленне ділення:", cilisne_dil)
print("Остача від ділення:", ostacha)
a = int(input("Введіть ціле число a: "))
b = float(input("Введіть дробове число b: "))
c = int(input("Введіть ціле число c: "))
d = float(input("Введіть дробове число d: "))
my_list = [a, b, c, d]
кількість_елементів = len(my_list)
print("Кількість елементів у списку:", кількість_елементів)
print("Парні елементи списку:")
for i in range(кількість_елементів):
    if i % 2 == 1:
        print(my_list[i])
a = int(input("Введіть ціле число a: "))
b = float(input("Введіть дробове число b: "))
c = int(input("Введіть ціле число c: "))
d = float(input("Введіть дробове число d: "))
my_list = [a, b, c, d]
my_list[1], my_list[3] = my_list[3], my_list[1]
print("Список з переставленими елементами:", my_list)
name = input("Введіть ваше прізвище та ім'я: ")
print("Виконавець лабораторної роботи:", name)
print("Висновки:")
print("В ході виконання даної лабораторної роботи я ознайомився з основами роботи зі списками в Python.")
print("Я навчився створювати списки, отримувати доступ до елементів списку, змінювати їх порядок та виводити їх на екран.")