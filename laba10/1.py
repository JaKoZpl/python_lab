class Driver:
    __pip = ""
    __driverLicense = ""
    __drivingExperience = ""
    __car = ""

    def __init__(self, pip, driverLicense, drivingExperience, car):
        self.__pip = pip
        self.__driverLicense = driverLicense
        self.__drivingExperience = drivingExperience
        self.__car = car

    @property
    def pip(self):
        return self.__pip

    @pip.setter
    def pip(self, k):
        self.__pip = k

    @property
    def driverLicense(self):
        return self.__driverLicense

    @driverLicense.setter
    def driverLicense(self, k):
        self.__driverLicense = k

    @property
    def drivingExperience(self):
        return self.__drivingExperience

    @drivingExperience.setter
    def drivingExperience(self, k):
        self.__drivingExperience = k

    @property
    def car(self):
        return self.__car

    @car.setter
    def car(self, k):
        self.__car = k

    def output(self):
        print("ПІП водія:", self.__pip)
        print("Категорія водія:", self.__driverLicense)
        print("Водійський стаж:", self.__drivingExperience)
        print("Марка транспорту:", self.__car)

    @classmethod
    def licenseFilter(cls, licenseType, *classObjects):
        for item in classObjects:
            if item.driverLicense == licenseType:
                print()
                print(item.pip)
                print(item.driverLicense)
                print(item.drivingExperience)
                print(item.car)


a = Driver("Онищук Сергій Васильович", "C", "10 років", "BMW")
a.output()
b = Driver("Кочубатов Петро Анатолійович", "C", "4 роки", "")
b.output()
Driver.licenseFilter("C", a, b)
