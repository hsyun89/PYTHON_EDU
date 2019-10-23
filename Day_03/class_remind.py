class Person:
    name = 'han'
    age =27
    def __init__(self,name):
        self.name = name
    def greeting(self):
        print(f'안녕하세요, 저는{self.name}입니다.')
    
class Student(Person):
    def __init__(self, name, student_id):
        self.name = name
        self.student_id= student_id
    def greeting(self):
        print(f'안녕하세요. 저는 {self.name}입니다. 아이디는 {self.student_id}입니다')

# p1 = Person('juan')
# p1.greeting()
# p2 = Student('justin',12345)
# p2.greeting()
print(Student.age)
print(Student.name)