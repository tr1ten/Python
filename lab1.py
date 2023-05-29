import math
def celciusToFahrenheit():
    c = int(input("Celcius : "))
    print("Fahrenheit : ", (c * 9 / 5) + 32)

def areaOfCylinder():
    r = int(input("Radius : "))
    h = int(input("Height : "))
    print("Area : ", 2 * math.pi * r * (r + h))

def volumeOfCylinder():
    r = int(input("Radius : "))
    h = int(input("Height : "))
    print("Volume : ", math.pi * r * r * h)
    
    
def feetToMetre():
    f = int(input("Feet : "))
    print("Metre : ", f * 0.3048)

# sum to all prime till n
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def sumOfPrimes():
    # Path: lab1.py
    n = int(input("n : "))
    sum = 0
    for i in range(2, n + 1):
        if isPrime(i):
            sum += i
    print("Sum : ", sum)
    
    
def euclideanDistance():
    x1,y1 = map(int, input("x1 y1 : ").split())
    x2,y2 = map(int, input("x2 y2 : ").split())
    print("Distance : ", ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
    
# energy of water in joules given intital temp and final temp given weight
def energyOfWater():
    m = int(input("Weight : "))
    i = int(input("Initial temp : "))
    f = int(input("Final temp : "))
    print("Energy : ", m * (f - i) * 4184)
    
def poundsToKg():
    x = int(input("Pounds : "))
    print("Kg :", x*0.453592)

if __name__=='__main__':
    # poundsToKg()
    # feetToMetre()
    # areaOfCylinder()
    # celciusToFahrenheit();
    # sumOfPrimes()
    # euclideanDistance()
    energyOfWater()
    
