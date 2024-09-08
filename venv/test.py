# class Player:
#
#     def __init__(self, name):
#         self.name = name
#         self.hp = 100
#
#
#     def showInfo(self):
#         print(f"Name:{self.name}")
#         print(f"Hp:{self.hp}")
#
#     def setHp(self, newHp):
#         self.hp = newHp
#     def getHp(self):
#         return self.hp
#
#
#
#
# player1 = Player("human")
# player1.showInfo()
# player1.setHp(12)
# print(player1.getHp())
# player1.showInfo()
#
# player2 = Player("elf")
# player2.showInfo()

class Student:
    def __init__(self, name, grade, money, intelegence, age):
        self.name = name
        self.grade = grade
        self.money = money
        self.intelegence = intelegence
        self.age = age

    def setName(self, newName):
        self.name = newName
    def setGrade(self, newGrade):
        self.grade = newGrade
    def setMoney(self, newMoney):
        self.money = newMoney
    def setIntelegence(self, newIntelegence):
        self.intelegence = newIntelegence
    def setAge(self, newAge):
        self.age = newAge
    def showInfo(self):

        print(f"Name:{self.name}")
        print(f"age:{self.age}")
        print(f"grade:{self.grade}")
        print(f"money:{self.money}💲")
        print(f"intelegence:{self.intelegence}")
        print("-----------------------------------------")
    def getName(self):
        return self.name
    def getGrade(self):
        return self.grade
    def getMoney(self):
        return self.money
    def getIntelegence(self):
        return self.intelegence
    def getAge(self):
        return self.age
Student1 = Student("markus", "9", "2000", "59/100", "15")
Student1.showInfo()
Student1.setMoney("1500")
Student1.showInfo()



