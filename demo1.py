
import json
from difflib import get_close_matches

data= json.load(open("data.json"))

def  translate(w):
    w = w.lower()
    if w in data:
        return data[word]
    elif len(get_close_matches(w,data.keys()))>0:
        yn = input( "did you mean %s instead? Enter 'Y' if yes or 'N' for no:" % get_close_matches(w,data.keys())[0])
        if yn=='Y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=='N':
            return "The word doesn't exist"
        else:
            return "we didn't understand your answer"
    else:
        return "The word doesn't exist .please check again"


word = input("Enter Word Please:")


output = (translate(word))
if type(output) == list :
    for item in output:
        print (item)
else:
        print(output)