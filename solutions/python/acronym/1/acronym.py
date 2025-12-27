import re

def abbreviate(words):
    words = re.sub(r"[^a-zA-Z]", " ", words.replace("'", ""))
    word_list = [x[0] for x in words.split()]

    return "".join([x.upper() for x in word_list])
