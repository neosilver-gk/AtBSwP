# The practice in Chap3

def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = 3 * number + 1
        print(result)
        return result

while True:
    try:
        number = int(input('Please type in a Number: '))
        break
    except ValueError:
        print('Your input was not a Number! Try again ...')

while number != 1:
    number = collatz(number)
