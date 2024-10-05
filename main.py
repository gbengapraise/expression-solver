
class Expression:
   
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def display(self):
       
        result = self.num1 + self.num2 * self.num3
        print(f"The result of the expression {self.num1} + {self.num2} * {self.num3} is: {result}")



def main():
   
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    
    expression = Expression(num1, num2, num3)


    expression.display()


if __name__ == "__main__":
    main()