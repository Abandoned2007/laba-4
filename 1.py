class Car:
    color = None # цвет автомобиля
    fuel = None #количество топлива
    door = None
    wheel = None
    brand = None
    model = None
    year = None
    
    def go(self):
        pass
	
    def turn(self):
        pass

    def stop(self):
        pass

myCar = Car()
myCar.brand = 'Audi'
myCar.model = 'A7'
myCar.year = '2022'
myCar.color = 'red'  # красим в красный цвет
myCar.fuel = 50  # заливаем топливо
myCar.door = 4
myCar.wheel = 4
myCar.go() 
myCar.turn() 
myCar.stop()
print(myCar.brand)
print(myCar.model)
print(myCar.year)
print(myCar.color)
print(myCar.fuel)
print(myCar.door)
print(myCar.wheel)

