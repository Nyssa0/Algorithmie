# converts a binary number to a hexadecimal number
def binary_to_hexa():
    # the user can enter a number
    number = str(input("Please type the number you would like to convert : "))
    # creates a binary number by deleting spaces if there are any
    binary = number.replace(' ', '')
    # conversion
    hexa = '%0*X' % ((len(binary) + 3) // 4, int(binary, 2))
    print(f"Binary number : {binary}")
    print(f"Hexadecimal number : {hexa}")


binary_to_hexa()

