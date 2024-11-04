class CodeGenerator:
    def __init__(self):
        self.temp_count = 0
        self.label_count = 0
        self.code = []

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"

    def emit(self, code_line):
        self.code.append(code_line)

    def translate_expression(self, expr):
        if expr["type"] == "binary_op":
            left = self.translate_expression(expr["left"])
            right = self.translate_expression(expr["right"])
            result = self.new_temp()
            self.emit(f"{result} = {left} {expr['op']} {right}")
            return result
        elif expr["type"] == "identifier":
            return expr["value"]
        elif expr["type"] == "literal":
            return expr["value"]

    def translate_assignment(self, assignment):
        value = self.translate_expression(assignment["expr"])
        self.emit(f"{assignment['var']} = {value}")

    def translate_if_else(self, condition, true_block, false_block=None):
        true_label = self.new_label()
        false_label = self.new_label()
        end_label = self.new_label()

        # Translate the condition
        cond_result = self.translate_expression(condition)
        self.emit(f"if {cond_result} goto {true_label}")
        self.emit(f"goto {false_label}")

        # Translate the true block
        self.emit(f"{true_label}:")
        for stmt in true_block:
            self.translate_statement(stmt)
        self.emit(f"goto {end_label}")

        # Translate the false block, if it exists
        if false_block:
            self.emit(f"{false_label}:")
            for stmt in false_block:
                self.translate_statement(stmt)

        # End label
        self.emit(f"{end_label}:")

    def translate_while_loop(self, condition, body):
        start_label = self.new_label()
        true_label = self.new_label()
        end_label = self.new_label()

        # Start of the loop
        self.emit(f"{start_label}:")
        
        # Translate the condition
        cond_result = self.translate_expression(condition)
        self.emit(f"if {cond_result} goto {true_label}")
        self.emit(f"goto {end_label}")

        # Loop body
        self.emit(f"{true_label}:")
        for stmt in body:
            self.translate_statement(stmt)

        # Go back to the start
        self.emit(f"goto {start_label}")
        
        # End of the loop
        self.emit(f"{end_label}:")

    def translate_statement(self, stmt):
        if stmt["type"] == "assignment":
            self.translate_assignment(stmt)
        elif stmt["type"] == "if":
            self.translate_if_else(stmt["condition"], stmt["true_block"], stmt.get("false_block"))
        elif stmt["type"] == "while":
            self.translate_while_loop(stmt["condition"], stmt["body"])

    def generate_code(self):
        return "\n".join(self.code)

# Example usage
generator = CodeGenerator()

# Assignment example
generator.translate_statement({
    "type": "assignment",
    "var": "x",
    "expr": {
        "type": "binary_op",
        "op": "+",
        "left": {"type": "identifier", "value": "y"},
        "right": {"type": "identifier", "value": "z"}
    }
})

# If-else example
generator.translate_statement({
    "type": "if",
    "condition": {
        "type": "binary_op",
        "op": ">",
        "left": {"type": "identifier", "value": "x"},
        "right": {"type": "literal", "value": "10"}
    },
    "true_block": [
        {"type": "assignment", "var": "a", "expr": {"type": "literal", "value": "1"}}
    ],
    "false_block": [
        {"type": "assignment", "var": "a", "expr": {"type": "literal", "value": "0"}}
    ]
})

# While loop example
generator.translate_statement({
    "type": "while",
    "condition": {
        "type": "binary_op",
        "op": "<",
        "left": {"type": "identifier", "value": "a"},
        "right": {"type": "literal", "value": "10"}
    },
    "body": [
        {"type": "assignment", "var": "a", "expr": {
            "type": "binary_op",
            "op": "+",
            "left": {"type": "identifier", "value": "a"},
            "right": {"type": "literal", "value": "1"}
        }}
    ]
})

# Print the generated intermediate code
print(generator.generate_code())
