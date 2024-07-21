# PSON
PSON aka PynxSON is my extension of the JSON library for Python.
Did you ever want a better version of JSON? This library is for you then!

# How To Install?
1. Download the file (Pson.py) from this repo.
2. Place the file into your project.
3. Import the file: `from Pson import *`
4. Call the functions: __examples below__

An actual PIP system will work in the future.

# What Are The Features?
1. Comments (Ever needed to describe your objects? Well now you can!)
2. Better read and write (no "with open")
3. Better Speed and compatibility

# Examples
## Functions
`JParseF(filepath)` - Parses a File
`JParse(jsonstring)` - Takes a String
`jwrite(obj, key, value, parser)` - Writes to a file (supports with ^)

## Comments
`# This is a comment`
More in https://github.com/2983u2/Pson/tree/main/examples.

# Latest patch
- Removed If statements
- Removed non-needed variables
- Cleaned up Jwrite a little
- Added a Parser object for "JParseF()"
- Renamed "parse_json_file()" to "JParseF()"
- Renamed "parse_json()" to "JParse()" 