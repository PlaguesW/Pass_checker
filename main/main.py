digits = [c for c in '0123456789']
lower_letters = [c for c in 'abcdefghijklmnopqrstuvwxyz']
upper_letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
punctuation = [c for c in '!#$%&*+-=?@^_']
num_pass, chars = input('Введите количество паролей для генерации: '), []
while 1:  # Check of correct numbers of passwords
    if not str(num_pass).isdigit() or int(num_pass) < 0:
        print('Пожалуйста, введите натуральное число: ')
        num_pass = input()
    else:
        num_pass = int(num_pass)
        break
from random import *

len_pass = input(
    'Введите длину одного пароля. Пароль должен содержать не менее 8 символов: ')
while 1:  # Check of correct lenght of passwords
    if not str(len_pass).isdigit() or int(len_pass) < 7:
        print('Пожалуйста, введите натуральное число больше 7')
        len_pass = input()
    else:
        len_pass = int(len_pass)
        break


def valid_1_0():  # Check of correctness input 1 or 0
    while 1:
        ans = input()
        if ans not in str(10):
            print('Пожалуйста, введите 1 или 0')
        else:
            return int(ans)


print('Включать ли цифры 0123456789? Да - введите 1, нет - 0.')
include_digits = valid_1_0()
print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? Да - введите 1, нет - 0')
with_lower_letters = valid_1_0()
print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? Да - введите 1, нет - 0')
with_upper_letters = valid_1_0()
print('Включать ли символы!#$%&*+-=?@^_? Да - введите 1, нет - 0')
with_punctuation = valid_1_0()
print('Исключать ли неоднозначные символы il1Lo0O? Да - введите 1, нет - введите 0.')
exclude = valid_1_0()
if exclude:  # avoiding of ambiguous characters
    digits.remove('0')
    digits.remove('1')
    lower_letters.remove('i')
    lower_letters.remove('l')
    lower_letters.remove('o')
    upper_letters.remove('L')
    upper_letters.remove('O')


def chars_app(lists, n):  # Adding characters to the password
    if n > 0:
        for _ in range(n):
            chars.append(choice(lists))
    return chars


def generate_password():
    volume_digits = volume_lower_letters = volume_upper_letters = volume_punctuation = 0
    if include_digits:  # случайный выбор количества цифр в пароле с учетом остальных символов
        volume_digits = randint(1, (len_pass - with_lower_letters - with_upper_letters -
                                    with_punctuation))
    if with_lower_letters:  # случайный выбор количества строчных букв в пароле с учетом остальных символов
        volume_lower_letters = randint(1, (len_pass - with_upper_letters - with_punctuation -
                                           volume_digits))
    if with_upper_letters:  # случайный выбор количества прописных букв в пароле с учетом остальных символов
        volume_upper_letters = randint(1, (len_pass - with_punctuation - volume_lower_letters -
                                           volume_digits))
    if with_punctuation:   # определение количества знаков !#$%&*+-=?@^_ в пароле с учетом остальных символов
        volume_punctuation = (len_pass - volume_digits - volume_lower_letters - volume_upper_letters)
    #  print(volume_digits, volume_lower_letters, volume_upper_letters, volume_punctuation)
    # дополнение длины пароля до введенной, если задействованы не все 4 вида символов:
    if len_pass > volume_digits + volume_lower_letters + volume_upper_letters + volume_punctuation:
        volume_digits = (len_pass - volume_lower_letters - volume_upper_letters - volume_punctuation) * include_digits
        volume_lower_letters = (len_pass - volume_digits - volume_upper_letters - volume_punctuation) \
                               * with_lower_letters
        volume_upper_letters = (len_pass - volume_digits - volume_lower_letters - volume_punctuation) \
                               * with_upper_letters
        volume_punctuation = (len_pass - volume_digits - volume_lower_letters - volume_upper_letters) \
                             * with_punctuation
    n = volume_digits
    lists = digits
    chars_app(lists, n)  # добавление в пароль цифр
    n = volume_lower_letters
    lists = lower_letters
    chars_app(lists, n)  # добавление в пароль строчных букв
    n = volume_upper_letters
    lists = upper_letters
    chars_app(lists, n)  # добавление в пароль прописных букв
    n = volume_punctuation
    lists = punctuation
    chars_app(lists, n)  # добавление в пароль символов
    shuffle(chars)  # перемешиваем список
    print(*chars, sep='')


for _ in range(num_pass):
    generate_password()
    chars = []