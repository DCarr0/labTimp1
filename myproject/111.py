groupmates =[
    {
        "name": "Максим ",
        "surname": "Щипакин",
        "exams": ["Физика  ", "История ", "Мат.Анализ"],
        "marks": [3, 4, 5]
    },
    {
        "name": "Иван ",
        "surname": "Кузнецов",
        "exams": ["Физика", "История ", "Мат.Анализ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Денис ",
        "surname": "Шубин",
        "exams": ["Физика ", "История ", "Мат.Анализ"],
        "marks": [4, 5, 5]
    },
    {
        "name": "Павел",
        "surname": "Чиянов",
        "exams": ["Физика  ","История ","Мат.Анализ"],
        "marks": [4,5,5]
    },
    {
        "name": "Абуди ",
        "surname": "Абдулов",
        "exams": ["Физика  ", "История ", "Мат.Анализ"],
        "marks": [3, 4, 3]
    }
]

print("Введите среднюю оценку для студента : ")
x = input()

def print_students(students):
    print(u"имя".ljust(15), u"Фамилия".ljust(13),
    u"экзамены".ljust(38), u"оценки".ljust(20))
    for student in students:
        if sum((student["marks"]))/len((student["marks"])) >= float(x):
            print(student["name"].ljust(15), student["surname"].ljust(13), str(student["exams"]).ljust(38), str(student["marks"]).ljust(20))

print_students (groupmates)
