#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username=="admin" and password=="12345":
        return "access granted"
    elif username=="ADMIN" and password=="12345":
        return "access granted"
    else: return "access denied"
        
    

def hows_the_weather(temperature):
    # your code here
    if temperature <40:
        return "It's brisk out there!""It's brisk out there!"
    elif temperature <65 and temperature >=40:
        return "It's a little chilly out there!"
    elif temperature >85:
        return "It's too dang hot out there!"
    else: return "It's perfect out there!"
    

def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    

def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero!"
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
