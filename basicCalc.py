# Made by Jacob Santora 12/11/2022
import math
print("Select a following operation: ")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
print("5 - Power")
print("6 - Logarithm")
print("7 - Square Root")
print("8 - Degrees to Radians")
print("9 - Radians to Degress")
print("10 - Sine")
print("11 - Cosine")
print("12 - Tangent")

def basicMath():
    print("Enter two Numbers to execute operation: ")
    num1 = int(input())
    num2 = int(input())

    if opNum == 1: 
        ans = num1 + num2
        print(ans)
    elif opNum == 2:
        ans = num1 - num2
        print(ans)
    elif opNum == 3:
        ans = num1 * num2
        print(ans)
    elif opNum == 4:
        ans = num1 / num2
        print(ans)

def complexMath():
    if opNum == 5:
        baseNum = int(input("Enter Base Number: "))
        powNum = int(input("Enter Power Number: "))
        ans = math.pow(baseNum, powNum)
        print(ans)
    elif opNum == 6:
        logNum = int(input("Enter Logarithm Number: "))
        logBase = int(input("Enter Base number: "))
        ans = math.log(logNum, logBase)
        print(ans)
    elif opNum == 7:
        sqrtNum = int(input("Enter Number to Square Root: "))
        ans = math.sqrt(sqrtNum)
        print(ans)
    elif opNum == 8:
        degNum = int(input("Enter Number in Degrees to convert to Radians: "))
        ans = math.radians(degNum)
        print(ans)
    elif opNum == 9:
        radNum = float(input("Enter Number in Radians to convert to Degrees: "))
        ans = radNum * 180 / math.pi
        print(ans)

def trigMath():
    if opNum == 10:
        sinNum = float(input("Enter Number for Sine execution: "))
        ans = math.sin(sinNum)
        print(ans)
    elif opNum == 11:
        cosNum = float(input("Enter Number for Cosine execution: "))
        ans = math.cos(cosNum)
        print(ans)
    elif opNum == 12:
        tanNum = float(input("Enter Number for Tangent execution: "))
        ans = math.tan(tanNum)
        print(ans)


opNum = int(input("Enter the operation Number: "))
if opNum > 0 and opNum <= 4:
    basicMath()
elif opNum >= 5 and opNum <= 9:
    complexMath()
elif opNum >= 10 and opNum <= 12:
    trigMath()