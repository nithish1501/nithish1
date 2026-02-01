class FileManager:
    def _init_(self, filename):
        self.filename = filename

    def _enter_(self):
        self.file = open(self.filename, "w")
        return self.file

    def _exit_(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileManager("test.txt") as f:
    f.write("Hello, context managers!")