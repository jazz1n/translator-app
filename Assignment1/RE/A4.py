import re

text = '''
Here is some text with a JSON object: {"key1": "value1", "key2": {"nestedKey": 123}}
and here is an array: [1, 2, {"arrayKey": "arrayValue"}, [3, 4]]
Another JSON object: {"simpleKey": "simpleValue"}
'''

# Define a more constrained pattern to match JSON objects without using recursion
pattern = r'\{(?:[^{}"]|"[^"]*"|\d+|true|false|null|(?:\{(?:[^{}"]|"[^"]*"|\d+|true|false|null)*\}))*\}'

# Find all matches in the text
matches = re.findall(pattern, text, re.DOTALL)

# Print results
for match in matches:
    print(match)
