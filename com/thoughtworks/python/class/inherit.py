class Person(object):
    pass


class Student(Person):
    def speak(self):
        print 'Student speak'


class Teacher(Person):
    def speak(self):
        print 'Teacher speak'


class SkillMixin(object):
    pass


class BasketballMixin(SkillMixin):
    def skill(self):
        return 'basketball'


class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'


class BStudent(Student, BasketballMixin):
    pass


class FTeacher(Teacher, FootballMixin):
    pass


s = BStudent()
print s.skill()

t = FTeacher()
print t.skill()


class StuTea(Teacher, Student):
    pass


StuTea().speak()


Teacher.speak(Teacher())
