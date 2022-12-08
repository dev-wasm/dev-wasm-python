class PythonWasm:
    def __init__(self):
        self.message = "Hello Python WASM!"
    
    def print(self):
        print(self.message)

wasm = PythonWasm()
wasm.print()