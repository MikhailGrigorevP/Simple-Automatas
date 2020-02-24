import generator
import re
import time


class Recognizer:

    __A = []
    __Over_A = dict()
    __result_file = 'Output\\Task1\\result.txt'
    __time_file = 'Output\\Task1\\time.txt'
    __overload_file = 'Output\\Task1\\overload.txt'

    def __init__(self, strings):
        self.__f = open(self.__result_file, 'w')
        self.__strings = strings

    def __del__(self):
        self.__f.close()

    def check_strings(self):
        f_time = open(self.__time_file, 'w')
        f_time.write('iter time' + '\n')
        f_time = open(self.__time_file, 'a')
        start_time = time.perf_counter()
        count = 0
        for i in range(len(self.__strings) - 1):
            # проверка на соответсвие РВ
            if (re.fullmatch(r'((^(int|long|short))(\s+)(([a-z][0-9A-Za-z]{0,15})))((\s+)(\()((\s*)'
                                   r'(int|long|short)(\s+)([a-z][0-9A-Za-z]{0,15})((\,)?))*(\)))(\;$)',
                                   self.__strings[i])):
                count += 1
                # запись в файл результатов проверки
                self.__f.write(self.__strings[i] + ' - yes' + '\n')
                # выхватываем название функции
                result = re.findall(r'(([a-z][0-9A-Za-z]{0,15}))', self.__strings[i])[1][1]
                # добавляем её в массив
                if self.__Over_A.get(result) is None:
                    self.__Over_A.setdefault(result, 1)
                else:
                    self.__Over_A[result] += 1
            else:
                self.__f.write(self.__strings[i] + ' - no' + '\n')
        f_time.write(str(time.perf_counter() - start_time)+'\n')
        f_time.close()
        print(count)

    def get_file_content(self):
        try:
            __f = open(self.__result_file)
        except IOError as e:
            self.check_strings()
            __f = open(self.__result_file)

        nf = __f.read()
        self.__A = nf.split('\n')

        __f.close()
        return self.__A

    def analyze_overload(self):
        f_overload = open(self.__overload_file, 'w')
        for key in self.__Over_A:
            if self.__Over_A.get(key) > 1:
                f_overload.write(str(key) + ' ' + str(self.__Over_A.get(key)) + '\n')
        f_overload.close()


if __name__ == "__main__":

    all_strings = generator.Generator().get_file_content()
    recognizer = Recognizer(all_strings)

    recognizer.check_strings()
    recognizer.analyze_overload()

