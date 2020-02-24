import generator
import re
import time
import AppClass


class Recognizer:

	__A = []
	__Over_A = dict()
	__result_file = 'Output\\Task2\\result.txt'
	__time_file = 'Output\\Task2\\time.txt'
	__overload_file = 'Output\\Task2\\overload.txt'

	def __init__(self, strings):
		self.__f = open(self.__result_file, 'w')
		self.__smc = AppClass.AppClass()
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
			res = self.__smc.CheckString(self.__strings[i])
			if not res[0]:
				self.__f.write(self.__strings[i] + ' - no' + '\n')
			else:
				count += 1
				self.__f.write(self.__strings[i] + ' - yes' + '\n')
				if self.__Over_A.get(res[1]) is None:
					self.__Over_A.setdefault(res[1], 1)
				else:
					self.__Over_A[res[1]] += 1
		f_time.write(str(time.perf_counter() - start_time)+'\n')
		f_time.close()
		print(count)

	def get_file_content(self):
		try:
			self.__f = open(self.__result_file)
		except IOError as e:
			self.check_strings()
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

	all_strings = generator.Generator().get_file_content()
	recognizer = Recognizer(all_strings)

	recognizer.check_strings()
	recognizer.analyze_overload()



