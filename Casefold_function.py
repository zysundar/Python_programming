#The casefold() method is an aggressive lower() method which convert strings to casefolded strings for caseless matching.

string = "PYTHON IS AWESOME"

# print lowercase string
print("Lowercase string:", string.casefold())


firstString = "der Fluß"
secondString = "der Fluss"

# ß is equivalent to ss in german
if firstString.casefold() == secondString.casefold():
    print('The strings are equal.')
else:
    print('The strings are not equal.')
