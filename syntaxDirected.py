import ply.lex as lex
import ply.yacc as yacc

# Token definitions for Zara language
tokens = (
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'ID', 'ASSIGN', 'IF', 'ELSE', 'WHILE',
    'GT', 'LT', 'GE', 'LE', 'EQ', 'NE'
)

# Token regular expressions
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'='
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_EQ = r'=='
t_NE = r'!='
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

# Intermediate code generator helpers
temp_count = 0
def new_temp():
    global temp_count
    temp_name = f't{temp_count}'
    temp_count += 1
    return temp_name

# Grammar rules with translation actions

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

# Assignment statement
def p_statement_assign(p):
    '''statement : ID ASSIGN expression'''
    p[0] = ('assign', p[1], p[3]['code'])
    print(f"{p[1]} = {p[3]['code']}")

# If-Else statement
def p_statement_if(p):
    '''statement : IF expression statement ELSE statement
                 | IF expression statement'''
    if len(p) == 6:
        p[0] = ('if_else', p[2]['code'], p[3], p[5])
    else:
        p[0] = ('if', p[2]['code'], p[3])

# While statement
def p_statement_while(p):
    '''statement : WHILE expression statement'''
    p[0] = ('while', p[2]['code'], p[3])

# Binary operations including comparison
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression GT expression
                  | expression LT expression
                  | expression GE expression
                  | expression LE expression
                  | expression EQ expression
                  | expression NE expression'''
    temp = new_temp()
    p[0] = {'code': temp}
    print(f"{temp} = {p[1]['code']} {p[2]} {p[3]['code']}")

# Grouped expressions
def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

# Number
def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = {'code': str(p[1])}

# Identifier
def p_expression_id(p):
    '''expression : ID'''
    p[0] = {'code': p[1]}

# Error rule for syntax errors
def p_error(p):
    print("Syntax error at '%s'" % p.value if p else "at end of input")

# Build the parser
parser = yacc.yacc()

# Examples of Zara programs
example_program1 = "x = 5\ny = x + 2\n"
example_program2 = "if x > 0 y = x + 1\n"
example_program3 = "while x > 0 x = x - 1\n"

# Function to test the parser
def test_parser(program):
    print("Testing Program:")
    print(program)
    result = parser.parse(program)
    if result:
        print("Parse Tree:", result)
    else:
        print("Parsing failed!")

# Run the parser on example programs
if __name__ == "__main__":
    test_parser(example_program1)
    print("\n")
    test_parser(example_program2)
    print("\n")
    test_parser(example_program3)
