from string import ascii_uppercase

LETTERS = {letter: n for n, letter in enumerate(ascii_uppercase, 1)}
REV = {n: letter for letter, n in LETTERS.items()}

def rows(letter):
    if letter == "A":
        return ["A"]
    n = LETTERS[letter]
    final = ["A".center(2*n - 1)]
    fmt = "{empty:{w1}}{letter:{w2}}{letter:{w3}}"
    w1, w2 = n - 2, 2
    for i in range(2, n + 1):
        final.append(fmt.format(empty="", w1=w1, letter=REV[i], w2=w2, w3=w1+1))
        w1 -= 1
        w2 += 2
    
    return final + final[-2::-1]

