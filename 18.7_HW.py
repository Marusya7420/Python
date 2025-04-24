import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Добавить ученика
        5. Вывести все оценки ученика по предметам
        6. Исправить (редактировать) оценку ученика по предмету
        7. Удалить ученика 
        8. Добавить предмет
        9. Удалить предмет
        10. Вывести средний балл оценок по всем предметам ученика
        11. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('Добавить ученика')
        student = input('Введите имя ученика: ')
        if student not in students_marks.keys():
            students.append(student)
            students_marks[student] = {}
            for class_ in classes:
                students_marks[student][class_] = []
            print(f'Ученик добавлен: {student}: {students_marks[student]}')
            print()
            print(f'Обновленные данные:')
            for student in students:
                print(f'{student}:')
                for class_ in classes:
                    print(f'{class_} - {students_marks[student][class_]}')
        else:
            print('Такой ученик уже есть')
    elif command == 5:
        print('Вывести все оценки ученика по всем предметам')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            print(f'{student}: {students_marks[student]}')
        else:
            print('Такого ученика нет в списке')
    elif command == 6:
        print('Исправить (редактировать) оценку ученика по предмету')
        student = input('Введити имя ученика: ')
        class_ = input('Введите предмет по которому надо исправить оценку: ')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            print(f'{class_} - {students_marks[student][class_]}')
            i = int(input('Введите порядковый номер оценки для исправления (редактирования): '))
            students_marks[student][class_].pop(i - 1)
            mark = int(input('Введите исправленную (отредактированную) оценку: '))
            students_marks[student][class_].insert(i - 1, mark)
            print(f'Исправленные (отредактированные) оценки: {student}: {class_} - {students_marks[student][class_]}')
        else:
            print('Ошибка: неверно введено имя ученика или название предмета')
    elif command == 7:
        print('Удалить ученика')
        student = input('Введите имя ученика, которого нужно удалить: ')
        if student in students_marks.keys():
            del students_marks[student]
            print('Ученик удален')
            print(f'Отредактированные данные: {students_marks}')
        else:
            print('Такого ученика нет в списке')
    elif command == 8:
        print('Добавить предмет')
        class_ = input('Введите название предмета, который надо добавить: ')
        if class_ not in classes:
            classes.append(class_)
            for student in students:
                for class_ in classes:
                    students_marks[student][class_] = []
            print(f'{class_} - Предмет добавлен')
            print(students_marks)
        else:
            print('Такой предмет уже есть в списке')
    elif command == 9:
        print('Удалить предмет')
        print(f'{students_marks[student].keys()}')
        class_ = input('Введите предмет, который нужно удалить: ')
        if class_ in students_marks[student].keys():
            for student in students:
                del students_marks[student][class_]
            print('Предмет удален')
            print(f'Отредактированные данные: {students_marks}')
        else:
            print('Такого предмета нет в списке')

    elif command == 10:
        print('Вывести средний балл оценок по всем предметам ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_}- {marks_sum / marks_count} ')
        else:
            print('Такого ученика в списке нет')
    elif command == 11:
        print('11. Выход из программы')
        break