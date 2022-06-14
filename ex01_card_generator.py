import random

print("You can choose between these types of cards :")
print("1 => Visa")
print("2 => Mastercard")

# generates credit card numbers
def card_generator():
    numbers = []  # list of the card's numbers
    # input to choose the type of card
    card = int(input("What type of card do you want (type 1 for a Visa , type 2 for a Mastercard) ? "))

    if card == 1:
        print(f"Here is your Visa !")
        # generates randomly the first number of four digits which will start with 4
        start = random.randint(4000, 4999)
        # adding the first number to the list
        numbers.append(start)
        # generates the three other four-digit numbers
        for i in range(0, 3):
            number = format(random.randint(0000, 9999), '04d')  # format allowing four-digit numbers starting with zeros
            numbers.append(number)
        # prints the list as a string without and with spaces
        print(''.join(map(str, numbers)))
        print(' '.join(map(str, numbers)))

    elif card == 2:
        print(f"Here is your Mastercard !")
        # generates randomly the first number of four digits which will start with 5
        start = random.randint(5000, 5999)
        # adding the first number to the list
        numbers.append(start)
        # generates the three other four-digit numbers
        for i in range(0, 3):
            number = format(random.randint(0000, 9999), '04d') # format allowing four-digit numbers starting with zeros
            numbers.append(number)
        # prints the list as a string without and with spaces
        print(''.join(map(str, numbers)))
        print(' '.join(map(str, numbers)))

    # prevents the user from making a mistake by choosing the wrong number
    else:
        print(f"You made a mistake while choosing your card ! Try again please.")
        card_generator()


card_generator()

