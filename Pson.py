KeyLocal = "iMQUg4rjfq" # DO NOT REMOVE.
urlServerKey = "https://raw.githubusercontent.com/2983u2/Pson/main/ServerKey.py"


import json
import requests
import os
class Update:
    def start():
        r = requests.get(urlServerKey, allow_redirects=True)
        with open('ServerKey.py', 'wb') as f:
            f.write(r.content)
            f.close()
            from ServerKey import KeyServer
            if KeyServer == KeyLocal:
                print("")
                os.system("del ServerKey.py")
            else:
                print("This version is outdated. Please update to see bug fixes and much more\nhttps://github.com/2983u2/Pson\n\n\n\n")
class JSONParser:
    def __init__(self, json_string, file_path):
        self.json_string = json_string
        self.file_path = file_path
        self.index = 0
        self.current_char = self.json_string[self.index]
        self.line_number = 1
        self.column_number = 1
        self.variables = {}

    def error(self, message):
        raise Exception(f"Invalid JSON syntax at line {self.line_number}, column {self.column_number}: {message}")

    def advance(self):
        self.index += 1
        if self.index < len(self.json_string):
            self.current_char = self.json_string[self.index]
            if self.current_char == '\n':
                self.line_number += 1
                self.column_number = 1
            else:
                self.column_number += 1
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
        while self.current_char == '#':
            while self.current_char!= '\n' and self.current_char is not None:
                self.advance()
            self.advance()
            self.skip_whitespace()

    def parse_string(self):
        result = ""
        self.advance()  # skip opening quote
        while self.current_char!= '"':
            if self.current_char == '\\':
                self.advance()
                if self.current_char == 'n':
                    result += '\n'
                elif self.current_char == 't':
                    result += '\t'
                elif self.current_char == '"':
                    result += '"'
                elif self.current_char == '\\':
                    result += '\\'
                else:
                    self.error("Invalid escape sequence")
            else:
                result += self.current_char
            self.advance()
        self.advance()  # skip closing quote
        return result

    def parse_number(self):
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        if self.current_char == '.':
            result += '.'
            self.advance()
            while self.current_char is not None and self.current_char.isdigit():
                result += self.current_char
                self.advance()
        return float(result)

    def parse_object(self):
        result = {}
        self.advance()  # skip opening brace
        self.skip_whitespace()
        while self.current_char!= '}':
            key = self.parse_string()
            self.skip_whitespace()
            if self.current_char!= ':':
                self.error("Expected colon")
            self.advance()  # skip colon
            self.skip_whitespace()
            value = self.parse_value()
            result[key] = value
            self.skip_whitespace()
            if self.current_char == ',':
                self.advance()
                self.skip_whitespace()
        self.advance()  # skip closing brace
        return result

    def parse_array(self):
        result = []
        self.advance()  # skip opening bracket
        self.skip_whitespace()
        while self.current_char!= ']':
            value = self.parse_value()
            result.append(value)
            self.skip_whitespace()
            if self.current_char == ',':
                self.advance()
                self.skip_whitespace()
        self.advance()  # skip closing bracket
        return result

    def parse_value(self):
        self.skip_whitespace()
        if self.current_char == '"':
            return self.parse_string()
        elif self.current_char.isdigit():
            return self.parse_number()
        elif self.current_char == '{':
            return self.parse_object()
        elif self.current_char == '[':
            return self.parse_array()
        elif self.current_char == 't':
            self.advance()
            self.advance()
            self.advance()
            self.advance()
            return True
        elif self.current_char == 'f':
            self.advance()
            self.advance()
            self.advance()
            self.advance()
            self.advance()
            return False
        elif self.current_char == 'n':
            self.advance()
            self.advance()
            self.advance()
            self.advance()
            return None
        elif self.current_char == 'I':
            return self.parse_if_expression()
        else:
            self.error("Invalid JSON value")

    def parse(self):
        self.skip_whitespace()
        if self.current_char == '{':
            return self.parse_object()
        elif self.current_char == '[':
            return self.parse_array()
        else:
            self.error("Invalid JSON syntax")
    def write_to_object(self, obj, key, value):
        if isinstance(obj, dict):
            obj[key] = value
        elif isinstance(obj, list):
            if key.isdigit():
                index = int(key)
                if index < len(obj):
                    obj[index] = value
                else:
                    self.error("Index out of range")
            else:
                self.error("Invalid key for list")
        else:
            self.error("Invalid object type")

def JParse(json_string, file_path=None):
    Update.start()
    if file_path is None:
        file_path = "<string>"
    parser = JSONParser(json_string, file_path)
    
    return parser.parse()

def Jwrite(obj, key, value, parser):
    obj[key] = value
    with open(parser.file_path, "w") as file:
        json.dump(obj, file, indent=4)

def JParseF(file_path):
    Update.start()
    with open(file_path, 'r') as file:
        json_string = file.read()
        parser = JSONParser(json_string, file_path)
        obj = parser.parse()
        return obj, parser

class JwriteContext:
    def __init__(self, obj, key, value, parser):
        self.obj = obj
        self.key = key
        self.value = value
        self.parser = parser

    def __enter__(self):
        Jwrite(self.obj, self.key, self.value, self.parser)
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def jwrite(obj, key, value, parser):
    return JwriteContext(obj, key, value, parser)