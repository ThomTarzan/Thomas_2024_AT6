class UserInputValidator:
    def __init__(self, input_list):  
        self.input_list = input_list
        self.is_digit = []
        self.validate_positive_integers()  

    def validate_positive_integers(self):
        self.is_digit = []  
        for el in self.input_list:
            if isinstance(el, str) and el.isdigit():  
                self.is_digit.append(el)
        return self.is_digit

    def __str__(self):  
        return str(self.is_digit)