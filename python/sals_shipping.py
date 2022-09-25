weight = 3.3
# "Ground Shipping"

price_perpound = 0

flat_charge = 0

total_cost_ground = 0

total_cost_drone = 0

cost_premium_ground = 125
#Ground Shipping
if weight <= 2:
  price_perpound = 1.5
  flat_charge = 20
  total_cost_ground = (weight * price_perpound) + flat_charge
     
elif ((weight > 2) and (weight <= 6)):
  price_perpound = 3
  flat_charge = 20
  total_cost_ground = (weight * price_perpound) + flat_charge
     
elif ((weight > 6) and (weight <= 10)):
  price_perpound = 4
  flat_charge = 20
  total_cost_ground = (weight * price_perpound) + flat_charge
  
elif weight > 10:
  price_perpound = 4.75
  flat_charge = 20
  total_cost_ground = (weight * price_perpound) + flat_charge
#Drone Shipping 
if weight <= 2:
  price_perpound = 4.5
  flat_charge = 0
  total_cost_drone = (weight * price_perpound) + flat_charge
    
elif ((weight > 2) and (weight <= 6)):
  price_perpound = 9
  flat_charge = 0
  total_cost_drone = (weight * price_perpound) + flat_charge
      
elif ((weight > 6) and (weight <= 10)):
  price_perpound = 12
  flat_charge = 0
  total_cost_drone = (weight * price_perpound) + flat_charge
    
elif weight > 10:
  price_perpound = 14.25
  flat_charge = 0
  total_cost_drone = (weight * price_perpound) + flat_charge

print("Ground Shipping Premium $", cost_premium_ground + total_cost_ground)
print("Cost of Standard Shipping is:", total_cost_ground)
print("Cost of Drone Shipping is:", total_cost_drone)


