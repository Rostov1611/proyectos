# Data entry request

Password_1= input("Create a password.")
Password_2 = input("Confirm your password.")

# Logical Comparison Operators

They_are_the_same = (Password_1 == Password_2)
It_is_Long= (len(Password_1)>= 8)


# Conditional statements to display the result

if They_are_the_same and It_is_Long:
    print("Password Successfully Created!.")
elif not It_is_Long:
    print("Error! The password must be at least 8 characters long.")
else:
    print("Error! Passwords do not match.")