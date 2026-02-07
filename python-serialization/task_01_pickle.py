"""pickle class for anyhting"""
import pickle

class CustomObject:
    """class"""
    def __init__(self, name, age, is_student):
        """main"""
        self.name = name
        self.age = age
        self.is_student = is_student
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
    def serialize(self, filename):
        """ser"""
        try:
            with open(filename, "wb") as file:
                return pickle.dump(self, file)
        except:
            return None

    @classmethod
    def deserialize(cls, filename):
        """des"""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except:
            return None