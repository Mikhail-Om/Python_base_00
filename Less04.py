# Практическое задание к четвертой лекции
#
#
#Задание 1
#
# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. 
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия. 
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.


def calc_money(H,R,B):
    pay = H * R + B
    return pay
print("Нужно заплатить ", calc_money(int(input("Часы работы ")),int(input("Ставка ")),int(input("Бонусы "))))

    #Задание 2
#
# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
f_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
s_list = [f_list[i] for i in range(1, len(f_list)) if f_list[i] > f_list[i-1] ]

print(f"Исходный список: {f_list}")
print(f"Новый список:  {s_list}")

#Задание 3
#
# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
# Подсказка: используйте функцию range() и генератор.

N_list = [print(el) for el in range(1, 241) if el % 20 == 0 or el % 21 == 0 ]  # Это получилось в одну строку

####

N_list = (el for el in range(1, 241) if el % 20 == 0 or el % 21 == 0) # - это всё -таки в 2
list(N_list)

#Задание 4
#
# Представлен список чисел. Определите элементы списка, не имеющие повторений. 
# Сформируйте итоговый массив чисел, соответствующих требованию. 
# Элементы выведите в порядке их следования в исходном списке. 
# Для выполнения задания обязательно используйте генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

import collections
f_list =[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
s_list =[i for i, count in collections.Counter(f_list).items() if count == 1]
print(s_list)

#Задание 5
#
# Реализовать формирование списка, используя функцию range() и возможности генератора. 
# В список должны войти чётные числа от 100 до 1000 (включая границы). 
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce
list_f = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(lambda x ,y : x * y, list_f))

#Задание 6
#
# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools. 
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
# Предусмотрите условие его завершения. 
# Например, в первом задании выводим целые числа, начиная с 3. 
# При достижении числа 10 — завершаем цикл. 
# Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

from itertools import count, cycle
def iterator_f(strt,stp):
    for el in count(strt):
        if el > stp:
            break
        else:
            yield el
iterator_f = iterator_f(3, 10)

for i in iterator_f:
    print(i)
    

def iterator_s(lst,stp):
    c = 0
    for el in cycle(lst):
        if c > stp:
            break
        yield el
        c += 1
iterator_s = iterator_s([1,2],10)
for i in iterator_s:
    print(i)