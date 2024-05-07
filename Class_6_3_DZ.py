""" Домашнее задание по теме "Наследование классов """

# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers, которая
# возвращает количество лошидиных сил для автомобиля
# Создайте наследника класса Car - класс Nissan и переопределите свойство price, а также переопределите функцию
# horse_powers
# Дополнительно создайте класс Kia, который также будет наследником класса Car и переопределите также свойство price,
# а также переопределите функцию horse_powers

class Car:

    price = 1000000
    horse_powers = 100

class Nissan(Car):

    price = 1500000
    horse_powers = 150

class Kia(Car):

    price = 1300000
    horse_powers = 120

car = Car()
nissan = Nissan()
kia = Kia()
print('Nissan')
print('Цена: ', nissan.price)
print('Лошединых сил: ', nissan.horse_powers)
print()
print('Kia')
print('Цена: ', kia.price)
print('Лошединых сил: ', kia.horse_powers)

