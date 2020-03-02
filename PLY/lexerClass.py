# coding=utf8
import ply.lex as lex
from ply.lex import TOKEN
import re


class MyLexer(object):
    states = (
        ('name', 'exclusive'),
        ('tail', 'exclusive'),
    )

    tokens = (
        'FUNCTYPE', 'ANY', 'NL', 'FUNCNAME', 'PARAMETRS',
    )

    t_ANY = r'(.)'

    def t_FUNCTYPE(self, t):
        r'(?m)^(int|long|short)\s+'
        if t.lexer.current_state() == 'name':
            t.lexer.begin('tail')
        else:
            t.lexer.begin('name')
        return t

    def t_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        return t

    def t_name_FUNCNAME(self, t):
        r'[a-zA-Z][a-zA-Z0-9]{0,15}'
        if t.lexer.current_state() == 'tail':
            t.lexer.begin('INITIAL')
        else:
            t.lexer.begin('tail')
        return t

    def t_name_ANY(self, t):
        r'(.)'
        t.lexer.begin('INITIAL')
        return t

    def t_name_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_tail_PARAMETRS(self, t):
        r'\s*\((\s*(int|long|short)(\s+[a-zA-Z][a-zA-Z0-9]{0,15})?\s*,?)*\)\s*;'
        t.lexer.begin('INITIAL')
        return t

    def t_tail_ANY(self, t):
        r'.'
        t.lexer.begin('INITIAL')
        return t

    def t_tail_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    t_name_ignore = ''
    t_tail_ignore = ''
    t_ignore = ''

    # ну и куда же мы без обработки ошибок
    def t_name_error(self, t):
        print("Illegal character in NAME '%s'" % t.value[0])
        # t.lexer.skip(1)
        t.lexer.begin('INITIAL')

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        # t.lexer.skip(1)
        t.lexer.begin('INITIAL')

    def t_tail_error(self, t):
        print("Illegal character in TAIL'%s'" % t.value[0])
        # t.lexer.skip(1)
        t.lexer.begin('INITIAL')

    def input(self, data):
        return self.lexer.input(data)

    def token(self):
        return self.lexer.token()

    def __init__(self):
        # Build the lexer
        self.lexer = lex.lex(module=self, optimize=True)


if __name__ == "__main__":

    f = open("..\\Functions\\sample.txt")
    nf = f.read()
    f.close()
    lexer = MyLexer()
    lexer.input(nf)
    while True:
        tok = lexer.token()  # читаем следующий токен
        if not tok:
            break
        if tok.type == "FUNCTYPE":
            print('\n')

        print(tok.type, tok.value)
