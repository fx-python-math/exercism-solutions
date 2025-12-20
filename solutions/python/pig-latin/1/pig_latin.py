import re 

def convert(word):
    vowel_regex = "(?i)^([^aeiouy]+)"
    matchh = re.match(vowel_regex, word)
    matchh_two = re.match("(?i)^yt|xr", word)
    matchh_three = re.match("(?i)^([^aeiouxy]*qu)", word)

    if matchh_three:
        word = word.replace(matchh_three.group(), "")
        return f"{word}{matchh_three.group()}"

    elif word.lower().startswith("y") and not matchh_two:
        word = word.replace("y", "")
        return f"{word}y"

    elif matchh_two:
        return word
    
    elif matchh:
        word = word.replace(matchh.group(), "")
        return f"{word}{matchh.group()}"
        
    else:
        return word


def translate(word):
    return " ".join(convert(w) + "ay" for w in word.split())