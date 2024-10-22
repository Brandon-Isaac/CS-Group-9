from zara_lexer import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

def p_program(p):
    '''program : statement_list'''
    p[0] = ("program", p[1])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : expression_statement
                 | conditional_statement
                 | loop_statement'''
    p[0] = p[1]

def p_expression_statement(p):
    '''expression_statement : ID ASSIGN expression
                            | expression'''
    if len(p) == 4:
        p[0] = ('assign', p[1], p[3])
    else:
        p[0] = p[1]

def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression LT expression
                  | LPAREN expression RPAREN
                  | NUMBER
                  | ID'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    elif len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_conditional_statement(p):
    '''conditional_statement : IF expression THEN statement_list ELSE statement_list END'''
    p[0] = ('if', p[2], p[4], p[6])

def p_loop_statement(p):
    '''loop_statement : WHILE expression DO statement_list END'''
    p[0] = ('while', p[2], p[4])

def p_error(p):
    print("Syntax error in input!")

import ply.yacc as yacc
parser = yacc.yacc()

# Tests
test1 = "3 + 4 * 5"
test2 = "IF x THEN x = x + 1 ELSE x = x - 1 END"
test3 = "WHILE x < 10 DO x = x + 1 END"

print(parser.parse(test1))
print(parser.parse(test2))
print(parser.parse(test3))

