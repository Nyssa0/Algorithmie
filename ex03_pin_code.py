import datetime
import string
import random
import sys
import hashlib

sys.setrecursionlimit(1000000000)


# finds a password that was hashed
def find_password():
    # hashed version of the password that will be generated
    hashed_password = ''
    # hashed version of the password we want to find
    hashed = '8a069869956a4e0cf7ac69f9c20e0d49'
    # counter of attempts
    counter = 0
    # start of the chronometer
    time_start = datetime.datetime.now()
    # verifies if the hashed passwords correspond
    while hashed_password != hashed:
        # password length
        number = 8
        # type of characters : digits in this case
        characters = string.digits
        # generates a password
        password = ''.join(random.choice(characters) for i in range(number))
        # converts the password
        result_hash = hashlib.md5(password.encode())
        # returns the hashed password in an hexadecimal format
        hashed_password = result_hash.hexdigest()
        # increments the counter
        counter += 1
    # end of the chronometer
    time_end = datetime.datetime.now()
    # calculates the execution time
    exec_time = time_end - time_start
    print(f"Hashed version of the password we want to find : {hashed}")
    print(f"Generated password : {password}")
    print(f"Hashed version of the generated password : {hashed_password}")
    print(f"The two hashed passwords correspond so the password is {password}")
    print(f"Password found after {counter} attempts in {exec_time}")


find_password()

