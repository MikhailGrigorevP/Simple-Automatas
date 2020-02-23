import generator
import re
import time
import AppClass

if __name__ == "__main__":

	smc = AppClass.AppClass()

	str = "int my"
	if not smc.CheckString(str):
		result = "not acceptable"
	else:
		result = "acceptable"
	print('The string "%s" is %s.\n' % (str, result))


	str = "int my;"
	if not smc.CheckString(str):
		result = "not acceptable"
	else:
		result = "acceptable"
	print('The string "%s" is %s.\n' % (str, result))


	str = "int my"
	if not smc.CheckString(str):
		result = "not acceptable"
	else:
		result = "acceptable"
	print('The string "%s" is %s.\n' % (str, result))



	str = "int myаааааааааааааааа"
	if not smc.CheckString(str):
		result = "not acceptable"
	else:
		result = "acceptable"
	print('The string "%s" is %s.\n' % (str, result))


	str = "ift myа"
	if not smc.CheckString(str):
		result = "not acceptable"
	else:
		result = "acceptable"
	print('The string "%s" is %s.\n' % (str, result))

	str = "inthjg myа"
	if not smc.CheckString(str):
		result = "not acceptable"
	else:
		result = "acceptable"
	print('The string "%s" is %s.\n' % (str, result))

