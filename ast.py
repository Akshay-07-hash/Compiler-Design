# ast.py

class ProgramNode:
    """Root of the AST: Contains the list of functions."""
    def __init__(self, func):
        self.func = func
        
    def __repr__(self):
        return f"Program({self.func})"

class FunctionNode:
    """Represents a function definition."""
    def __init__(self, name, body):
        self.name = name
        self.body = body 
        
    def __repr__(self):
        return f"Function(name='{self.name}', body={self.body})"

class ReturnNode:
    """Represents a 'return' statement."""
    def __init__(self, expr):
        self.expr = expr # The expression being returned
        
    def __repr__(self):
        return f"Return({self.expr})"

class NumberNode:
    """Represents a constant integer literal."""
    def __init__(self, value):
        self.value = value
        
    def __repr__(self):
        return f"Number({self.value})"