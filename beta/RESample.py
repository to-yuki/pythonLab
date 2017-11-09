import re

string = u"https://www.python.org/community/irc/"
pattern = r"https://(.*?)/(.*?)/(.*?)/"

prog = re.compile(pattern)
result = re.match(pattern, string)

print(result.group())
print(result.group(0))
print(result.group(1))
print(result.group(2))
print(result.group(3))



