#Terrence Barnes Jr.
#10/6/2026
#P2LAB2
#A program that creates a dictionary 

car = {'Camaro':18.21, 'Prius':52.36, 'Model S':110, 'Silverado':26}

car_keys = car.keys()

print(car_keys)

print(*car_keys, sep = ", ")

car_name = input("Enter a car name: ")

carmpg = car[car_name]

print(f"the {car_name} gets {carmpg} miles per gallon.")

miles_driven = float(input(f"How many miles have you driven with the {car_name}? "))

gallons_needed = miles_driven / carmpg
print(f"{gallons_needed:.2f} gallons of gas are needed to drive the {car_name} {miles_driven} miles.")