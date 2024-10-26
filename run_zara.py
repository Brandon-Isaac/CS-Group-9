from zara_parser import parser
# Tests
test1 = "3 + 4 * 5"
test2 = "IF x THEN x = x + 1 ELSE x = x - 1 END"
test3 = "WHILE x < 10 DO x = x + 1 END"

print(parser.parse(test1))
print(parser.parse(test2))
print(parser.parse(test3))