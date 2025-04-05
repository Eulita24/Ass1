from abc import ABC, abstractmethod

# Abstract Base Class FileHandler
class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass  # Abstract method, must be implemented in subclasses

    @abstractmethod
    def write(self, data):
        pass  # Abstract method, must be implemented in subclasses


# Concrete Class TextFileHandler
class TextFileHandler(FileHandler):
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        with open(self.file_name, 'r') as file:
            return file.read()

    def write(self, data):
        with open(self.file_name, 'w') as file:
            file.write(data)
        print("Text written to the file successfully.")


# Concrete Class BinaryFileHandler
class BinaryFileHandler(FileHandler):
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        with open(self.file_name, 'rb') as file:
            return file.read()

    def write(self, data):
        with open(self.file_name, 'wb') as file:
            file.write(data)
        print("Binary data written to the file successfully.")


# Example usage
text_handler = TextFileHandler("example.txt")
text_handler.write("Hello, world!")
print("TextFileHandler read:", text_handler.read())

binary_handler = BinaryFileHandler("example.bin")
binary_handler.write(b"Hello, binary world!")
print("BinaryFileHandler read:", binary_handler.read())
