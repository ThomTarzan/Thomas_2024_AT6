from User_input_validator import UserInputValidator

# test lists
ts1 = ["r", 5, "5", "-30", 11, "35"] # --> ["5", "35"]
ts2 = ["Hello", "10", "11", "-1", 123] # --> ["10", "11"]

# Instances
inst1 = UserInputValidator(ts1)
inst2 = UserInputValidator(ts2)

print(inst1)
print(inst2)