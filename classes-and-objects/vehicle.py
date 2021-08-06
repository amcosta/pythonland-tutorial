class Vehicle:
    """Exemplo de documentação de código em Python"""

    def __init__(self, started = False, speed = 0):
        self.started = started
        self.speed = speed

    def start(self):
        self.started = True
        print("'Car started, let's ride!'")

    def increase_speed(self, delta):
        if self.started:
            self.speed += delta
            print("Vrooooom!")
        else:
            print("You need to start the car first")

    def stop(self):
        self.speed = 0

class Car(Vehicle):
    trunk_open = False

    def open_trunk(self):
        self.trunk_open = True

    def close_trunk(self):
        self.trunk_open = False

class Motocycle(Vehicle):
    def __init__(self, started = False, speed = 0, center_stand_out = False):
        self.center_stand_out = center_stand_out
        super().__init__(started, speed)

c1 = Car()
c1.start()
c1.increase_speed(50)

m1 = Motocycle(center_stand_out=True)
m1.start()
m1.increase_speed(150)