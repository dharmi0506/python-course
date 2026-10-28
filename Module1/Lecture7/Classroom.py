choice = int(input("Enter 1 for two-wheeler and 2 for four-wheeler \n"))

# car_type = int(input("Enter 1 for 5 seater car and 2 for 7 seater cars\n"))
# bike_type = int(input("Enter 1 for Scooty and 2 for Bike\n"))

if choice == 1:             # outer: Bike

    bike_type = int(input("Enter 1 for Scooty and 2 for Bike\n"))

    if bike_type == 1:
        
        print("Scooty — 80 km/h") 

    else:

        print("Mountain Bike — 40 km/h")

elif choice == 2:           # outer: Car

    car_type = int(input("Enter 1 for 5 seater car and 2 for 7 seater cars\n"))

    if car_type == 1:

        print("Sedan — 5 seats")

    else:

        print("SUV — 7 seats")
        
