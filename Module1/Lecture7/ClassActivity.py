"""
1) Add the activity details.
   a) Mention the activity name as "Custom Ride Builder".
   b) Mention the file name as `ride_builder.py`.
   c) Mention the lesson as "Nested Conditional Statements".

2) Display the welcome message.
   a) Print a title banner for the ride builder.
   b) Add blank lines to keep the output neat.

3) Show the first vehicle choices.
   a) Display Bike as option 1.
   b) Display Car as option 2.
   c) Ask the user to enter 1 or 2.

4) Check the main choice.
   a) Use `if` when the user chooses Bike.
   b) Use `elif` when the user chooses Car.
   c) Use `else` for an invalid choice.

5) Use nested conditions for Bike.
   a) Show bike type options only if the user picked Bike.
   b) Ask the user to choose Scooty or Mountain Bike.
   c) Use an inner `if-else` to display the selected bike details.

6) Use nested conditions for Car.
   a) Show car type options only if the user picked Car.
   b) Ask the user to choose Sedan or SUV.
   c) Use an inner `if-else` to display the selected car details.

7) Display ride details.
   a) Print the selected ride name.
   b) Print speed or seat information.
   c) Print what the ride is best used for.

8) Handle invalid input.
   a) Show an error message if the first choice is not 1 or 2.
   b) Ask the user to enter the correct option next time.

9) End the program.
   a) Print a closing banner.
   b) Display a message saying the custom ride is ready.
"""

print("====================================")
print("      Welcome to Ride Builder!      ")
print("====================================")
print()

print("Option 1 : two-wheeler")
print("Option 2 : four-wheeler")

choice = input("Enter 1 or 2\n") 

choice = int(choice)

if choice == 1 :
    #this block only runs when the choice is 1
    print("Option 1 : scooty")
    print("Option 2 : Mountain Bike")
    two_wheeler = int(input("enter 1 or 2\n")) 

    if two_wheeler == 1 :
        #this block only executes if choice is 1 and two_wheeler is also 1
        print("You picked  : Scooty")
        print("Top speed   : 80 km/h")
        print("Best for    : City roads")
    else:
        #this block only executes if choice == 1 and two_wheeler != 1
        print("You picked  : Mountain Bike")
        print("Top speed   : 40 km/h")
        print("Best for    : Off-road trails")
elif choice == 2 :
    #this block only executes when choice == 2
    print("Step 2: Pick your car type")
    print(" Option 1 - Sedan")
    print(" Option 2 - SUV")
    print()

    
    car_type = int(input("enter 1 or 2\n "))
    if car_type == 1 :
        #this block only executes if choice == 2 and car_type == 1
        print("You picked  : Sedan")
        print("Seats       : 5 passengers")
        print("Best for    : Family trips")
    else :
        
        print("You picked  : SUV")
        print("Seats       : 7 passengers")
        print("Best for    : Off-road adventures")

else:
    print("That was not a valid choice.")
    print("Please enter 1 for Bike or 2 for Car.")

print()
print("====================================")
print("   Your custom ride is ready!       ")
print("   Enjoy the journey!               ")
print("====================================")
        
           

 
    
    
