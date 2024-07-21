from Pson import *
import datetime

# NOTE JParse() does the same as JParseF() but with defined strings.

start_time = datetime.datetime.now()
result, parser = JParseF("example1.json")
end_time = datetime.datetime.now()

print(f"Time taken to parse: {end_time - start_time}")
print(result)

# This writes to the json file selected by (JParseF)

with jwrite(result, "name", "JohnDoe", parser) as f:
    pass

# Also can be used as 
jwrite(result, "name", "JohnDoe", parser)