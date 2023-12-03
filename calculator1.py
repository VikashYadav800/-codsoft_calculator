class calculator:
      def add(a,b):
            return a + b
      
      def subtract(a,b):
            return a - b
      
      def multiply(a,b):
            return a * b
      
      def divide(a,b):
            if(b==0):
                  return "Error!division by zero is not allowed"
            else:
                  return a / b
            
calc = calculator()

while 'true':
      print("\n1.add")
      print("\n2.subtract")
      print("\n3.multiply")
      print("\n4.divide")
      print("\n5.exit")

      choice = input("enter the number according to your choice:")

      if choice=='1':
            num1=float(input("enter the first number:"))
            num2=float(input("enter the second number:"))
            print("the sum of",num1,"and",num2,"is", calculator.add(num1,num2))

      elif choice=='2':
            num1=float(input("enter the first number:"))
            num2=float(input("enter the second number:"))
            print("the difference of",num1,"and",num2,"is",calculator.subtract(num1,num2)) 

      elif choice=='3':
            num1=float(input("enter the first number:"))
            num2=float(input("enter the second number:"))
            print("the product of",num1,"and",num2, "is",calculator.multiply(num1,num2))

      elif choice=='4':
            num1=float(input("enter the first number:"))
            num2=float(input("enter the second number:"))
            print("the quotient of",num1,"and",num2,"is", calculator.divide(num1,num21))

      elif choice=='5':
            print("existing the calculator.")
            break
      
      else:
            print("invalid input !please enter a number between 1 and 5.")