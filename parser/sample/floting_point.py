import logging

from lex_tokens import LexToken
from ply.yacc import yacc


class FloatingPointParser(object):
    class FloatingPointSyntaxError(Exception): pass

    def __init__(self, debug=False):
        if debug:
            self._log = logging.getLogger('PhysicalDivideCharParser')
        else:
            self._log = yacc.NullLogger()

        self._lex = LexToken(debug)
        self.tokens = self._lex.tokens

        self._parser = yacc.yacc(module=self, debug=debug, debuglog=self._log)

    def p_floating_point(self, p):
        'expression : floating'
        p[0] = p[1]

    def p_floating_1(self, p):
        'floating : single_num DOT single_num'
        p[0] = p[1] + p[2] + p[3]

    def p_floating_2(self, p):
        'floating : single_num dot_char single_num'
        p[0] = p[1] + p[2] + p[3]

    def p_floating_3(self, p):
        'floating : single_num'
        p[0] = p[1]

    def p_divid_dot(self, p):
        'dot_char : DOT'
        p[0] = p[1]

    def p_sign1(self, p):
        'single_num : NUMBER'
        p[0] = str(p[1])

    def p_sign2(self, p):
        'single_num : MINUS NUMBER'
        p[0] = p[1] + str(p[2])

    def p_error(self, p):
        if p is None:  # End-of-file
            raise self.FloatingPointSyntaxError('Parsing error (%s)' % self.__expr_text)
        err_msg = 'token type: {}, value: {}'.format(p.type, p.value)
        raise self.FloatingPointSyntaxError(err_msg)

    def parse(self, s):
        self.__expr_text = s
        try:
            return self._parser.parse(s, lexer=self._lex.lexer())
        except self.FloatingPointSyntaxError:
            print "NOT Matched"
            return None


if __name__ == '__main__':
    header_parser = FloatingPointParser()

    data = '5.6'
    data = '- 5.6'
    data = 'VERSION 5.6 ;'
    data = '5'
    data = '-5'
    print header_parser.parse(data)


