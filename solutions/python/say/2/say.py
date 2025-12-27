import re

BELOW_20 = {
    0: "zero",
    1: "one",
    2: "two" ,
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

POWERS_OF_10 = {
    0: "",
    1: "ten",
    2: "hundred",
    3: "thousand",
    4: "ten thousand ",
    5: "hundred thousand " ,
    6: "million ",
    7: "ten million ",
    8: "hundred million" ,
    9: "billion "
}

PREFIXES = {
    2: "twen",
    3: "thir",
    4: "for",
    5: "fif"
}

def splitter(number):
    split = []
    s = str(number)
    temp = len(s)
    for i in range(len(str(number))):
        split.append((int(s[i]), temp - i - 1))

    return split

def under_thousand(number):
    if number in BELOW_20:
        return BELOW_20[number]
    if number == 0:
        return "zero"
    if number == 10:
        return "ten"
    
    n = splitter(number)
    
    final = ' '.join(
        f"{BELOW_20[a]}{(' ' + POWERS_OF_10[b]) if POWERS_OF_10[b] else ''}"
        for a, b in n
        if a != 0
    )

    matchh = re.search(r"\b(?:(?P<teen_case>one ten (?P<number>[a-z]+))|(?P<other>(?P<number_2>[a-z]+) ten))\b", final)

    if matchh:
        teen = matchh.group('teen_case')
        other_tens = matchh.group('other')
        num = matchh.group('number')
        num_2 = matchh.group('number_2')

        if teen:
            if num == "one":
                new_teen = BELOW_20[11]
            elif num == "two":
                new_teen = BELOW_20[12]
            elif num == "three":
                new_teen = PREFIXES[3] + "teen"
            elif num == "five":
                new_teen = PREFIXES[5] + "teen"
            elif num == "eight":
                new_teen = BELOW_20[8] + "een"
            else:
                new_teen = matchh.group('number') + "teen"
            
            final = re.sub(r"\bone ten ([a-z]+)\b", new_teen, final)

        if other_tens:
            if num_2 == "two":
                new = PREFIXES[2] + "ty"
            elif num_2 == "three":
                new = PREFIXES[3] + "ty"
            elif num_2 == "four":
                new = PREFIXES[4] + "ty"
            elif num_2 == "five":
                new = PREFIXES[5] + "ty"
            elif num_2 == "eight":
                new = BELOW_20[8] + "y"
            else:
                new = matchh.group('number_2') + "ty"

            final = re.sub(r"\b([a-z]+) ten\b", new, final)

    final = re.sub(r"\b([a-z]+ty)\s+([a-z]+)\b", r"\1-\2", final)

    final = re.sub(r"\s{2,}", " ", final).strip()

    return final

SCALES = {9: "billion", 6: "million", 3: "thousand", 1: ""}


def say(number):
    if 0 > number or number > 999_999_999_999:
        raise ValueError("input out of range")
    if number == 0:
        return "zero"
    if number < 1000:
        return under_thousand(number)

    largest_power = splitter(number)[0][1]

    S = max(s for s in SCALES if s <= largest_power)

    front, back = number // (10**S) , number % (10**S)

    if back:
        return f"{say(front)} {SCALES[S]} {say(back)}"
    else:
        return f"{say(front)} {SCALES[S]}"
    


        
