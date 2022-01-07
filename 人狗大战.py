class Person:
    role='person'
    def __init__(self,name,aggressivity,life_value,money):
        self.name=name#名字
        self.aggressivity=aggressivity#攻击力
        self.life_value=life_value#生命值
        self.money=money
    def attack(self,dog):
        dog.life_value-=self.aggressivity
class Dog:
    role='dog'
    def __init__(self,name,breed,aggressivity,life_value,money):
        self.name=name
        self.breed=breed
        self.aggressivity=aggressivity
        self.life_value=life_value
        self.money=money
    def bite(self,person):
        person.life_value-=self.aggressivity
class Weapon:
    def __init__(self,name,price,add_aggressivity,add_life_value):
        self.name=name
        self.price=price
        self.add_aggressivity=add_aggressivity
        self.add_life_value=add_life_value
    def update(self,obj):
        obj.money-=self.price
        obj.aggressivity+=self.add_aggressivity
        obj.life_value+=self.add_life_value
    def prick(self,obj):
        obj.life_value-=50


lance=Weapon('长矛',300,30,100)    
person_1=Person('egon',10,100,500)
dog_1=Dog('二愣子','哈士奇',30,100,0)

print('狗的生命',dog_1.life_value)
person_1.attack(dog_1)
print('人攻击了狗')
print('狗的生命',dog_1.life_value)

print('人类的生命',person_1.life_value)
dog_1.bite(person_1)
print('狗咬人')
print('人类的生命',person_1.life_value)
if(person_1.money>=lance.price):
    person_1.money-=lance.price
    print('人类的金钱',person_1.money)
    print('人类的生命',person_1.life_value)
    lance.update(person_1)
    person_1.yyy = lance
    print('购买成功')
    print('人类的生命',person_1.life_value)
    print('人类的攻击力',person_1.aggressivity)
else:
    print('购买失败')
    print('人类的生命',person_1.life_value)
    print('人类的攻击力',person_1.aggressivity)

print('狗的生命',dog_1.life_value)
person_1.attack(dog_1)
print('人攻击了狗')
print('狗的生命',dog_1.life_value)
if person_1.yyy==lance:
    person_1.yyy.prick(dog_1)
    print('人使用武器攻击了狗')
    print('狗的生命',dog_1.life_value)
