class Transport:
    def __init__(self) -> None:
        pass
    def calculate_cost(self,weight,distance):
        return weight*distance

class Truck(Transport):
    def __init__(self) -> None:
        super().__init__()
    def calculate_cost(self,weight,distance):
        return weight*distance

class Ship(Transport):
    def __init__(self) -> None:
        super().__init__()
    def calculate_cost(self,weight,distance):
        return weight*2*distance

class Plane(Transport):
    def __init__(self) -> None:
        super().__init__()
    def calculate_cost(self,weight,distance):
        return weight*120*distance
print("Ship-->")
ship = Ship()
print(ship.calculate_cost(4,5))
print("Truck-->")
truck = Truck()
print(truck.calculate_cost(40,60))
print("Transport-->")
transport = Transport()
print(transport.calculate_cost(3,4))
print("Plane-->")
plane = Plane()
print(plane.calculate_cost(2,4))