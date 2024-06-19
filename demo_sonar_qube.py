# This script is intentionally written with issues for SonarQube analysis

import os

#Inyeccion de Codigo
def risky_function():
    user_input = input("Enter something: ")
    eval(user_input)

#Code Smell
def unused_function():
    pass  

#String Duplicado
def duplicate_code():
    print("This is some duplicate code")
    print("This is some duplicate code")

#Loop ineficiente
def inefficient_loop():
    total = 0
    for i in range(1000):
        total += i
    return total

#Error de Indice
def bug_prone_code():
    my_list = [1, 2, 3]
    print(my_list[3])  # This will cause an IndexError (bug)

#abuso de condicional
def complex_function(a, b, c, d, e, f, g, h):
    if a and b and c and d and e and f and g and h:
        return True
    return False


#No respeta convecion de nombres
def non_compliant_naming():
    VAR = 5 
    return VAR

if __name__ == "__main__":
    risky_function()
    duplicate_code()
    print(inefficient_loop())
    try:
        bug_prone_code()
    except IndexError:
        print("Caught an IndexError!")
    print(non_compliant_naming())
    print(complex_function(True, True, True, True, True, True, True, True))

