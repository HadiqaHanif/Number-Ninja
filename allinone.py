class Calculate:
    def even_odd(self):

        message = "ENTERED NUMBER IS EVEN!" if(self.number % 2 == 0) else("ENTERED NUMBER IS ODD!")
        print(message)
    def factorial(self):

        if self.number < 0 :
            print("Factorial is not defined for negative numbers.")
        elif self.number == 0 :
            print("Factorial is: 1")
        else:
            factorial = 1
            for i in range(1, self.number + 1):
                factorial = factorial * i
            print("Factorial is:", factorial)
    def gpa_calculator(self):
  
        if(self.number >= 85 and self.number <=100): 
            print("Your GPA is 4.0")
        elif(self.number >= 80 and self.number <= 84):
            print("Your GPA is 3.7")
        elif(self.number >= 75 and self.number <= 79):
            print("Your GPA is 3.3")
        elif(self.number >= 70 and self.number <= 74):
            print("Your GPA is 3.0")
        elif(self.number >= 65 and self.number <= 69):
            print("Your GPA is 2.7")
        elif(self.number >= 60 and self.number <= 64):
            print("Your GPA is 2.3")
        else:
           print("Your GPA is below average. Better luck next time!")
    def area_of_circle(self):

        print(f"Area of a circle is: {3.14*self.number**2}.")
    def circumference_of_circle(self):

        print(f"Circumference of a circle is: {2*3.14*self.number}.")
    def area_of_sq(self):

        print(f"Area of a square is: {self.number*self.number}.")
    def perimeter_of_sq(self):

        print(f"Perimeter of a square is: {4*self.number}.")
    def leap_year(self):
        print( self.number % 4 == 0 and (self.number % 100 != 0 or self.number % 400 == 0))
    def sq_root_of_a_number(self):
        print(f"Sqaure Root is: {self.number**(1/2)}")

    def random_number(self):
        import random
        print("lets start gues-number-game between 1 and 100.")
        num = random.randint(1, 100)
        if num == self.number:
            print(f"You Won! Number is: {num}")
        else:
            print("Not match! Try again maybe you are close.")
    def table(self):
        print(f"Multiplication Table of {self.number} is:")
        for i in range(1, 11):
            print(f"{self.number} x {i} = {self.number*i}")
    def number_line(self):
        if self.number > 0:
            print("Entered number is Positive.")
        elif self.number < 0:
            print("Entered number is Negative.")
        else:
            print("Entered number is Zero.")
    def temp_category(self):
        if self.number >= 35:
            print("It's Hot! Take sunglasses.")
        elif self.number >= 25 and self.number <= 34:
            print("It's Moderate! Be Happy.")
        else:
            print("It's Cold! Stay covered , Stay save.")
    def cube_root(self):
        print(f"Cube root of number is: {self.number**(1/3)}")
    def cube(self):
        print(f"Cube of a number is: {self.number**3}.")
    def sq(self):
        print(f"Square of a number is: {self.number**2}.")
class Usage(Calculate):
    def selection_to_do(self):
        while True:
            print(f"Welcome to All-In-One Tool Kit.")
            print("Press 0 to exit.")
            print("Press 1 for Even/Odd.")
            print("Press 2 for Factorial.")
            print("Press 3 to Calculate GPA.")
            print("Press 4 for Area of Cirle.")
            print("Press 5 for Circumference of Circle.")
            print("Press 6 for Area of Square.")
            print("Press 7 fpr Perimeter of Square.")
            print("Press 8 to check leap-year.")
            print("Press 9 for Square-Root.")
            print("Press 10 for number guess game.")
            print("Press 11 for Multiplication-Table.")
            print("press 12 to check number (+,-,0)")
            print("Press 13 to check Temperature-Category.")
            print("Press 14 for Cube-Root.")
            print("Press 15 for Square.")
            print("Press 16 for Cube.")
            from take_input import user_input
            self.number = user_input()
            while True:
                try:
                    self.choice = int(input("Enter your choice: "))
                    break
                except :
                    print("Please Choose Option Between 0 and 15")
            if self.choice == 1 :
                self.even_odd()
            elif self.choice == 2 :
                self.factorial()
            elif self.choice == 3 :
                self.gpa_calculator()
            elif self.choice == 0:
                print("Are you sure to exit?\n" , "(Yes/No)")
                a = input("Your choice here: ").lower()
                if a == "no":
                    continue
                else:
                    print("Exited")
                    return
            elif self.choice == 4 :
                self.area_of_circle()
            elif self.choice == 5:
                self.circumference_of_circle()
            elif self.choice == 6:
                self.area_of_sq()
            elif self.choice == 7:
                self.perimeter_of_sq()
            elif self.choice == 8:
                self.leap_year()
            elif self.choice == 9:
                self.sq_root_of_a_number()
            elif self.choice == 10:
                self.random_number()
            elif self.choice == 11:
                self.table()
            elif self.choice == 12:
                self.number_line()
            elif self.choice == 13:
                self.temp_category()
            elif self.choice == 14:
                self.cube_root()
            elif self.choice == 15:
                self.sq()
            elif self.choice == 16:
                self.cube()
            else:
                print("Option not available yet.")
            while True:
                print("Press 'E' to exit and 'M' to return to options dashboard: ")
                b = input("Enter your choice: ").upper()
                if b == "E":
                    exit()
                elif b == "M":
                    break
                else:
                    print("Invalid Input! Select only 'E' or 'M'.")
o = Usage()
o.selection_to_do()
