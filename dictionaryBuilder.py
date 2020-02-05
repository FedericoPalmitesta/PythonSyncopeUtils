import re, json, sys


def parse_string(string):
    string = re.sub(r'\".?\"', '', string)
    string = re.sub(r'\".+?\"', '', string)
    return re.sub(r'(\"|\(|\[|\{|\)|\]|\}|<|>|=|/)', '', string)


dictionary = {}

with open('dict.json', 'w+') as json_file:
    if len(json_file.readlines()) != 0:
        json_file.seek(0, 0)
        dictionary = json.load(json_file)


if sys.argv[1] == '--help':
    print('Provide two parameters: the path to an UPPER case MasterContent.xml and to a lowerCamelCase MasterContent')
elif len(sys.argv) < 2:
    print('Error: no arguments have been provided. Use --help for usage')
else:
    try:
        uppercase_file = sys.argv[1]
        lowercamelcase_file = sys.argv[2]

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

        with open('dict.json', 'w+', encoding='utf-8') as json_file:
            json.dump(dictionary, json_file, ensure_ascii=False, indent=4, sort_keys=True)

        print('Dictionary successfully updated')

    except FileNotFoundError:
        print('The input file has not been found')
