import re, sys, json


def parse_string(string):
    string = string.replace("<", '')
    string = string.replace(">", '')
    string = string.replace("=", '')
    string = string.replace("/", '')
    string = re.sub(r'\".?\"', '', string)
    return re.sub(r'\".+?\"', '', string)


dictionary = {}

with open("dict.json") as json_file:
    dictionary = json.load(json_file)


if sys.argv[1] == "--help":
    print("Provide two parameters: the path to the MasterContent.xml to be parsed and a path to the output file")
elif len(sys.argv) < 2:
    print("Error: no arguments have been provided. Use --help for usage")
else:
    try:
        old_file = sys.argv[1]
        new_file = sys.argv[2]
        with open(old_file) as oldfile, open(new_file, 'w') as newfile:
            for line in oldfile:
                for word in parse_string(line).split():
                    line = line.replace(word, dictionary.get(word, word), 1)
                newfile.write(line)
        print("parsing succeeded")
    except FileNotFoundError:
        print("the input file has not been found")
