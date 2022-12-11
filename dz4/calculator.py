from dz4.complex import Complex, ExponentialError


class OperationError(Exception):
    pass

def get_number(string):
    string = string.replace(" ", "")
    if string.find('i') > -1:
        im, re = string.split('+')
        re = re.split('*')[0]
        return Complex(float(im), float(re))
    else:
        return float(string)

print("Calculator")
print("Enter complex numbers as \"a + b * i\"")

while True:
    print("\nNew calculation:\n")
    try:
        a = get_number(input("Enter first number: "))
        op = input("Enter operand (+, -, /, *): ")
        b = get_number(input("Enter second number: "))

        if op == '+':
            ans = a + b
        elif op == '-':
            ans = a - b
        elif op == '/':
            ans = a / b
        elif op == '*':
            ans = a * b
        else:
            raise OperationError()

        print("\nAnswer:")
        print(ans)
    except ValueError:
        print("You have entered bad numbers! Try again")
    except OperationError:
        print("You have entered unsupported operation! Try again")
    except ZeroDivisionError:
        print("You have divided by zero! Try again")
    except ExponentialError:
        print("Unable to convert to exponential form! Try again")


