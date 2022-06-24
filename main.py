
number1 = float(input("Number 1 "))
number2 = float(input("Number 2 "))
print("Addition is 1")
print("Subtraction is 2 ")
print("Multiplication is 3 ")
print("Division is 4 ")
opperation = int(input("Number of the opperation "))


if opperation == 1:
    answer1 = float(number1 + number2)
    print(answer1)
elif opperation == 2:
    answer2 = float(number1 - number2)
    print(answer2)
elif opperation == 3:
    answer3 = float(number1 * number2)
    print(answer3)
elif opperation == 4:
    answer4 = float(number1 / number2)
    print(answer4)