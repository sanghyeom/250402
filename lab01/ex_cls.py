# ex_cls

#class 이름만큼은 대문자로 시작함 (관행) ex) NyPerson
class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    
    def speed(self):
        return (self.height/self.weight)*5
    
    def print(self):
        print(f"나는{self.name}이고 키")

p1 = Person("Tom", 170, 100)
print(type(p1))
p1.print()
# print(p1.name,p1.height,p1.weight)

# p1 = {
#     'name':'Tom',
#     'height':170,
#     'weight':100
# }

# print(p1['name'],p1['height'],p1['weight'])
p2 = Person("kim", 180, 85)
print(p2.name,p2.height,p2.weight)


print( p1.speed() )
print( p2.speed() )


# 절차지향적으로 구성하면 결합이 느슨함, 
def speed(d):
    return (d['height']/d['weight'])*5