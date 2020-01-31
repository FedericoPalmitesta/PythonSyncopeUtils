import re


def parse_string(string):
    string = string.replace("<", '')
    string = string.replace(">", '')
    string = string.replace("=", '')
    string = string.replace("/", '')
    string = re.sub(r'\".?\"', '', string)
    return re.sub(r'\".+?\"', '', string)


dictionary = dict()

uppercase_file = input("Provide the path of an 'UPPERCASE' MasterContent (/path/MasterContent.xml): ")
lowercamelcase_file = input("Provide the path of a 'lowerCamelCase' MasterContent (/path/MasterContent.xml): ")

uppercase_words = set()
lowercamelcase_words = set()

with open(uppercase_file) as uppercase:
    for line in uppercase:
        uppercase_words.update(parse_string(line).split())

with open(lowercamelcase_file) as lowercase:
    for line in lowercase:
        if not line.startswith('<!--') or line.startswith('+') or line.startswith('<?'):
            lowercamelcase_words.update(parse_string(line).split())

for word in lowercamelcase_words:
    if word.upper() in uppercase_words:
        dictionary[word.upper()] = word

print('The result is the following dictionary:')
print(dictionary)
