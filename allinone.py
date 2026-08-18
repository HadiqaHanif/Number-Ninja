from take_input import user_input
class Calculate:
    def __init__(self):
        self.number = user_input()
    def even_odd(self):
        from take_input import user_input
        message = "ENTERED NUMBER IS EVEN!" if(self.number % 2 == 0) else("ENTERED NUMBER IS ODD!")
        print(message)
    def factorial(self):
        from take_input import user_input
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
        from take_input import user_input
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
        from take_input import user_input
        print(f"Area of a circle is: {3.14*self.number**2}.")
    def circumference_of_circle(self):
        from take_input import user_input
        print(f"Circumference of a circle is: {2*3.14*self.number}.")
    def area_of_sq(self):
        from take_input import user_input
        print(f"Area of a square is: {self.number*self.number}.")
    def perimeter_of_sq(self):
        from take_input import user_input
        print(f"Perimeter of a square is: {4*self.number}.")
    def leap_year(self):
        print( self.number % 4 == 0 and (self.number % 100 != 0 or self.number % 400 == 0))
    def sq_root_of_a_number(self):
        print(f"Sqaure Root is: {self.number**(1/2)}")
    
o = Calculate()
o.sq_root_of_a_number()



