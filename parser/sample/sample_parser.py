import logging

from lex_tokens import LexToken
import ply.yacc as yacc


class Parser(object):
    class ParserSyntaxError(Exception): pass

    def __init__(self, debug=False):
        if debug:
            self._log = logging.getLogger('Parser')
        else:
            self._log = yacc.NullLogger()

        self._lex = LexToken(debug)
        self.tokens = self._lex.tokens

        self._parser = yacc.yacc(module=self, debug=debug, debuglog=self._log)

    def p_expression(self, p):
        "statement : MINUS instance_token module_token components SEMI"
        self._struct.setdefault('mem_data', (p[2], p[3]))
        p[0] = self._struct

    def p_instance_token(self, p):
        "instance_token : instance"
        p[0] = p[1]

    def p_instance_full(self, p):
        "instance : instance divide_char express_name"
        p[0] = p[1] + p[2] + p[3]

    def p_instance_signle(self, p):
        "instance : express_name"
        p[0] = p[1]

    def p_module_token(self, p):
        "module_token : express_name"
        p[0] = p[1]

    def p_components_1(self, p):
        'components : components component'

    def p_components_2(self, p):
        'components : component'

    def p_component_1(self, p):
        'component : token_name express_name'
        self._struct.setdefault(p[1], p[2])

    def p_component_2(self, p):
        'component : token_name L_PAREN NUMBER NUMBER R_PAREN NAME'
        self._struct.setdefault(p[1], (p[3], p[4], p[6]))
        p[0] = p[1] + p[2] + str(p[3]) + str(p[4]) + p[5] + p[6]

    def p_component_3(self, p):
        'component : token_name NUMBER NUMBER NUMBER NUMBER'
        self._struct.setdefault(p[1], (p[2], p[3], p[4], p[5]))
        p[0] = p[1] + str(p[2]) + str(p[3]) + str(p[4]) + str(p[5])

    def p_component_4(self, p):
        'component : token_name NUMBER express_name express_name'
        self._struct.setdefault(p[1], (p[2], p[3], p[4]))
        p[0] = p[1] + str(p[2]) + p[3] + p[4]

    def p_component_5(self, p):
        'component : token_name NUMBER'
        self._struct.setdefault(p[1], p[2])
        p[0] = p[1] + str(p[2])

    def p_component_6(self, p):
        'component : token_name'
        if p[1] == 'UNPLACED':
            self._struct.setdefault(p[1], (0, 0, ''))
        p[0] = p[1]

    def p_expression_token(self, p):
        'token_name : PLUS express_name'
        p[0] = p[2]

    def p_expression_name(self, p):
        'express_name : NAME'
        p[0] = p[1]

    def p_char_divide(self, p):
        'divide_char : DIVIDE'
        p[0] = p[1]

    def p_char_dot(self, p):
        'divide_char : DOT'

    def p_error(self, p):
        if p is None:  # End-of-file
            raise self.PhysicalInstanceSyntaxError('Parsing error (%s)' % self.__expr_text)
        err_msg = 'token type: {}, value: {}'.format(p.type, p.value)
        raise self.PhysicalInstanceSyntaxError(err_msg)

    def parse(self, s):
        self._struct = {}
        self.__expr_text = s
        try:
            return self._parser.parse(s, lexer=self._lex.lexer())
        except self.PhysicalInstanceSyntaxError:
            return None


if __name__ == '__main__':
    inst_parser = Parser()
    data = '''- AAA_a/bbbbbbb_ccc_1_d/E_0/F_0/G_0/H_0/I_5/J_1/K_3/L_0/M_1 ABCDEFGHIJKL 
    + FOX ( 987654 123456 ) XZ 
    ;'''
    print inst_parser.parse(data)
