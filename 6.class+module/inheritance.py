class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return "안녕하세요. 저는 {}이고, 학생입니다.".format(self.name)


class EStudent(Student):
    def __str__(self):
        return "안녕하세요. 저는 {}이고, 초등학생입니다.".format(self.name)
    def print_age(self):
        print("{}의 나이는 {}살입니다.".format(self.name, self.age))
    
class MStudent(Student):
    def __str__(self):
        return "안녕하세요. 저는 {}이고, 중학생입니다.".format(self.name)
   
sasumi = Student("사스미", 4)
haedal = EStudent("해달이", 1)
boogie = MStudent("부기", 5)

print(sasumi)
print(haedal)
print(boogie)

haedal.print_age() # 부모에서 자식으로 상속
# sasumi.print_age() 자식에게 부모로 상속 불가
