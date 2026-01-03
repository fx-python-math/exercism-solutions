import re

def score(word):
    word = word.upper()

    ones = len(''.join(re.findall("[AEIOULNRST]+", word)))
    twos = len(''.join(re.findall("[DG]+", word)))
    threes = len(''.join(re.findall("[BCMP]+", word)))
    fours = len(''.join(re.findall("[FHVWY]+", word)))
    fives = len(''.join(re.findall("[K]+", word)))
    eights = len(''.join(re.findall("[JX]+", word)))
    tens = len(''.join(re.findall("[QZ]+", word)))

    return ones + 2*twos + 3*threes + 4*fours + 5*fives + 8*eights + 10*tens
