from zara_lexer import tokens
import ply.yacc as yacc

# Intermediate code generation
temp_count = 0

def new_temp():
    global temp_count
    temp = f"t{temp_count}"
    temp_count += 1
    return temp

# Parser rules with translation actions
def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

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
    '''expression_statement : ID ASSIGN expression SEMICOLON'''
    print(f"{p[1]} = {p[3]}")

def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression LT expression
                  | LPAREN expression RPAREN
                  | NUMBER
                  | ID'''
    if len(p) == 4:  # Binary operations
        temp = new_temp()
        print(f"{temp} = {p[1]} {p[2]} {p[3]}")
        p[0] = temp
    elif len(p) == 3:  # Parenthesized expression
        p[0] = p[2]
    else:  # Single NUMBER or ID
        p[0] = p[1]

def p_conditional_statement(p):
    '''conditional_statement : IF expression THEN statement_list ELSE statement_list END'''
    print(f"IF {p[2]} GOTO L1")
    print(f"GOTO L2")
    print(f"L1:")
    for stmt in p[4]:
        print(stmt)
    print(f"GOTO L3")
    print(f"L2:")
    for stmt in p[6]:
        print(stmt)
    print(f"L3:")

def p_loop_statement(p):
    '''loop_statement : WHILE expression DO statement_list END'''
    print(f"L0:")
    print(f"IF {p[2]} GOTO L1")
    print(f"GOTO L2")
    print(f"L1:")
    for stmt in p[4]:
        print(stmt)
    print(f"GOTO L0")
    print(f"L2:")

def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

# Example test code
test_code = """
x = 3 + 4 * 5;
IF x < 10 THEN
    x = x + 1;
ELSE
    x = x - 1;
END;
WHILE x < 10 DO
    x = x + 1;
END;
"""

parser.parse(test_code)
