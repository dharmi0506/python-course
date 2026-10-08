# PART 1: Ask the agent for their details
name = input("Enter your real name, Agent: ") #Dharmi Agent
gadget = input("Enter your favorite gadget: ") #TV

# PART 2: Store the agent's details using different data types
agent_number = 7  #integar(int)
speed_rating = 9.5 #float
mission_count = 12 #integar(int)
height_m = 1.65 #float
is_active = True #boolean

# PART 3: Print each detail along with its data type
print("Name:", name, "-> type:", type(name)) #Name: Dharmi -> type: <cls str>
print("Gadget:", gadget, "-> type:", type(gadget)) #gadget:TV-> type: <cls str>

print("Agent Number:", agent_number, "-> type:", type(agent_number)) #Agent number:7-> <cls int>
print("Speed Rating:", speed_rating, "-> type:", type(speed_rating)) #Speed Rating:9.5-> <cls float>
print("Mission Count:", mission_count, "-> type:", type(mission_count)) #Mission Count:12-> <cls int>
print("Height (m):", height_m, "-> type:", type(height_m)) #Height m:1.65-> <cls float>
print("Is Active:", is_active, "-> type:", type(is_active)) # Is active:true-> <boolean>

# PART 4: Typecast the numbers and true/false value into text
agent_number_text = str(agent_number) # agent number text"-> string" , "int" 
mission_count_text = str(mission_count) # mission count "-> string " ,"float"
speed_rating_text = str(speed_rating) # speed rating"-> string" , "float"
status_text = str(is_active) # status text" -> string" , ?

print("Agent Number as text:", agent_number_text, "-> type:", type(agent_number_text)) 
#Agent Number as text: 123 -> type: <cls str>
print("Mission Count as text:", mission_count_text, "-> type:", type(mission_count_text)) #mision count text "-> string " , <cls int>
print("Speed Rating as text:", speed_rating_text, "-> type:", type(speed_rating_text)) # speed rating text "string " , <cls float>
print("Status as text:", status_text, "-> type:", type(status_text)) # status text " string " , <cls float>

# PART 5: Slice the name to create a secret code name
first_three = name[0:3] #name = Dharmi() , output : Dha
last_letter = name[-1:] #name =Dharmi () , output : i
code_name = first_three + last_letter # code name:Dha i
print("First 3 letters of name:", first_three) # Dha
print("Last letter of name:", last_letter) #i
print("Secret Code Name:", code_name) # code name:Dhai

# PART 6: Reverse the gadget name using slicing
reversed_gadget = gadget[::-1] #reversed gadget = television
print("Reversed Gadget Name:", reversed_gadget) #reversed gadget. output:noisivelet 

# PART 7: Join everything together to build the final badge message
badge_line_1 = "AGENT " + code_name.upper()
badge_line_2 = "ID: " + agent_number_text + " | MISSIONS: " + mission_count_text
badge_line_3 = "SPEED: " + speed_rating_text + " | ACTIVE: " + status_text
badge_line_4 = "SECRET GADGET CODE: " + reversed_gadget.upper()
#OUTPUT:"agent ID:SPEED SECRET GADJET CODE"
# PART 8: Print the complete secret agent badge
print("")
print("===== SECRET AGENT BADGE =====")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print("===============================")
#OUTPUT:"===== SECRET AGENT BADGE ===== "
#badge line 1
#badge line 2 
#badge line 3 
#badge line 4
#===============================