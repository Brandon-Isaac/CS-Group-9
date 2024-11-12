import ply.lex as lex
import ply.yacc as yacc

# Token definitions for Zara language
tokens = (
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'ID', 'ASSIGN', 'EQUALS', 'IF', 'ELSE', 'WHILE'
)

# Token regular expressions
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'='
t_EQUALS = r'=='
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

# Number handling
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignore whitespace and newlines
t_ignore = ' \t'
t_ignore_NEWLINE = r'\n+'

# Error handling for invalid characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Parsing rules with precedence to handle ambiguity
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Grammar rules

# Program
def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])

# Statement List
def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

# Statements
def p_statement_assign(p):
    '''statement : ID ASSIGN expression'''
    p[0] = ('assign', p[1], p[3])

def p_statement_if(p):
    '''statement : IF condition statement ELSE statement
                 | IF condition statement'''
    if len(p) == 6:
        p[0] = ('if_else', p[2], p[3], p[5])
    else:
        p[0] = ('if', p[2], p[3])

def p_statement_while(p):
    '''statement : WHILE condition statement'''
    p[0] = ('while', p[2], p[3])

# Condition rule
def p_condition(p):
    '''condition : expression EQUALS expression'''
    p[0] = ('equals', p[1], p[3])

# Expression rules
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = ('number', p[1])

def p_expression_id(p):
    '''expression : ID'''
    p[0] = ('id', p[1])

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' (line: {p.lineno})")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Updated Zara program to test
example_program = "x = 5\ny = x + 2\n"

# Function to test the parser
def test_parser(program):
    result = parser.parse(program)
    if result:
        print("Parse Tree:", result)
    else:
        print("Parsing failed!")

# Run the parser on the example program
if __name__ == "__main__":
    test_parser(example_program)
