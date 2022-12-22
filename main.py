import platform

class PythonWasm:
    def __init__(self):
        self.message = "Hello Python WASM!"
    
    def print(self):
        print(self.message)
    
    def write(self, filename, message):
        file = open(filename, "w")
        file.write(message)
        file.close()
    
    def copy(self, fromFile, toFile):
        f1 = open(fromFile, "r")
        f2 = open(toFile, "w")

        for line in f1.readlines():
            f2.write(f"{line}\n")
        
        f1.close()
        f2.close()

print(platform.platform())

wasm = PythonWasm()
wasm.print()

# Python + wasm is a little odd in how it expects the filesystem to be
# laid out, so we place this file in the /workspace/ directory in the
# wasm environment
wasm.write("/workspace/test.txt", "this is a test")
print("Wrote file")

wasm.copy("/workspace/test.txt", "/workspace/test-2.txt")
print("Copied file")