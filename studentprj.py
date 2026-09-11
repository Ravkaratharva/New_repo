# Making a simple calculator 

import math

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): 
    if b == 0:
        return "Error: Division by zero"
    return a / b
def mod(a, b): return a % b
def exp(a, b): return a ** b
def sqrt(a): 
    if a < 0:
        return "Error: Negative number"
    return math.sqrt(a)
def fact(a):
    if a < 0 or not a.is_integer():
        return "Error: Factorial requires a non-negative integer"
    return math.factorial(int(a))
def trig_sin(a): return math.sin(math.radians(a))
def trig_cos(a): return math.cos(math.radians(a))
def trig_tan(a): return math.tan(math.radians(a))
def log(a):
    if a <= 0:
        return "Error: Logarithm undefined for zero or negatives"
    return math.log10(a)

operations = {
    '+': add, '-': sub, '*': mul, '/': div, '%': mod, '^': exp
}

single_operations = {
    'sqrt': sqrt, 'fact': fact, 'sin': trig_sin, 'cos': trig_cos, 'tan': trig_tan, 'log': log
}

def calculator():
    print("=== Advanced Python Calculator ===")
    print("Binary operations (+, -, *, /, %, ^) e.g., 5 + 3")
    print("Unary operations (sqrt, fact, sin, cos, tan, log) e.g., sqrt 16")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("\nEnter calculation: ").strip().lower()
        if user_input == 'exit':
            print("Goodbye!")
            break
            
        parts = user_input.split()
        
        try:
            if len(parts) == 3:
                num1, op, num2 = float(parts[0]), parts[1], float(parts[2])
                if op in operations:
                    print("Result:", operations[op](num1, num2))
                else:
                    print("Invalid binary operator.")
            elif len(parts) == 2:
                op, num1 = parts[0], float(parts[1])
                if op in single_operations:
                    print("Result:", single_operations[op](num1))
                else:
                    print("Invalid unary operator.")
            else:
                print("Invalid input format. Use: [num1] [op] [num2] or [op] [num].")
        except ValueError:
            print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    calculator()