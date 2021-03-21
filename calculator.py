print("Calculator");
print("Please enter an operation: ");

choice = input(" + : Addition, - : Subtraction, * : Multiplication, / : Division, ** : Exponentiation, % : Modulus ");

f_number = float(input("Enter your first number: "));
s_number = float(input("Enter your second number: "));

if choice == '+':
    print("Result: ", f_number + s_number)
elif choice == '-':
    print("Result: ", f_number - s_number)
elif choice == '*':
    print("Result: ", f_number * s_number)
elif choice == '/':
    if s_number == 0:
        print("You cannot divide by 0!")
    else:
        print("Result: ", f_number / s_number)
elif choice == '**':
    print("Result: ", f_number ** s_number)
elif choice == '%':
    print("Result: ", f_number % s_number)
else:
    print("You have not typed a valid operator, please run the program again.");
