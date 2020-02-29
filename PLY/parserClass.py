from PLY.lexerClass import MyLexer
import ply.yacc as yacc

class MyParser(object):

    tokens = MyLexer.tokens
    __Over_A = dict()
    __A = []
    __overload_file = '..\\Task3\\overload.txt'
    __result_file = '..\\Task3\\result.txt'
    count = 0

    def get_A(self):
        return self.__Over_A

    def __init__(self, from_file=False):
        self.__file = from_file
        self.lexer = MyLexer()
        self.parser = yacc.yacc(module=self)
        if from_file:
            self.__f = open(self.__result_file, 'w')

    def __del__(self):
        if self.__file:
            self.__f.close()

    def check_string(self, code):
        result = self.parser.parse(code)
        print(self.count)
        return result

    def p_func_list(self, p):
        '''func_list : func
        | func_list func '''
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 3:
            p[0] = p[1] + p[2]

    def p_func(self, p):
        '''func : FUNCTYPE FUNCNAME PARAMETRS'''
        if self.__file:
            self.__f.write(p[1] + p[2] + p[3] + ' - yes\n')
        if self.__Over_A.get(p[2]) is None:
            self.__Over_A.setdefault(p[2], 1)
        else:
            self.__Over_A[p[2]] += 1
        self.count += 1
        p[0] = p[1] + p[2] + p[3] + ' - yes\n'

    def p_func_first_err_type(self, p):
        'func : FUNCTYPE err_list'
        if self.__file:
            self.__f.write(p[1] + p[2] + ' - no\n')
        p[0] = p[1] + p[2] + ' - no\n'

    def p_func_second_err_type(self, p):
        'func : FUNCTYPE FUNCNAME err_list'
        if self.__file:
            self.__f.write(p[1] + p[2] + p[3] +' - no\n')
        p[0] = p[1] + p[2] + p[3] + ' - no\n'

    def p_func_forth_err_type(self, p):
        'func : FUNCTYPE FUNCNAME PARAMETRS err_list'
        if self.__file:
            self.__f.write(p[1] + p[2] + p[3] + p[4] + ' - no\n')
        p[0] = p[1] + p[2] + p[3] + p[4] + ' - no\n'

    def p_err_list(self, p):
        '''err_list :
        | err
        | err_list err'''
        if len(p) == 1:
            p[0] = ""
        elif len(p) == 2:
            p[0] = p[1]
        elif len(p) == 3:
            p[0] = p[1] + p[2]

    def p_err(self, p):
        '''err : ANY'''
        if len(p) == 2:
            p[0] = p[1]

    # system
    def p_error(self, p):
        print('Unexpected token:', p)



if __name__ == "__main__":
    f = open("..\\Functions\\sample.txt")
    nf = f.read()
    f.close()
    parser = MyParser()
    print(parser.check_string(nf))
