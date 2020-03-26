import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))

word = input("Enter Your word to search: ")

def translate(word):
    if word.lower() in data:
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    # return closest match
    elif len(get_close_matches(word, data.keys())) >0:
        print(f"did you mean {get_close_matches(word, data.keys())[0]}")
        answer = input("press y for Yes and n for No: ")
        if answer == "y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "not Found"

    else:
        return"No Match, Pla try another word..."

#print multiple result in saperate line
result = translate(word)
if type(result) == "list":
    for item in result:
        print(item)
else:
    print(result)


