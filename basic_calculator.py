print("*" * 10 , "Basic Calculator with Arithmetic Operators" , "*" * 10)

result = 0;
ops = ""
operators_allowed = "+ , - , * , / , % "
while True:
  operation = input("Please select one of the operators : (+ , -, *, /, %) :")
  if operation in operators_allowed:
    num1 = float(input("Please enter the first number (ACCEPT ONLY NUMBER) :"))
    num2 = float(input("Please enter the second numbe (ACCEPT ONLY NUMBER) :"))
    
    if operation == "+":
      result = num1 + num2
      ops = "Addition"
      # print(result)
    elif operation == "-":
      result = num1 - num2
      ops = "Substraction"
    elif operation == "*":
      result = num1 * num2
      ops = "Multiply"
    elif operation == "/":
      result = num1 / num2
      ops = "Division"
    elif operation == "%":
      result = num1 % num2
      ops = "Modulus"
      
    print(f"The ressult of {ops} between {num1} and {num2} is : {result :.2f} ") 
  else:
    print("Invalid Operator! Only + , -, *, / or % operator is allowed")

  confirm = input("To exit the program presses x : ")
  if confirm.lower() == "x": break