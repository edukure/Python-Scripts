import re

# message = 'Call me at 555-415-6868'
message = 'Meu telefone é (34)9864-8686'

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex = re.compile(r'\(\d\d\)\d\d\d\d\-\d\d\d\d')
matchObject = phoneNumRegex.search(message)
print(matchObject.group())
