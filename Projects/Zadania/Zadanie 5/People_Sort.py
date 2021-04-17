"""Given a list of people objects, create a function that sorts the list by an attribute name.
The attribute to sort by will be given as a string.
The Person class will only include these attributes in the following order:

firstname
lastname
age"""


# Examples
# p1 = Person("Michael", "Smith", 40)
# p2 = Person("Alice", "Waters", 21)
# p3 = Person("Zoey", "Jones", 29)


class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age

    # def __getattr__(self, item):
    #     print("AA")
    # def __getattribute__(self,item):

    def __repr__(self):
        return
def people_sort(lista,atr):
    lista.sort(key=lambda x: x.firstname, reverse=True)
    return lista

    

p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)
# print(p1.__getattribute__("firstname"))

# print(people_sort([p1, p2, p3], "firstname"))
print(getattr(p1,'age'))
print(p1.__dict__['age'])

