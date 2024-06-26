from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, yob) -> None:
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name, yob, grade) -> None:
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(
            f'Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}')


class Doctor(Person):
    def __init__(self, name, yob, specialist) -> None:
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print(
            f'Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}')


class Teacher(Person):
    def __init__(self, name, yob, subject) -> None:
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(
            f'Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}')


class Ward:
    def __init__(self, name) -> None:
        self.__name = name
        self.__list_people = list()

    def add_person(self, person: Person):
        self.__list_people.append(person)

    def describe(self):
        print(f'Ward Name: {self.__name}')
        for p in self.__list_people:
            p.describe()

    def count_doctor(self):
        counter = sum(isinstance(p, Doctor) for p in self.__list_people)
        return counter

    def sort_age(self):
        self.__list_people.sort(key=lambda p: p._yob)

    def compute_average(self):
        yob_average = sum(
            p._yob for p in self.__list_people if isinstance(p, Teacher)) / sum(isinstance(p, Teacher) for p in self.__list_people)
        return yob_average


# Testcases:
if __name__ == "__main__":
    # (2a)
    student1 = Student(name="studentA", yob=2010, grade="7")
    student1.describe()
    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    teacher1.describe()
    doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
    doctor1.describe()

    # (2b)
    print()
    teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
    doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
    ward1 = Ward(name="Ward1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    ward1.describe()

    # (2c)
    print(f'\nNumber of doctors: {ward1.count_doctor()}')

    # (2d)
    print("\nAfter sorting Age of Ward1 people")
    ward1.sort_age()
    ward1.describe()

    # (2e)
    print(
        f"\nAverage year of birth ( teachers ): {ward1.compute_average()}")
