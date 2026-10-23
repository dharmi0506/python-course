# ============================================================
# Farm Harvest Calculator
# ============================================================

# --- Assignment Operator (=) ---
# Store the harvest in kg from each of the 5 fields

field1 = 10

field2 = 12

field3 = 14

field4 = 15

field5 = 8

# --- Arithmetic Operators (+, -, *, /) ---
# Calculate total and average harvest

total_harvest = field1+ field2+ field3+ field4+ field5

avg = total_harvest/5  

print("Total harvest      :", total_harvest, "kg") #59kg
print("Average per field  :", avg, "kg") #11.8kg

# Price per kg is 15 rupees — calculate total earnings
earnings = total_harvest *15 
print("Total earnings     : Rs.", earnings) #


# --- Floor Division (//) and Modulus (%) ---
# Pack the harvest into bags of 25 kg each
bags     = total_harvest // 25 
leftover = total_harvest % 25 

print("Full bags packed  :", bags) #2
print("Leftover grain     :", leftover, "kg") #9

# --- Comparison Operators (>, <, ==, >=) ---
# Compare this year's harvest with last year
last_year = 500
print("Better than last year?  :", total_harvest > last_year) #false
print("Same as last year?      :", total_harvest == last_year) #false
print("At least as good?       :", total_harvest >= last_year) #false

# --- Assignment Operators (+=, -=) ---
# A bonus field adds 30 kg to the total_harvest
total_harvest += 30 
print("After bonus crop   :", total_harvest, "kg") #89kg

# Subtract 15 kg saved as seeds for next season
total_harvest -= 15
print("After seed reserve :", total_harvest, "kg") #74kg

# Final bag count after all adjustments
bags = total_harvest // 25 