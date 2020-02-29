from collections import Counter
import string
import random


class Generator:
    # атрибуты класса


    # методы класса

    # создание методов класса
    def __init__(self, num=1000000, __input_file='functions'):

        # количество элементов
        self.__n = num
        self.__input_file = "Functions\\" + __input_file + ".txt"
        self.__A = []
        # файл со всеми строками функций
        try:
            self. __f = open(self.__input_file)
        except IOError as e:
            self.__f = open(self.__input_file, 'w')
            self.generate_file()

    def __del__(self):
        self.__f.close()

    def get_num(self):
        return self.__n

    def get_file_content(self):
        try:
            f = open(self.__input_file)
        except IOError as e:
            self.generate_file()
            f = open(self.__input_file)

        nf = f.read()
        self.__A = nf.split('\n')

        f.close()
        return self.__A

    # повредить
    def damage(self):
        return random.random()

    # генерировать тип
    def generate_type(self):
        type_name = ['int', 'short', 'long']
        func_type = type_name[random.randrange(3)]
        if self.damage() > 0.95:
            func_type = ''.join(random.choice(string.ascii_letters) for _ in range(4))
        else:
            func_type = type_name[random.randrange(3)]
        return func_type

    # генерировать имя функции
    def generate_func_name(self):
        func_name_length = random.randrange(15) + 1
        if self.damage() > 0.98:
            first_sym = random.choice(string.digits)
        else:
            first_sym = random.choice(string.ascii_letters)
        if self.damage() > 0.98:
            return first_sym +\
                ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(func_name_length))
        else:
            return first_sym +\
                ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation)
                        for _ in range(func_name_length))

    # генерировать список параметров
    def generate_options_list(self):
        generate_options_num = random.randrange(10)
        symbols = ['(', ')', ', ', ';', ' ']

        if self.damage() < 0.95:
            first_symbol = symbols[0]
            last_symbol = symbols[1]
        else:
            first_symbol = symbols[random.randrange(4)]
            last_symbol = symbols[random.randrange(4)]

        return first_symbol + \
            ''.join((self.generate_type() + ' ' + self.generate_func_name() +
                     ((', ' if (self.damage() < 0.80) else symbols[random.randrange(4)])
                      if (i < generate_options_num - 1) else '')) for i in range(generate_options_num)) +\
            ''.join(last_symbol)

    # генерировать строку
    def generate_string(self):
        symbols = ['(', ')', ',', ';', ' ']
        if self.damage() < 0.98:
            if self.damage() < 0.98:
                last_symbol = ';'
            else:
                last_symbol = ';'.join(random.choice(string.ascii_letters + string.digits + string.punctuation))
        else:
            last_symbol = symbols[random.randrange(4)]
        return ''.join(self.generate_type() + ' ' + self.generate_func_name() + ' ' + self.generate_options_list() + last_symbol)

    # генерировать файл
    def generate_file(self):
        for _ in range(self.__n):
            self.__f.write(self.generate_string() + '\n')


if __name__ == "__main__":

    Generator()


