from SMC import AppClass_sm


class AppClass:

	def __init__(self):
		self.__counter = 0;
		self.__substring = ''
		self.__name = ''
		self._fsm = AppClass_sm.AppClass_sm(self)
		self._is_acceptable = False
		self._fsm.enterStartState()

		# Uncomment to see debug output.
		# self._fsm.setDebugFlag(True)

	def ClearSMC(self):
		self.__substring = ''
		self.CounterZero()
		self.clearSubstring()
		self._is_acceptable = True

	def CheckString(self, string):
		self._fsm.Type()
		for c in string:
			# break
			if not self._is_acceptable:
				break
			if c.isalpha():
				self.__substring += c
				self._fsm.Alpha()
			elif c.isdigit():
				self.__substring += c
				self._fsm.Digit()
			elif c == ',':
				self._fsm.Comma()
			elif c == '(':
				self._fsm.OpenBracket()
			elif c == ')':
				self._fsm.CloseBracket()
			elif c == ' ':
				self._fsm.WhiteSpace()
			elif c == ';':
				self._fsm.Semicolon()
			else:
				self._fsm.Unknown()
		self._fsm.EOS()
		if self._is_acceptable:
			return self.__name
		else:
			return None

	def Acceptable(self):
		self._is_acceptable = True

	def Unacceptable(self):
		self._is_acceptable = False

	def CounterInc(self):
		self.__counter += 1

	def CounterZero(self):
		self.__counter = 0

	def isValidType(self):
		return self.__counter <= 5

	def isValidName(self):
		return self.__counter < 16

	def checkType(self):
		return self.__substring == "int" or self.__substring == "short" or self.__substring == "long"

	def clearSubstring(self):
		self.__substring = ''

	def set_name(self):
		self.__name = self.__substring


