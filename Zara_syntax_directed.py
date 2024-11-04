# zara_parser.py
import ply.yacc as yacc
from zara_lexer import tokens  # Import tokens from the lexer

# Intermediate code generator
temp_count = 0
label_count = 0

def new_temp():
    global temp_count
    temp = f"t{temp_count}"
    temp_count += 1
    return temp

def new_label():
    global label_count
    label = f"L{label_count}"
    label_count += 1
    return label

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
    '''expression_statement : ID ASSIGN expression'''
    print(f"{p[1]} = {p[3]}")  # Intermediate code for assignment

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
        p[0] = new_temp()
        print(f"{p[0]} = {p[1]} {p[2]} {p[3]}")  # Intermediate code
    elif len(p) == 3:  # Parenthesized expression
        p[0] = p[2]
    else:  # Single NUMBER or ID
        p[0] = p[1]

def p_conditional_statement(p):
    '''conditional_statement : IF expression THEN statement_list ELSE statement_list END'''
    
    true_label = new_label()  # Label for true branch
    end_label = new_label()  # Label for end of conditional
    print(f"IF {p[2]} GOTO {true_label}")  # Conditional jump
    print(f"GOTO {end_label}")  # Jump to end if false
    print(f"{true_label}:")
    for stmt in p[4]:  # Process true branch statements
        print(stmt)
    print(f"GOTO {end_label}")
    print(f"{end_label}:")

def p_loop_statement(p):
    '''loop_statement : WHILE expression DO statement_list END'''
    
    start_label = new_label()
    true_label = new_label()
    end_label = new_label()
    print(f"{start_label}:")
    print(f"IF {p[2]} GOTO {true_label}")  # Loop condition
    print(f"GOTO {end_label}")  # Exit if condition fails
    print(f"{true_label}:")
    for stmt in p[4]:  # Loop body
        print(stmt)
    print(f"GOTO {start_label}")  # Repeat loop
    print(f"{end_label}:")

def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

# Testing the parser
if __name__ == '__main__':
    print("Starting parser...")
    test_code = [
        "x = 3 + 4 * 5",
        "IF x < 5 THEN x = x + 1 ELSE x = x - 1 END",
        "WHILE x < 10 DO x = x + 1 END"
    ]

    for code in test_code:
        print(f"Parsing: {code}")
        parser.parse(code)
