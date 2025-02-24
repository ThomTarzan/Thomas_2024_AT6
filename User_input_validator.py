class UserInputValidator:
    def __init__(self):
        self.is_digit = []
    
    def validate_positive_integers(self, lst):
        self.is_digit = [] # empty list
        for el in lst:
            if el.isdigit(): # True if el is a positiv integer (including zero)
                self.is_digit.append(el)
        return self.is_digit

# test data --> ['2', '6', '0'] if correct
test_list = ["2", "6", "-2", "0", "-100", "Hello", "!"]

uiv = UserInputValidator()

print(uiv.validate_positive_integers(test_list))