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