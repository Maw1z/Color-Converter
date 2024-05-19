def get_rgb(color):
    while True:
        try:
            value = int(input(f"Enter {color} value: "))
            if 0 <= value <= 255:
                return value
            else:
                print(f"{color} value must be between 0 and 255. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer value.")
     
     
def get_hex():
    while True:
        value = input("Enter hexcode with #: ")
        if len(value) != 7:
            print("Please enter valid hexcode. Please try again.")
        else:
            return value
        

def get_cymk(color):
    while True:
        try:
            value = int(input(f"Enter {color} percentage:"))
            if 0 <= value <= 100:
                return value
            else:
                print(f"{color} value must be between 0 and 255. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer value")
        