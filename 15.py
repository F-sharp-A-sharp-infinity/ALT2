car_list = ["ford", "renault", "vw", "bmw"]
user_input = input("please enter car manufacturer: ")
user_input = user_input.lower()
if user_input in car_list:
    print("we stock this car manufacturer.")
else:
    print("we do not stock this car manufacturer.")