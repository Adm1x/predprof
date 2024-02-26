"""
Решение первой задачи предпроф экзамена
На вход подается csv файл с данными
нужно вывести топ 3 самых высокооплачиваемых профессии
включая компании которые их предоставляют и зарплаты

"""
from csv import reader
with open('vacancy_new.csv', encoding=utf-8) as data_file:
    #преобразуем полученный файл к списку
    vacancy=list(data_file)
    vacancy.pop(1)
    vacancy.pop(2)
    """реализуем цикл отбора для зарплат
    
    vacancy-значение находящееся в списке под определенным номером
    
    """

    for i in range(4):
        for n in range(201):
            if vacancy[n] < vacancy[n+1]:
                better_work = vacancy[n+1]
            else:
                better_work = vacancy[n]
    print(better_work)
    vacancy.pop(n)


for i in range:

    print(salary[j])
