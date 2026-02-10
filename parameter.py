import inspect

def complex_function(a: int, b: str = "default") -> bool:
    pass


sig = inspect.signature(complex_function)
for name, param in sig.parameters.items():
    print(f"Arg: {name} | Type: {param.annotation} | Default: {param.default}")