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