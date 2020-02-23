import generator
import re
import time

class Recognizer:

    __A = []
    __Over_A = []

    def __init__(self, strings):
        self.__f = open('result1.txt', 'w')
        self.__strings = strings

    def __del__(self):
        self.__f.close()

    def check_strings(self):
        f_time = open('time1.txt', 'w')
        f_time.write('iter time' + '\n')
        f_time = open('time1.txt', 'a')
        start_time = time.perf_counter()
        for i in range(len(self.__strings) - 1):
            # проверка на соответсвие РВ
            if (re.match(r'((^(int|long|short))(\s+)(([^0-9]{1}[0-9a-zA-Z]{0,15})))((\s+)(\()((\s*)'
                                   r'(int|long|short)(\s+)([^0-9]{1}[0-9a-zA-Z]{0,15})((\,)?))*(\)))(\;$)',
                                   self.__strings[i])):
                # запись в файл результатов проверки
                self.__f.write(self.__strings[i] + ' - yes' + '\n')
                # выхватываем название функции
                result = re.findall(r'(([^0-9]{1}[0-9a-zA-Z]{0,15}))', self.__strings[i])[1][1]
                # добавляем её в массив
                self.__Over_A.append(result)
            else:
                self.__f.write(self.__strings[i] + ' - no' + '\n')
        f_time.write(str(i) + ' ' + str(time.perf_counter() - start_time)+'\n')
        f_time.close()

    def get_file_content(self):
        try:
            self.__f = open('result1.txt')
        except IOError as e:
            self.check_strings()
            self.__f = open('result1.txt')

        nf = self.__f.read()
        self.__A = nf.split('\n')

        self.__f.close()
        return self.__A

    def analyze_overload(self):
        counter_one = generator.Counter(self.__Over_A )
        f_overload = open('overload.txt', 'w')
        for item, count in counter_one.items():
            if count > 1:
                f_overload.write(str(item) + ' - ' + str(count) + '\n')
        f_overload.close()


if __name__ == "__main__":

    all_strings = generator.Generator().get_file_content()
    recognizer = Recognizer(all_strings)

    recognizer.check_strings()
    A = recognizer.get_file_content()
    recognizer.analyze_overload()

