# Ride Cost Calculator 

Travelling_Km = float(input("Enter the Distance Travelled => "))
Diesel_cost = float(input("Enter the Cost of Diesal => "))
Vehicle_fuel_avg = float(input("Enter the Vehicle Fuel Average => "))

Fuel_consumption = (Travelling_Km/Vehicle_fuel_avg)
Cost_per_day = (Diesel_cost/Fuel_consumption)

print("The Cost of  Driving per day to office is = ", Cost_per_day)
