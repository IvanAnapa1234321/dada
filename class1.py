class Person():#создаем класс  Person
    #x=5 вносим даные в этот класс
    def __init__(self,name,age):
        self.name=name
        self.age=age 
    def upfuns(self):# создаём метод(функцию)
        print(" Привет,меня зовут "+ self.name)
      
pers2=Person("Василий", 24 )
pers2.upfuns()# вызываем функцию 
 
 
#pers1=Person() присваивем переменной pers1 класс Person
#print(pers1.x) вызыаем данные из класса person и выводим на печать данные из класса с помощью прошлого действия

class Person1():#создаем класс  Person
    #x=5 вносим даные в этот класс
    def __init__(qwertyuiyt123,name,age):
        qwertyuiyt123.name=name
        qwertyuiyt123.age=age 
    def upfuns1(fadaserty):# создаём метод(функцию)
        print(" Привет,меня зовут "+ fadaserty.name)# Параметр self является ссылкой на сам класс и используется для доступа к переменным, принадлежащим классу.
        #Его не обязательно называть self, вы можете называть его как хотите, но он должен быть первым параметром любой функции в классе.
        #Используем слова qwertyuiyt123 и fadaserty вместо self:



pers3=Person1("Василий", 24 )
pers3.age=40 
#del pers3.age  удаляем данные класса 
print(pers3.name )
print(pers3.age)
pers3.upfuns1()# вызываем функцию 