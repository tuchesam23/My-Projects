import re

var = input("camelCase: ")
var = re.sub(r'(?<!^)(?=[A-Z])', '_', var).lower()
print("snake_case: ", var)
