print("🧮 Welcome to Calculator App!")
def add(a,b):
    return a + b

def sub(a,b):
    return(a - b)

def mult(a,b):
    return(a * b)

def div(a,b):
    if b == 0:
        return "❌ Cannot divisible by zero!"
    return a / b
     
def modulus(a,b):
    if b== 0:
        return "❌ Cannot divisible by zero!"
    return a % b

def power(a,b):
    return a**b

while True:
    print("\n====== 🧮 CALCULATOR MENU ======")
    print("1. ➕ Addition")
    print("2. ➖ Subtraction")
    print("3. ✖️ Multiplication")
    print("4. ➗ Division")
    print("5. 🔢 Modulus")
    print("6. ⚡ Power")
    print("7. 🚪 Exit")

    choice = int(input("Enter your choice(1-7): "))
 
    if choice == 7:
        print("👋Bye, Have a nice day!🙏")
        break

    if choice in [1,2,3,4,5,6]:
        try:
            a = float(input("enter the first number: "))
            b = float(input("enter the second number: "))
            
        except ValueError:
            print("❌ PLEASE ENTER THE VALID NUMBERS! ")
            continue

        if choice == 1:
            result = add(a,b)
            print(f"✅ Result: {result}")

        elif choice == 2:   
            result = sub(a,b)
            print(f"✅Result: {result}")

        elif choice == 3:
            result = mult(a,b)
            print(f"✅Result {result}")

        elif choice == 4:
            result = div(a,b)
            print(f"✅Result {result}")

        elif choice == 5:
            result = modulus(a,b)
            print(f"✅Result {result}")

        elif choice == 6:
            result = power(a,b)
            print(f"✅Result {result}")

    else:
        print("❌ Invalid option! Please choose 1-7.")
                


    
    
