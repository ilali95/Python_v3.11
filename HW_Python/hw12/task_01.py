# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.


import csv


class NameValidator:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if not isinstance(value, str) or not value.isalpha() or not value.istitle():
            raise ValueError("ФИО должно содержать только буквы и начинаться с заглавной буквы.")
        self.name = value

class SubjectValidator:
    def __init__(self, valid_subjects):
        self.valid_subjects = valid_subjects
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if value not in self.valid_subjects:
            raise ValueError(f"Предмет '{value}' не допускается.")
        self.name = value

class Student:
    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = self.load_subjects(subjects_file)
        self.grades = {subject: {'grades': [], 'test_results': []} for subject in self.subjects}
    
    def load_subjects(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            subjects = next(reader)
            return subjects
    
    def add_grade(self, subject, grade):
        self.subject_validator = subject
        if grade not in [2, 3, 4, 5]:
            raise ValueError("Оценка должна быть от 2 до 5.")
        
        if subject not in self.grades:
            self.grades[subject] = {'grades': [], 'test_results': []}
        
        self.grades[subject]['grades'].append(grade)
        
    def add_test_result(self, subject, test_result):
        self.subject_validator = subject
        if test_result not in range(0, 101):
            raise ValueError("Результат теста должен быть от 0 до 100.")
        
        if subject not in self.grades:
            self.grades[subject] = {'grades': [], 'test_results': []}
        
        self.grades[subject]['test_results'].append(test_result)

    
    def get_average_test_score(self, subject):
        self.subject_validator = subject
        test_results = self.grades[subject]['test_results']
        if not test_results:
            return 0
        return sum(test_results) / len(test_results)
    
    def get_average_grade(self):
        all_grades = [grade for subject_grades in self.grades.values() for grade in subject_grades['grades']]
        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)


if __name__ == "__main__":

    subjects_file_path = "subjects.csv"
    student = Student("Иванов Иван Иванович", subjects_file_path)

    student.add_grade("Математика", 4)
    student.add_test_result("Математика", 85)

    student.add_grade("Физика", 5)
    student.add_test_result("Физика", 92)

    try:
        student.add_grade("История", 3)
    except ValueError as e:
        print(e)

    try:
        student.add_test_result("История", 70)
    except ValueError as e:
        print(e)

    for subject in student.subjects:
        average_test_score = student.get_average_test_score(subject)
        print(f"Средний балл по тестам по предмету '{subject}': {average_test_score:.2f}")

    average_grade = student.get_average_grade()
    print(f"Общий средний балл по оценкам: {average_grade:.2f}")
