def calculator():
    operator = input("Please, choose necessary operator: ")

    number_1 = int(input('Enter the number: '))

    number_2 = int(input('Enter the number: '))

    if operator == "+":
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    elif operator == "-":
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
    elif operator == "*":
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
    elif operator == "/":
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    else:
        print("Please, enter the valid operators")

calculator()




