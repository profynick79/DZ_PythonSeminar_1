#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#*Пример:*
#6 -> 1  4  1
#24 -> 4  16  4
#60 -> 10  40  10

# i = int(input("Сколько журавликов сделал Петя или Сережа?: "))
# a = i * 2 * 2 #количество журавликов, которое сделала Катя
# print("Петя, Катя и Сережа cделали из бумаги ", (i * 2 + a)," журавликов")

i = int(input("Сколько журавликов сделали Петя, Сережа и Катя всего?: "))
if (i % 6 == 0):
    a = round(i / 6) #по столько сделали Петя и Сережа
    k = round(a * 4) #столько сделала Катя
    print("Петя и Сережа сделали по", a, "журавликов; Катя сделала", k, "журавликов")
else:
    print("Не возможно вычислить целые числа")