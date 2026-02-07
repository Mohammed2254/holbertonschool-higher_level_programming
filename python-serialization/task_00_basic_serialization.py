""" a model that serialize and deserialize a """
import json
def serialize_and_save_to_file(data, filename):
    """serielize"""
    with open(filename, "w") as file:
        return json.dump(data, file)

def load_and_deserialize(filename):
    """deserielize"""
    with open(filename, "r") as file:
        return json.load(file)