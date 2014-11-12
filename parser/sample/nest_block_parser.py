'''
Created on Nov 12, 2014

@author: daineseh
'''
import logging

from lex_tokens import LexToken
from ply import yacc


class NestBlockParser(object):
    class NestBlockSyntaxError(Exception): pass

    def __init__(self, debug=False):
        if debug:
            self._log = logging.getLogger('PhysicalDivideCharParser')
        else:
            self._log = yacc.NullLogger()

        self._lex = LexToken(debug)
        self.tokens = self._lex.tokens

        self._parser = yacc.yacc(module=self, debug=debug, debuglog=self._log)

    def p_floating_point(self, p):
        'expression : sets'
#         print p[1]
        p[0] = p[1]

    def p_define(self, p):
        'define : def_head sets def_pat'
        p[0] = [(p[1], p[2])]

    def p_set0(self, p):
        'sets : sets define'
        if not p[1]:
            p[0] = [p[2]]
        else:
            p[1].append(p[2])
            p[0] = p[1]

    def p_sets1(self, p):
        'sets : sets set_stat'
        if not p[1]:
            p[0] = [p[2]]
        else:
            p[1].append(p[2])
            p[0] = p[1]

    def p_sets2(self, p):
        'sets : set_stat'
        p[0] = [p[1]]

    def p_sets3(self, p):
        'sets : define'
        p[0] = [p[1]]


    def p_set1(self, p):
        'set_stat : NAME NAME EQUAL value'
        p[0] = (p[2], p[4])

    def p_define_head(self, p):
        'def_head : NAME LBRACES NAME RBRACES L_BRACKET NAME R_BRACKET'
        p[0] = (p[3], p[6])

    def p_define_tail(self, p):
        'def_pat : NAME LBRACES NAME RBRACES'
        p[0] = p[3]

    def p_value1(self, p):
        'value : NUMBER'
        p[0] = str(p[1])

    def p_value2(self, p):
        'value : NAME'
        p[0] = p[1]

    def p_error(self, p):
        if p is None:  # End-of-file
            raise self.NestBlockSyntaxError('Parsing error (%s)' % self.__expr_text)
        err_msg = 'token type: {}, value: {}'.format(p.type, p.value)
        raise self.NestBlockSyntaxError(err_msg)

    def parse(self, s):
        self.__expr_text = s
        try:
            return self._parser.parse(s, lexer=self._lex.lexer())
        except self.NestBlockSyntaxError:
            print "NOT Matched"
            return None


if __name__ == '__main__':
    header_parser = NestBlockParser()

    data = '''
define{NAME}[ALIAS]
    set A = no 
    set B = no 
    set C = yes

    define{SUBNAME}[AliasSUB]
       set SUBA = yes
       set SUBB = 11
    end_define{SUBNAME}
end_define{NAME}
'''
    data = '''
set AAAAA = no
set BBBBB = yes
set CCCCC = test
    '''
    data = '''
define{NAME}[alias]
    define{SUB_A}[ALIAS_A]
        set B = C
    end_define{SUB_A}
    set ZZ = yes
    set XX = UCCU
    define{SUB_B}[ALIAS_B]
       set D = E
       define{SUB_C}[ALIAS_C]
          set ASDF =JKL
       end_define{SUB_C}
    end_define{SUB_B}
end_define{NAME}'''
    print header_parser.parse(data)
