from abc import ABC, abstractmethod



class Vehicle(ABC):

    def __init__(self, make, model, spec=""):
        self.make = make
        self.model = model
        self.spec = spec

    @property
    @abstractmethod
    def start_engine(self):
        pass

    def get_spec(self):
        print(f"{self.make} {self.model} ({self.spec})")

class Car(Vehicle):
    @property
    def start_engine(self):
        print(f"{self.make} {self.model}: Двигун запущено")

class Motorcycle(Vehicle):
    @property
    def start_engine(self):
        print(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):

    @abstractmethod
    def create_car(self, make, model) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make, model) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model) -> Car:
        return Car(make, model, "US Spec")
 
    def create_motorcycle(self, make, model) -> Motorcycle:
        return Motorcycle(make, model, "US Spec")

class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model) -> Car:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make, model) -> Motorcycle:
        return Motorcycle(make, model, "EU Spec")

# Використання
vehicle1 = Car("Toyota", "Corolla")
vehicle1.start_engine

vehicle2 = Motorcycle("Harley-Davidson","Sportster")
vehicle2.start_engine


usFactory = USVehicleFactory()
usVehicle1 = usFactory.create_car("Toyota", "Corolla")
usVehicle1.start_engine
usVehicle1.get_spec()

usVehicle2 = usFactory.create_motorcycle("Harley-Davidson","Sportster")
usVehicle2.start_engine
usVehicle2.get_spec()

euFactory = EUVehicleFactory()
euVehicle1 = euFactory.create_car("Toyota", "Corolla")
euVehicle1.start_engine
euVehicle1.get_spec()

euVehicle2 = euFactory.create_motorcycle("Harley-Davidson","Sportster")
euVehicle2.start_engine
euVehicle2.get_spec()
