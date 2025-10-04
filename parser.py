# parser.py
from lexer import lexer # Import our Lexer
from ast import ProgramNode, FunctionNode, ReturnNode, NumberNode

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0 

    def current_token(self):
        """Returns the token at the current position."""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return self.tokens[-1] # The EOF token

    def consume(self, expected_type):
        """Checks the current token, advances position, and returns the consumed token."""
        token = self.current_token()
        if token.type == expected_type:
            self.pos += 1
            return token
        
        # Simple error handling for now
        raise SyntaxError(f"Syntax Error: Expected {expected_type}, but found {token.type} at position {self.pos}")

    # --- Grammar Rule Implementations (Recursive Descent) ---

    # Rule: program ::= function
    def parse_program(self):
        return ProgramNode(self.parse_function())

    # Rule: function ::= "int" "main" "(" ")" "{" statement "}"
    def parse_function(self):
        self.consume('INT')
        self.consume('MAIN')
        self.consume('LPAREN')
        self.consume('RPAREN')
        self.consume('LBRACE')
        
        statement_node = self.parse_statement()

        self.consume('RBRACE')
        
        return FunctionNode('main', statement_node)

    # Rule: statement ::= "return" expression ";"
    def parse_statement(self):
        self.consume('RETURN')
        
        expr_node = self.parse_expression()
        
        self.consume('SEMICOLON')
        
        return ReturnNode(expr_node)

    # Rule: expression ::= NUMBER
    def parse_expression(self):
        # Consume the number token and create a NumberNode
        number_token = self.consume('NUMBER')
        return NumberNode(number_token.value)

    def parse(self):
        """Main entry point for the parser."""
        ast = self.parse_program()
        # Ensure we consumed everything up to EOF
        self.consume('EOF') 
        return ast

# --- Test Parser ---
if __name__ == '__main__':
    source_code = "int main() { return 42; }"
    tokens = lexer(source_code)
    
    print("--- Tokens Input to Parser ---")
    print(tokens)

    parser = Parser(tokens)
    try:
        ast = parser.parse()
        print("\n--- Abstract Syntax Tree (AST) Output ---")
        print(ast)
    except SyntaxError as e:
        print(f"Parsing Failed: {e}")