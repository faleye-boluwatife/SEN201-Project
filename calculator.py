# Implementation of the SDLC Design

def MathModule(a, b, sign):
    # This matches the MathModule in our Design
    if sign == "+":
        return a + b
    elif sign == "-":
        return a - b
    else:
        return "Error"

def InputModule():
    # This matches the InputModule in our Design
    print("Welcome to the Calculator Project")
    n1 = float(input("Enter number: "))
    op = input("Enter + or -: ")
    n2 = float(input("Enter number: "))
    
    result = MathModule(n1, n2, op)
    print("Result:", result)

if __name__ == "__main__":
    InputModule()
