# This script is intentionally written with issues for SonarQube analysis

import os
import logging

USERNAME = "admin"
PASSWORD = "password123"

def risky_function():
    user_input = input("Enter something: ")
    eval(user_input)  

def unused_function():
    pass  

def duplicate_code():
    print("This is some duplicate code")
    print("This is some duplicate code")  

def inefficient_loop():
    total = 0
    for i in range(1000):
        total += i
    return total

def bug_prone_code():
    my_list = [1, 2, 3]
    print(my_list[3])

def complex_function(a, b, c, d, e, f, g, h):
    if a and b and c and d and e and f and g and h:
        return True
    return False 

def non_compliant_naming():
    VAR = 5 
    return VAR

def log_sensitive_info():
    logging.basicConfig(level=logging.INFO)
    logging.info(f"Logging in with username: {USERNAME} and password: {PASSWORD}") 

def magic_numbers():
    return 3.14159 * 2 * 10  

def poor_error_handling():
    try:
        1 / 0
    except Exception as e:
        print("An error occurred")  

# Commented-out code (code smell)
# def old_function():
#     pass


def long_function():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    j = 10
    k = 11
    l = 12
    m = 13
    n = 14
    o = 15
    p = 16
    q = 17
    r = 18
    s = 19
    t = 20
    u = 21
    v = 22
    w = 23
    x = 24
    y = 25
    z = 26
    return a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p + q + r + s + t + u + v + w + x + y + z

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
    log_sensitive_info()
    print(magic_numbers())
    poor_error_handling()
    long_function()
