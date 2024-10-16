import re

# Define the patterns for different tokens
TOKEN_PATTERNS = [
    ('KEYWORD', r'\b(if|else|while|do|for|int|float|char|return)\b'),
    ('OPERATOR', r'[+\-*/=<>!]'),
    ('DATA_TYPE', r'\b(int|float|char|void)\b'),
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ('LITERAL', r'\b\d+(\.\d+)?\b'),  # matches integers and floats
    ('WHITESPACE', r'\s+'),  # matches whitespace
    ('COMMENT', r'//.*'),  # matches single line comments
    ('NEWLINE', r'\n')  # matches new lines
]

# Combine all patterns into one regex
token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in TOKEN_PATTERNS)


# Function to perform lexical analysis
def lexical_analyzer(code):
    tokens = []
    for match in re.finditer(token_regex, code):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        if token_type == 'WHITESPACE' or token_type == 'COMMENT':
            continue  # Ignore whitespace and comments
        tokens.append((token_type, token_value))
    return tokens


# Sample input code for the Zara language
zara_code = """
int x = 10;
float y = 20.5;
if (x < y) {
    x = x + 1;
    // Increment x
} else {
    x = x - 1;
}
"""

# Perform lexical analysis
tokens = lexical_analyzer(zara_code)

# Print the tokens
for token in tokens:
    print(token)
