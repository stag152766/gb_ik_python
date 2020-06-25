# сортировка сложных структур

from collections import namedtuple
from operator import attrgetter

Person = namedtuple('Person', 'name, age')

p_1 = Person('Vasya', 25)
p_2 = Person('Kolya', 30)
p_3 = Person('Olya', 23)

people = [p_1, p_2, p_3]
print(people)


def by_age(person):
    return person.age


result = sorted(people, key=by_age)
print(result)

# не стоит каждый раз писать функцию, когда мы сортируем объект по ключу

result_2 = sorted(people, key=attrgetter('age'))
print(result_2)
