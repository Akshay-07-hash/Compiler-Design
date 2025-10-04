# codegen.py

from ast import ProgramNode, FunctionNode, ReturnNode, NumberNode

class CodeGenerator:
    """Traverses the AST and generates x86-64 assembly code."""

    def __init__(self, ast):
        self.ast = ast
        self.output_code = []

    def emit(self, instruction):
        """Adds an assembly instruction to the output list."""
        self.output_code.append(instruction)

    def generate_code(self):
        """Main entry point: starts code generation from the ProgramNode."""
        self.visit(self.ast)
        return "\n".join(self.output_code)

    def visit(self, node):
        """Dispatch method to call the correct visitor based on node type."""
        # This is a simple implementation of the Visitor pattern
        method_name = 'visit_' + type(node).__name__.replace('Node', '')
        visitor_method = getattr(self, method_name, self.generic_visit)
        return visitor_method(node)

    def generic_visit(self, node):
        raise Exception(f"No visit method defined for node type: {type(node).__name__}")

    # --- Visitor Methods for AST Nodes ---

    def visit_Program(self, node: ProgramNode):
        """Visit the root of the AST."""
        self.emit("section .text") # Code section
        self.visit(node.func)

    def visit_Function(self, node: FunctionNode):
        """Visit a function (only main for now)."""
        # Standard label for the main function
        self.emit("\tglobal _main") 
        self.emit("_main:")
        
        # Function prologue (simplified)
        self.emit("\tpush rbp")
        self.emit("\tmov rbp, rsp")
        
        # Generate code for the function body (the return statement)
        self.visit(node.body)
        
        # Function epilogue (simplified)
        self.emit("\tpop rbp")
        self.emit("\tret")

    def visit_Return(self, node: ReturnNode):
        """Visit a return statement."""
        # Generate the value of the expression (which loads it into EAX)
        self.visit(node.expr) 
        
        # EAX already contains the return value (from visit_Number), so we do nothing else
        # The 'ret' instruction is handled in visit_Function

    def visit_Number(self, node: NumberNode):
        """Visit a number literal."""
        # Load the constant integer value into the EAX register (the standard return register)
        self.emit(f"\tmov eax, {node.value}")