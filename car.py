class Wheel:
# constructor
    def __init__(self, num_wheels, quality):
        self.__setNumWheels(num_wheels)
        self.__setQuality(quality)

# private function
    def __setNumWheels(self, num_wheels):
        self.num_wheels = num_wheels

# private
    def __setQuality(self, quality):
        self.quality = quality

# public
    def getNumWheels(self):
        return self.num_wheels

# public
    def getQuality(self):
        return self.quality


class Vehicle:
#Constructor
    def __init__(self, num_wheels, wheel_quality, engine):
#composition
        self._wheels = Wheels(num_wheels, wheel_quality)
        self._engine = engine
#public method
    def printInfo(self):
        print("Number of wheels:", self._wheels.getNumWheels())
        print("Wheel Quality:", self._wheels.getQuality())
        print("Engine Type:", self._engine)
        print("\n")

class Truck(Vehicle):
#Constructor
    def __init__(self, num_wheels, wheel_quality, engine, size):
        Vehicle.__init__(self, num_wheels, wheel_quality, engine)
        self.__size = size
#Override
    def printInfo(self):
        print("Number of wheels in truck:", self._wheels.getNumWheels())
        print("Wheel Quality of truck:", self._wheels.getQuality())
        print("Engine Type of truck:", self._engine)
        print("Truck Size:", self.__size)
        print("\n")

class Car(Vehicle):
#Constructor
    def __init__(self, num_wheels, wheel_quality, engine, model):
        Vehicle.__init__(self, num_wheels, wheel_quality, engine)
        self.__model = model
#Override
    def printInfo(self):
        print("Number of wheels in car:", self._wheels.getNumWheels())
        print("Wheel Quality of car:", self._wheels.getQuality())
        print("Engine Type of car:", self._engine)
        print("Car Model:", self.__model)
        print("\n")