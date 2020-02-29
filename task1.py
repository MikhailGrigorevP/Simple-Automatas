import generator
import re
import time


class RecognizerRE:
    __A = []
    __Over_A = dict()
    __result_file = 'Task1\\result.txt'
    __time_file = 'Task1\\time.txt'
    __overload_file = 'Task1\\overload.txt'
    __file = False

    def __init__(self, from_file=False, strings=None):
        self.__file = from_file
        if from_file:
            self.__f = open(self.__result_file, 'w')
            self.__strings = strings

    def __del__(self):
        if self.__file:
            self.__f.close()

    def check_strings_from_console(self):
        self.__Over_A.clear()
        working = True
        print('Input your line or "exit" to exit:')

        while working:
            user_string = input()
            if user_string == "exit":
                working = False
                break

                # проверка на соответсвие РВ
            rex = re.match(r'^(int|long|short)\s+([a-zA-Z][a-zA-Z0-9]{0,15})\s*\((\s*(int|long|short)'
                           r'\s+[a-zA-Z][a-zA-Z0-9]{0,15}\s*,?)*\)\s*;$', user_string)

            if rex is not None:
                print("- yes\n")
                result = rex.group(2)
                # добавляем её в массив
                if self.__Over_A.get(result) is None:
                    self.__Over_A.setdefault(result, 1)
                else:
                    self.__Over_A[result] += 1
            else:
                print("- no\n")

        print('Statistic: \n')
        for key in self.__Over_A:
            if self.__Over_A.get(key) > 1:
                print(str(key) + ' ' + str(self.__Over_A.get(key)) + '\n')

    def check_strings_from_file(self):
        self.__Over_A.clear()
        f_time = open(self.__time_file, 'w')
        f_time.write('iter time' + '\n')
        f_time = open(self.__time_file, 'a')
        start_time = time.perf_counter()
        count = 0
        for i in range(len(self.__strings) - 1):\

            # проверка на соответсвие РВ
            rex = re.match(r'^(int|long|short)\s+([a-zA-Z][a-zA-Z0-9]{0,15})\s*\((\s*(int|long|short)'
                           r'\s+[a-zA-Z][a-zA-Z0-9]{0,15}\s*,?)*\)\s*;$', self.__strings[i])

            if rex is not None:
                count += 1
                # запись в файл результатов проверки
                self.__f.write(self.__strings[i] + ' - yes' + '\n')
                # выхватываем название функции
                func_name = rex.group(2)
                # добавляем её в массив
                if self.__Over_A.get(func_name) is None:
                    self.__Over_A.setdefault(func_name, 1)
                else:
                    self.__Over_A[func_name] += 1
            else:
                self.__f.write(self.__strings[i] + ' - no' + '\n')
        f_time.write(str(time.perf_counter() - start_time) + '\n')
        f_time.close()
        print(count)

    def get_file_content(self):
        try:
            __f = open(self.__result_file)
        except IOError as e:
            self.check_strings_from_file()
            __f = open(self.__result_file)

        nf = __f.read()
        self.__A = nf.split('\n')

        __f.close()
        return self.__A

    def get_Over(self):
        return self.__Over_A

    def get_Time(self):
        return self.__time_file

    def analyze_overload(self):
        f_overload = open(self.__overload_file, 'w')
        for key in self.__Over_A:
            if self.__Over_A.get(key) > 1:
                f_overload.write(str(key) + ' ' + str(self.__Over_A.get(key)) + '\n')
        f_overload.close()


if __name__ == "__main__":

    dialog = True

    while dialog:
        dialog = False
        print('Hello, how do your want to input lines (file or console)')
        input_type = input()
        if input_type == "file":
            print("Input filename:")
            filename = input()
            all_strings = generator.Generator(1000000, filename).get_file_content()
            recognizer = RecognizerRE(True, all_strings)
            recognizer.check_strings_from_file()
            recognizer.analyze_overload()
            print("Data saved to files")
            print("Show statistic (yes to show):")
            input_show = input()
            if input_show == "yes":
                Over_A = recognizer.get_Over()
                for key in Over_A:
                    if Over_A.get(key) > 1:
                        print(str(key) + ' ' + str(Over_A.get(key)) + '\n')
                try:
                    f = open(recognizer.get_Time())
                    nf = f.read()
                    print("Time:", nf.split('\n')[1])

                    f.close()
                except IOError as e:
                    print("---- Error ----")

        elif input_type == "console":
            recognizer = RecognizerRE()
            recognizer.check_strings_from_console()
        else:
            print("You are wrong! Try again")
            dialog = True




