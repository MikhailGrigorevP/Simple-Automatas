import ply.yacc as yacc


def check_string(code):
    return parser.parse(code)


def p_func_list(p):
    '''func_list : func
    | func_list func '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1] + p[2]


def p_func(p):
    '''func : FUNCTYPE FUNCNAME PARAMETRS'''
    # __f = open(__result_file, 'a')
    # __f.write(p[1] + p[2] + p[3] + ' - yes\n')
    # __f.close()
    p[0] = p[1] + p[2] + p[3] + ' - yes\n'

def p_func_first_err_type(p):
    'func : FUNCTYPE err_list'
    p[0] = p[1] + p[2]  + ' - no\n'


def p_func_second_err_type(p):
    'func : FUNCTYPE FUNCNAME err_list'
    p[0] = p[1] + p[2] + p[3] + ' - no\n'


def p_func_forth_err_type(p):
    'func : FUNCTYPE FUNCNAME PARAMETRS err_list'
    p[0] = p[1] + p[2] + p[3] + p[4] + ' - no\n'


def p_err_list(p):
    '''err_list : err
    | err_list err'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1] + p[2]


def p_err(p):
    'err : ANY'
    p[0] = p[1]


# system
def p_error(p):
    print('Unexpected token:', p)


parser = yacc.yacc()


if __name__ == "__main__":
    f = open("../Functions/functions.txt")
    nf = f.read()
    f.close()
    print(parser.parse(nf))
