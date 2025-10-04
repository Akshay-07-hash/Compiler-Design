# main.py

from lexer import lexer
from parser import Parser
from codegen import CodeGenerator

def compile_source(source_code):
    """Orchestrates the entire compilation process."""
    
    # 1. Lexical Analysis
    tokens = lexer(source_code)
    print(f"Tokens: {tokens[:8]}...")
    
    # 2. Syntax Analysis
    parser = Parser(tokens)
    ast = parser.parse()
    print(f"AST Root: {ast}")
    
    # 3. Code Generation
    generator = CodeGenerator(ast)
    assembly_code = generator.generate_code()
    
    return assembly_code

if __name__ == '__main__':
    SOURCE_CODE = "int main() { return 42; }"
    OUTPUT_FILE = "output.s"
    
    print("\n--- Starting Compiler ---")
    print(f"Compiling: {SOURCE_CODE}")
    
    try:
        assembly = compile_source(SOURCE_CODE)
        
        # Save the assembly code to a file
        with open(OUTPUT_FILE, "w") as f:
            f.write(assembly)
            
        print(f"\n--- Compilation Successful! ---")
        print(f"Assembly saved to {OUTPUT_FILE}")
        print("\n--- Generated Assembly Code ---")
        print(assembly)
        
    except Exception as e:
        print(f"\n--- Compilation Failed! ---")
        print(f"Error: {e}")