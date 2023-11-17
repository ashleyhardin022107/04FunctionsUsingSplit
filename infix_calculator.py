expression = input("Enter an eqaution: ")
input1, operator, input2 = expression.split(" ")
if operator == "+":
    print(int(input1) + int(input2))
elif operator == "-":
    print(int(input1) - int(input2))
elif operator == "*":
    print(int(input1) * int(input2))
elif operator == "/":
    print(int(input1) / int(input2))