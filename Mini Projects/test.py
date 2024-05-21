first = input("Give the first number: ")
operator = input("Choose the operator out of +, -, *, / : ")
second = input("Give the second number: ")

first = int(first)
second = int(second)

if(operator=="+"):
    print(first+second)
elif(operator=="-"):
    print(first-second)
elif(operator=="*"):
    print(first*second)
elif(operator=="/"):
    print(first/second)
else:
    print("Invalid Operator")
    
