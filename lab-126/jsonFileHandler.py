import json
#f=open('insulin.json')
def readJsonFile(f):
    data = ""
    try:
        with open('insulin.json') as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data