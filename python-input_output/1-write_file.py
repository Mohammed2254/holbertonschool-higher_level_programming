""" model to w a file"""


def write_file(filename="", text=""):
    """the func"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
