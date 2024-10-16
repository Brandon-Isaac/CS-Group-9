class SymbolTable:

    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, var_type, value=None):
        """Adds a new symbol to the table."""
        if name in self.symbols:
            print(f"Error: Variable '{name}' is already declared.")
        else:
            self.symbols[name] = {"type": var_type, "value": value}
            print(f"Added: {name} -> Type: {var_type}, Value: {value}")

    def update_symbol(self, name, value):
        """Updates the value of an existing symbol."""
        if name in self.symbols:
            self.symbols[name]['value'] = value
            print(f"Updated: {name} -> Value: {value}")
        else:
            print(f"Error: Variable '{name}' not found.")

    def get_symbol(self, name):
        """Retrieves a symbol's type and value."""
        if name in self.symbols:
            return self.symbols[name]
        else:
            print(f"Error: Variable '{name}' not found.")
            return None

    def log_symbols(self):
        """Logs all symbols in the symbol table."""
        print("Current Symbol Table:")
        for name, data in self.symbols.items():
            print(f"{name}: Type = {data['type']}, Value = {data['value']}")


# Create a global symbol table
symbol_table = SymbolTable()


# Function to simulate Zara variable declarations
def zara_program():
    # Declare variables of different types
    symbol_table.add_symbol("x", "integer", 10)
    symbol_table.add_symbol("y", "float", 3.14)
    symbol_table.add_symbol("name", "string", "ZaraLanguage")
    symbol_table.add_symbol("numbers", "array", [1, 2, 3, 4])
    symbol_table.add_symbol("stack1", "stack", [])

    # Simulate updates and retrieve
    symbol_table.update_symbol("x", 20)  # Updating integer variable
    symbol_table.update_symbol("stack1", [1, 2])  # Adding items to stack
    print(symbol_table.get_symbol("Y"))  # Retrieve integer
    print(symbol_table.get_symbol("name"))  # Retrieve string

    # Test sub-program (method) that modifies symbol table
    zara_sub_program()

    # Log symbol table at the end of program
    symbol_table.log_symbols()


def zara_sub_program():
    # Simulate a function that declares local variables
    print("Inside sub-program...")
    symbol_table.add_symbol("temp", "integer", 50)
    symbol_table.update_symbol("temp", 100)  # Updating local variable
    print(symbol_table.get_symbol("temp"))  # Retrieve local variable


# Run the Zara program
zara_program()
