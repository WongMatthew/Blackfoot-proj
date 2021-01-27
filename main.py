# CMPT120 Final Project - Audio Blackfoot
# Date: Dec 6th, 2020
# Authors: Matthew Wong & Mitchell Liu  

# Import modules 
import helper
import cmpt120image

# Main while loop
while True:
  
  # asks the user where they want to start
  move = input("Where do you want to go (Town/Restaurant/Home/Family/Greetings)? ")  

  if move.lower() == "town": 
    helper.town()

  elif move.lower() == "restaurant": 
    helper.restaurant()

  elif move.lower() == "home":
    helper.home()
    
  elif move.lower() == "family":
    helper.family()

  elif move.lower() == "greetings":
    helper.greetings()

  elif exit == False:
    break

  # if the user's input is invalid
  else:
    print("please enter a valid location")

