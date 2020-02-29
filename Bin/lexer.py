# coding=utf8
import ply.lex as lex
from ply.lex import TOKEN
import re

states = (
    ('name', 'exclusive'),
    ('tail', 'exclusive'),
)

tokens = (
    'FUNCTYPE', 'ANY', 'FUNCNAME', 'PARAMETRS',
)

t_ANY = r'.'


def t_FUNCTYPE(t):
    r'(?m)^(int|long|short)\s+'
    if t.lexer.current_state() == 'name':
        t.lexer.begin('tail')  # переходим в начальное состояние
    else:
        t.lexer.begin('name')  # парсим строку
    return t


def t_name_FUNCNAME(t):
    r'[a-zA-Z][a-zA-Z0-9]{0,15}'
    if t.lexer.current_state() == 'tail':
        t.lexer.begin('INITIAL')  # переходим в начальное состояние
    else:
        t.lexer.begin('tail')  # парсим строку
    return t


def t_name_ANY(t):
    r'.'
    t.lexer.begin('INITIAL')  # переходим в начальное состояние


def t_tail_PARAMETRS(t):
    r'\s*\((\s*(int|long|short)\s+[a-zA-Z][a-zA-Z0-9]{0,15}\s*,?)*\)\s*;'
    t.lexer.begin('INITIAL')  # переходим в начальное состояние
    return t


def t_tail_ANY(t):
    r'.'
    t.lexer.begin('INITIAL')  # переходим в начальное состояние


# говорим что ничего не будем игнорировать
t_name_ignore = ' '  # это кстати обязательная переменная, без неё нельзя создать новый state
t_tail_ignore = ' '  # это кстати обязательная переменная, без неё нельзя создать новый state
t_ignore = ' \r\t\f'


# ну и куда же мы без обработки ошибок
def t_name_error(t):
    print("Illegal character in NAME '%s'" % t.value[0])
    t.lexer.skip(1)
    t.lexer.begin('INITIAL')


# а здесь мы обрабатываем ошибки. Кстати заметьте формат названия функции
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    t.lexer.begin('INITIAL')


# а здесь мы обрабатываем ошибки. Кстати заметьте формат названия функции
def t_tail_error(t):
    print("Illegal character in TAIL'%s'" % t.value[0])
    t.lexer.skip(1)
    t.lexer.begin('INITIAL')


def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)
    t.lexer.begin('INITIAL')


lexer = lex.lex()

if __name__ == "__main__":

    f = open("../Functions/sample.txt")
    nf = f.read()
    f.close()
    lexer.input(nf)

    while True:
        tok = lexer.token()  # читаем следующий токен
        if not tok:
            break
        if tok.type == "FUNCTYPE":
            print('\n')

        print(tok.type, tok.value)
