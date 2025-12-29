logo=r'''
            __  __                                  _     _            
  ___ ___  / _|/ _| ___  ___   _ __ ___   __ _  ___| |__ (_)_ __   ___ 
 / __/ _ \| |_| |_ / _ \/ _ \ | '_ ` _ \ / _` |/ __| '_ \| | '_ \ / _ \
| (_| (_) |  _|  _|  __/  __/ | | | | | | (_| | (__| | | | | | | |  __/
 \___\___/|_| |_|  \___|\___| |_| |_| |_|\__,_|\___|_| |_|_|_| |_|\___|
                                                                       '''
MENU = {
  "espresso": {
      "ingredients": {
          "water": 50,
          "coffee": 18,
      },
      "cost": 1.5,
  },
  "latte": {
      "ingredients": {
          "water": 200,
          "milk": 150,
          "coffee": 24,
      },
      "cost": 2.5,
  },
  "cappuccino": {
      "ingredients": {
          "water": 250,
          "milk": 100,
          "coffee": 24,
      },
      "cost": 3.0,
  }
}

resources = {
  "water": 300,
  "milk": 200,
  "coffee": 100,
}

def check_resources(drink_name) :
  order_ingredients = MENU[drink_name]["ingredients"]
  for item, amt_req in order_ingredients.items() :
      if resources.get(item,0) < amt_req :
          print(f"Sorry there is not enough {item}.")
      return "enough"

def process_coins() :
  total=int(input("how many quarters? :")) *0.25
  total+=int(input("how many dimes? :")) *0.10
  total+=int(input("how many nickles? :")) *0.05
  total+=int(input("how many pennies? :")) *0.01
  return total

def make_coffee(drink_name) :
  order_ingredients = MENU[drink_name]["ingredients"]
  for item, amt_req in order_ingredients.items():
      resources[item]-=amt_req
  print(f"Here is your {drink_name} ☕. Enjoy!")

def coffee_machine() :
  is_on = True
  money_gained=0
  while is_on:
      print(logo)
      user_ip = input("What would you like? (espresso/latte/cappuccino) 😊 : ").lower()
      if user_ip == "off":
          print("Coffee Machine turning off...")
          is_on = False
      elif user_ip == "report":
          print("Current resource values 📃:")
          for key in resources:
              print(f"{key}: {resources[key]}")
          print(f"Money: ${money_gained}")
      elif user_ip=="espresso" or user_ip=="latte" or user_ip=="cappuccino" :
          resource_status = check_resources(user_ip)
          if resource_status != "enough":
              return resource_status
          else:
              inserted_coins = process_coins()
              if inserted_coins < MENU[user_ip]["cost"]:
                  print("Sorry that's not enough money. Money refunded.")

              else:
                  money_gained += MENU[user_ip]["cost"]
                  change = round(inserted_coins - MENU[user_ip]["cost"], 2)
                  print(f"Here is ${change} dollars in change.")
                  make_coffee(user_ip)
      else :
          print("Enter a valid input!")

coffee_machine()


