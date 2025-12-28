from collections import Counter
import re

def counting(string):
    start = string[0]
    COUNTS = []
    count = 0
    for x in string:
        if x != start:
            break
        count += 1

    COUNTS.append(count) if count != 1 else COUNTS.append(0)

    part = string[:count]

    string = string[count:]

    if string == "":
        return COUNTS
    else:
        return COUNTS + counting(string)

def encode(string):
    if string == "":
        return ""
    string = string
    counts = counting(string)
    start = string[0]

    count = 0
    for x in string:
        if x != start:
            break
        count += 1

    part = string[:count]
    string = string[count:]


    encoded = f"{counts[0]}{part[0]}"
    encoded = encoded.strip("0")

    if string == "":
        return encoded
    else:
        return encoded + encode(string)

def decode(string):
    tokens = re.findall(r"\d*\D", string)
    print(tokens)

    if tokens == []:
        return string

    new = ''.join(int(token[:-1]) * token[-1] if len(token) > 1 else token for token in tokens)

    return new
        

    
