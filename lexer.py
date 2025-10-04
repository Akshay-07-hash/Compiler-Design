import re

# 1. Define the Token class
class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
    
    def __repr__(self):
        # A clean way to print the token for debugging
        return f"Token({self.type}, {repr(self.value) if self.value is not None else ''})"

# 2. Define Token Specifications (Regex Patterns)
TOKEN_SPECS = [
    # Keywords
    ('INT', r'int'),
    ('MAIN', r'main'),
    ('RETURN', r'return'),
    # Symbols/Punctuation
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('SEMICOLON', r';'),
    # Data Types
    ('NUMBER', r'[0-9]+'),
    # Ignore
    ('SKIP', r'[ \t\n]+'), # Whitespace to ignore
]

# 3. Implement the Lexer function
def lexer(code):
    tokens = []
    # Combine patterns into one regex for efficient matching
    token_patterns = '|'.join(f'(?P<{name}>{pattern})' 
                              for name, pattern in TOKEN_SPECS)
    
    for match in re.finditer(token_patterns, code):
        type = match.lastgroup
        value = match.group(type)
        
        if type == 'SKIP':
            continue
        elif type == 'NUMBER':
            # Convert number string to an integer value
            tokens.append(Token(type, int(value)))
        else:
            tokens.append(Token(type, value))
            
    # Always append an End-Of-File token to signal the end
    tokens.append(Token('EOF')) 
    return tokens

# --- Test Lexer ---
if __name__ == '__main__':
    source_code = "int main() { return 42; }"
    print("--- Source Code ---")
    print(source_code)
    print("\n--- Tokens Generated ---")
    
    generated_tokens = lexer(source_code)
    for token in generated_tokens:
        print(token)