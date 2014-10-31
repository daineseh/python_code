import logging
import ply.lex as lex

# # Set up a logging object
# logging.basicConfig(
#     level=logging.DEBUG,
#     filename="parselog.txt",
#     filemode="w",
#     format="%(filename)10s:%(lineno)4d:%(message)s"
# )

class LexToken(object):
    class LexTokenError(Exception): pass

    def __init__(self, debug=False):
        if debug:
            self._log = logging.getLogger('vlog_lex')
        else:
            self._log = lex.NullLogger()

        # List of token names.   This is always required
        self.tokens = (
           'NUMBER',
           'PLUS',
           'MINUS',
#            'TIMES',
           'DIVIDE',
           'L_PAREN',
           'R_PAREN',
           'NAME',
           'SEMI',
           'DOT',
#            'Q_MARK',
#            'L_BRACKET',
#            'R_BRACKET',
        )

        # Regular expression rules for simple tokens
        self.t_ignore_COMMENT = r'\#.*'
        self.t_SEMI = r';'
        self.t_PLUS = r'\+'
        self.t_MINUS = r'-'
#         self.t_TIMES = r'\*'
        self.t_DIVIDE = r'/'
        self.t_L_PAREN = r'\('
        self.t_R_PAREN = r'\)'
        self.t_DOT = r'\.'
#         self.t_Q_MARK = r'\"'
#         self.t_L_BRACKET = r'\['
#         self.t_R_BRACKET = r'\]'

        # A string containing ignored characters (spaces and tabs)
        self.t_ignore = ' \t'

        # Build the lexer
        self._lexer = lex.lex(module=self, debug=debug, debuglog=self._log)

    def t_NAME(self, t):
        # r'[A-Za-z_][\w_]*'
        r'[A-Za-z_][\w]*'
        return t

    # A regular expression rule with some action code
    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Error handling rule
    def t_error(self, t):
        print "Illegal character '%s'" % t.value[0]
        t.lexer.skip(1)

    def lexer(self):
        return self._lexer

if __name__ == '__main__':
    data = '''AA ;
    BB ;
    //
    '''

    lex_obj = LexToken()
    lexer = lex_obj.lexer()
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: break  # No more input
        print tok
