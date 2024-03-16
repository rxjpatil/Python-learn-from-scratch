size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N  
extra_cheese = input() # Do you want extra cheese? Y or N

if size == 'S':
  base_p = 15
elif size == 'M':
  base_p = 20
elif size == 'L':
  base_p = 25

# Add ons 
if size == 'S' and add_pepperoni == 'Y':
  base_p +=2
elif size == 'M' or 'L'  and add_pepperoni == 'Y':
  base_p +=3

# Cheese Add ons 
if extra_cheese == 'Y':
  base_p += 1
print("Thank you for choosing Python Pizza Deliveries!")
print (f"Your final bill is: ${base_p}.")
