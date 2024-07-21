from Pson import *

# NOTE JParse() does the same as JParseF() but with defined strings.

result, _ = JParseF("example1.json")
print(result)

# This writes to the json file selected by (JParseF)

with jwrite(result, "name", "JohnDoe", _) as f:
    pass

# Also can be used as 
jwrite(result, "name", "JohnDoe", _)

