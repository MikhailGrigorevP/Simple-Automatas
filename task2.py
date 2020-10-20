import generator
import re
import time
from SMC import AppClass


class RecognizerSMC:

    __A = []
    __Over_A = dict()
    __result_file = 'Task2\\result.txt'
    __time_file = 'Task2\\time.txt'
    __overload_file = 'Task2\\overload.txt'
    __file = False

    def __init__(self, from_file=False, strings=None):
        self.__file = from_file
        self.__smc = AppClass.AppClass()
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
            res = self.__smc.CheckString(user_string)

            if res is not None:
                print("- yes\n")
                result = res
                # добавляем её в массив
                if self.__Over_A.get(res) is None:
                    self.__Over_A.setdefault(res, 1)
                else:
                    self.__Over_A[res] += 1
            else:
                print("- no\n")

        print('Statistic: \n')
        for k in self.__Over_A:
            if self.__Over_A.get(k) > 1:
                print(str(k) + ' ' + str(self.__Over_A.get(k)) + '\n')

    def check_strings_from_file(self):
        f_time = open(self.__time_file, 'w')
        f_time.write('iter time' + '\n')
        f_time = open(self.__time_file, 'a')
        start_time = time.perf_counter()
        count = 0
        for i in range(len(self.__strings) - 1):
            res = self.__smc.CheckString(self.__strings[i])
            if res is None:
                self.__f.write(self.__strings[i] + ' - no' + '\n')
            else:
                count += 1
                self.__f.write(self.__strings[i] + ' - yes' + '\n')
                if self.__Over_A.get(res) is None:
                    self.__Over_A.setdefault(res, 1)
                else:
                    self.__Over_A[res] += 1
        f_time.write(str(time.perf_counter() - start_time)+'\n')
        f_time.close()
        print(count)

    def get_Over(self):
        return self.__Over_A

    def get_Time(self):
        return self.__time_file

    def get_file_content(self):
        try:
            self.__f = open(self.__result_file)
        except IOError as e:
            self.check_strings_from_file()
            self.__f = open(self.__result_file)

        nf = self.__f.read()
        self.__A = nf.split('\n')

        self.__f.close()
        return self.__A

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
            recognizer = RecognizerSMC(True, all_strings)
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
            recognizer = RecognizerSMC()
            recognizer.check_strings_from_console()
        else:
            print("You are wrong! Try again")
            dialog = True




