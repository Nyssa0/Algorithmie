import secrets
import random
import string

# list of passwords you can choose among
print("You can choose between these types of passwords :")
print("1 => Random password")
print("2 => Random password with at least an uppercase letter, a lowercase letter and a digit")
print("3 => Secure random password")


# generates passwords
def password_choice():
    # input to allow the user to choose the type of password they want
    choice = int(input("Please select the password you would like to generate by entering its number : "))

    # generates a message if you choose the wrong number and allows you to try again
    if 1 > choice or choice > 3:
        print("You have to select a number between 1 and 3. Please try again.")
        password_choice()

    if choice == 1:
        random_password()

    if choice == 2:
        random_password_2()

    if choice == 3:
        secure_password()


# generates a random password with letters and digits
def random_password():
    # the user can choose the length of the password
    length = int(input("How many characters do you want for your password ?"))
    # characters available : letters and digits in this case
    characters = string.ascii_letters + string.digits
    # generates the password randomly
    password = ''.join(random.choice(characters) for i in range(length))
    print("Your random password is: ", password)


# generates a random password with at least an uppercase letter, a lowercase letter and a digit
def random_password_2():
    # characters available : letters and digits in this case
    characters = string.ascii_letters + string.digits
    # selects 1 lowercase letter
    password = random.choice(string.ascii_lowercase)
    # selects 1 uppercase letter
    password += random.choice(string.ascii_uppercase)
    # selects 1 digit
    password += random.choice(string.digits)

    # the user can choose the length of the password
    length = int(input("How many characters do you want for your password (at least 3 characters) ? "))
    # generates an error if the user wants a password of less than 3 characters and allows you to try again
    if length < 3:
        print("You have to select a number superior or equal to 3. Please try again.")
        random_password_2()

    else:
        # generates other characters randomly and adds them to the password
        for i in range(length - 3):
            password += random.choice(characters)

        # list made out of the characters generated previously
        password_list = list(password)
        # shuffles all characters
        random.SystemRandom().shuffle(password_list)
        password = ''.join(password_list)
        print(f"Your random password is {password}")


# generates a secure random password
def secure_password():
    # the user can choose the length of the password
    length = int(input("How many characters do you want for your password ? "))
    # secure password
    password = ''.join((secrets.choice(string.ascii_letters + string.digits) for i in range(length)))
    print(f"Your secure password is {password}")


password_choice()

