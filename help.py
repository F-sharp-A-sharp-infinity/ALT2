file = open("data.txt", "w")
file.write("Passw0rd")
file.close()
file = open("data.txt", "r")
unsalted_password_because_who_cares_about_data_encryption = file.read()
file.close()
user_input = input("enter password: ")
if user_input == unsalted_password_because_who_cares_about_data_encryption:
    print("correct password")
else:
    print("incorrect password")