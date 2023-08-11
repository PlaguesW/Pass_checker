digits = [i for i in '0123456789']
lowercase_let = [i for i in 'abcdefghijklmnopqrstuvwxyz']
uppercase_let = [i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
punctuation = [i for i in '!#$%&*+-=?@^_']
num_pass, chars = input('Enter amount of passwords to generate: '), []
while 1:  # Check of correct numbers of passwords
    if not str(num_pass).isdigit() or int(num_pass) < 0:
        print('Please enter a positive natural number: ')
        num_pass = input()
    else:
        num_pass = int(num_pass)
        break
from random import *

len_pass = input(
    'Enter the length of one password. Password must contain at least 8 Characters: ')
while 1:  # Check of correct length of passwords
    if not str(len_pass).isdigit() or int(len_pass) < 7:
        print('Please enter a positive natural number greater than 7:')
        len_pass = input()
    else:
        len_pass = int(len_pass)
        break


def valid_1_0():  # Check of correctness input 1 or 0
    while 1:
        ans = input()
        if ans not in str(10):
            print('Please enter 1 or 0')
        else:
            return int(ans)


print('Include the numbers 0123456789? Yes - Enter 1, No - Enter 0.')
include_digits = valid_1_0()
print('Include lowercase letters abcdefghijklmnopqrstuvwxyz? Yes - Enter 1, No - Enter 0')
include_lowercase_let = valid_1_0()
print('Include uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ? Yes - Enter 1, No - Enter 0')
include_uppercase_let = valid_1_0()
print('Include symbols !#$%&*+-=?@^_? Yes - Enter 1, No - Enter 0')
include_punctuation = valid_1_0()
print('Exclude ambiguous characters il1Lo0O? Yes - Enter 1, No - Enter 0.')
exclude = valid_1_0()
if exclude:  # avoiding of ambiguous characters
    digits.remove('0')
    digits.remove('1')
    lowercase_let.remove('i')
    lowercase_let.remove('l')
    lowercase_let.remove('o')
    uppercase_let.remove('L')
    uppercase_let.remove('O')


def chars_app(lists, n):  # Adding characters to the password
    if n > 0:
        for _ in range(n):
            chars.append(choice(lists))
    return chars


def generate_password():
    vol_digits = vol_lowercase = vol_upper = volume_punctuation = 0
    if include_digits:  # Random selection of the numbers of digits in the password include other symbols
        vol_digits = randint(1, (len_pass - include_lowercase_let - include_uppercase_let -
                                    include_punctuation))
    if include_lowercase_let:  # Random selection of the numbers of lowercase letters in the password include other symbols
        vol_lowercase = randint(1, (len_pass - include_uppercase_let - include_punctuation -
                                    vol_digits))
    if include_uppercase_let:  # Random selection of the numbers of uppercase letters in the password include other symbols
        vol_upper = randint(1, (len_pass - include_punctuation - vol_lowercase -
                                           vol_digits))
    if include_punctuation:   # Determining the numbeer of characters !#$%&*+-=?@^_ in the password include other symbols
        volume_punctuation = (len_pass - vol_digits - vol_lowercase - vol_upper)
    #  print(vol_digits, volume_lower_letters, vol_upper, volume_punctuation)
    # addition of the password length to the entered one if all 4 types of symbols are involved:
    if len_pass > vol_digits + vol_lowercase + vol_upper + volume_punctuation:
        vol_digits = (len_pass - vol_lowercase - vol_upper - volume_punctuation) * include_digits
        vol_lowercase = (len_pass - vol_digits - vol_upper - volume_punctuation) \
                        * include_lowercase_let
        vol_upper = (len_pass - vol_digits - vol_lowercase - volume_punctuation) \
                               * include_uppercase_let
        volume_punctuation = (len_pass - vol_digits - vol_lowercase - vol_upper) \
                             * include_punctuation
    n = vol_digits
    lists = digits
    chars_app(lists, n)  # Adding numbers to password
    n = vol_lowercase
    lists = lowercase_let
    chars_app(lists, n)  # Adding lowercase letters to password
    n = vol_upper
    lists = uppercase_let
    chars_app(lists, n)  # Adding uppercase letters to password
    n = volume_punctuation
    lists = punctuation
    chars_app(lists, n)  # Adding symbols to password
    shuffle(chars)  # Shuffle the list
    print(*chars, sep='')


for _ in range(num_pass):
    generate_password()
    chars = []