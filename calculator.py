import math

def main_menu():
    print("\nPlease choose from one of the following menu options, or choose 3 to exit the program:")
    print("1. Basic Calculation (+, -, *, /)")
    print("2. Advanced Calculation (Sine, Cosine, Natural Logarithm)")
    print("3. (Exit Program)")
    choice = input("\nType option number here: ")
    return choice

def basic_calculation():
    while True:
        print("\nPlease choose from one of the following basic calculation options, or choose 5 to return to the main menu:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. (Return to Main Menu)")
        choice = input("\nType option number here: ")
        
        if choice == '5':
            return
        elif choice in ['1', '2', '3', '4']:
            if choice == '1':
                print("\nPlease enter the two numbers you want to add:\n")
            elif choice == '2':
                print("\nPlease enter the number that will be subtracted from first, and then the number that will be taken away second:\n")
            elif choice == '3':
                print("\nPlease enter the two numbers you want to multiply:\n")
            elif choice == '4':
                print("\nPlease enter the number that will be divided (dividend) first, and then the number that will do the dividing (divisor) second:\n")

            num1 = float(input("Enter the first number here: "))
            num2 = float(input("Enter the second number here: "))
            
            if choice == '1':
                print("\nResult:", num1 + num2)
            elif choice == '2':
                print("\nResult:", num1 - num2)
            elif choice == '3':
                print("\nResult:", num1 * num2)
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print("\nResult:", num1 / num2)
        else:
            print("Invalid option. Please choose a valid operation.")

def advanced_calculation():
    while True:
        print("\nPlease choose from one of the following advanced calculation options, or choose 4 to return to the main menu:")
        print("1. Sine (sin(x))")
        print("2. Cosine (cos(x))")
        print("3. Natural Logarithm (ln(x))")
        print("4. (Return to Main Menu)")
        choice = input("\nType option number here: ")
        
        if choice == '4':
            return
        elif choice in ['1', '2']:
            if choice == '1':
                print("\nPlease enter the angle in degrees to calculate its Sine value. You can enter any real number (e.g., -30, 45, 180):\n")
            elif choice == '2':
                print("\nPlease enter the angle in degrees to calculate its Cosine value. You can enter any real number (e.g., -30, 45, 180):\n")
            angle = float(input("Enter the angle in degrees here: "))
            if choice == '1':
                print("\nResult:", math.sin(math.radians(angle)))
            elif choice == '2':
                print("\nResult:", math.cos(math.radians(angle)))
        elif choice == '3':
            print("\nPlease enter a positive number to calculate its natural logarithm (⁡ln). Note that the number must be greater than zero.\n")
            num = float(input("Enter positive number here: "))
            if num <= 0:
                print("Error: Please enter a positive number greater than zero for natural logarithm.")
            else:
                print("\nResult:", math.log(num))
        else:
            print("Invalid option. Please choose a valid operation.")

def run_calculator():
    while True:
        choice = main_menu()
        if choice == '1':
            basic_calculation()
        elif choice == '2':
            advanced_calculation()
        elif choice == '3':
            print("\nExiting program. Thank you for using the calculator.")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 3.")
            continue

if __name__ == "__main__":
    run_calculator()