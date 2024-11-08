class Animal:
    def __init__(self, weight: float, height: float):
        self._weight = weight
        self._height = height

    def eat(self):
        ...

    def sleep(self):
        ...



class Cat(Animal): # Чертёж объекта кот/кошка
    count: int = 0
    def __init__(self, name: str, **props):
        self._name = name
        Cat.count += 1
        super().__init__(**props)
    
    @staticmethod
    def how_many_cats():
        print(f'There are {Cat.count} cats')

    def miau(self):
        print('Miau '*3)

    def __str__(self) -> str:
        return f'{self._name} with weight: {self._weight}'


cat_1 = Cat(input('Cat\'s name:'), weight=7.8, height=20.8) # Создаём экземпляр класса Cat

print(cat_1)
cat_1.miau()
cat_1.sleep()
Cat.how_many_cats()

# teo = Cat(name='Teo', weight=6.2, height=65.2)
ferty = 'privetikikkiki'
print('THe kak kfjoi j aoi {}'.format(ferty))#один из способов форматирования
#сейчас будет ипользован самый новый формат f-строки:
sad='vishni and persiki '
print(f'v sady pastyt {sad}')



