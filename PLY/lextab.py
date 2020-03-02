# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('ANY', 'FUNCNAME', 'FUNCTYPE', 'NL', 'PARAMETRS'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive', 'name': 'exclusive', 'tail': 'exclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_FUNCTYPE>(?m)^(int|long|short)\\s+)|(?P<t_NL>(\\n))|(?P<t_ANY>(.))', [None, ('t_FUNCTYPE', 'FUNCTYPE'), None, ('t_NL', 'NL'), None, (None, 'ANY')])], 'name': [('(?P<t_name_FUNCNAME>[a-zA-Z][a-zA-Z0-9]{0,15})|(?P<t_name_ANY>(.))|(?P<t_name_NL>(\\n))', [None, ('t_name_FUNCNAME', 'FUNCNAME'), ('t_name_ANY', 'ANY'), None, ('t_name_NL', 'NL')])], 'tail': [('(?P<t_tail_PARAMETRS>\\s*\\((\\s*(int|long|short)(\\s+[a-zA-Z][a-zA-Z0-9]{0,15})?\\s*,?)*\\)\\s*;)|(?P<t_tail_ANY>.)|(?P<t_tail_NL>(\\n))', [None, ('t_tail_PARAMETRS', 'PARAMETRS'), None, None, None, ('t_tail_ANY', 'ANY'), ('t_tail_NL', 'NL')])]}
_lexstateignore = {'INITIAL': '', 'name': '', 'tail': ''}
_lexstateerrorf = {'INITIAL': 't_error', 'name': 't_name_error', 'tail': 't_tail_error'}
_lexstateeoff = {}
