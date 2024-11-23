def calculator():

    print ("Select an Operation:")
    print ("1. Addition")
    print ("2. Subtraction")
    print ("3. Multiplication")
    print ("4. Division")

    operation = input("Enter your number: ")

    if operation not in ["1","2","3","4"]:
        print ("INVALID, USER INPUT NOT INCLUDED.")

    if operation == "1":
        num1 = input ("Enter 1st number: ")
        num2 = input ("Enter 2nd number: ")
        result = int(num1) + int(num2) 
        print(f"The sum is {str(result)}")
    elif operation == "2":
        num1 = input ("Enter 1st number: ")
        num2 = input ("Enter 2nd number: ")
        result = int(num1) - int(num2) 
        print(f"The difference is {str(result)}")
    elif operation == "3":
        num1 = input ("Enter 1st number: ")
        num2 = input ("Enter 2nd number: ")
        result = int(num1) * int(num2)
        print(f"The product is {str(result)}")
    elif operation == "4":
        num1 = input ("Enter 1st number: ")
        num2 = input ("Enter 2nd number: ")
        if num2 == "0":
                print("num2 Invalid, The divisor is equal to zero")
        else:
                result = int(num1) / int(num2) 
                print(f"The qoutient is {str(result)}")
    else:
        print ("INVALID INPUT")

if __name__ == "__main__":
     calculator()