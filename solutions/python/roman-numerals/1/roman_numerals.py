import re

ROMAN = {"1000": "M" , "500": "D", "100": "C" , "50": "L" , "10": "X" , "5": "V", "1": "I"}

def splitter(num):
    final = []
    for n in sorted(ROMAN.keys(), key=lambda x: -int(x)):
        while num >= int(n):
            final.append(n)
            num -= int(n)
        if num == 0:
            break
        
    s = " ".join(final)


    s = re.sub(r"\b5 1 1 1 1\b", "110", s)

    s = re.sub(r"\b1 1 1 1\b", "15", s)

    s = re.sub(r"\b50 10 10 10 10\b", "10100", s)

    s = re.sub(r"\b10 10 10 10\b", "1050", s)

    s = re.sub(r"\b500 100 100 100 100\b", "1001000", s)

    s = re.sub(r"\b100 100 100 100\b", "100500", s)

    return s

def roman(n):
    s = splitter(n)
    return re.sub(r'\b(?:1000|500|100|50|10|5|1)+\b',
                  lambda m: ''.join(ROMAN[p] for p in re.findall(r'1000|500|100|50|10|5|1', m.group(0))),
                  s).replace(' ', '')
