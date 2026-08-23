# user-input file
def user_input():
    while True:
        try:
            number = float(input("Enter a number needed for calculation: "))
            return number
        except ValueError:
            print("Invalid Input. Try Again!")
