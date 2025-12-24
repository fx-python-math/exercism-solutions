from string import ascii_uppercase

letters = {letter[1]: letter[0]+1 for letter in enumerate(ascii_uppercase)}
rev = {letter[0]+1: letter[1] for letter in enumerate(ascii_uppercase)}

def rows(letter):
    if letter == "A":
        return ["A"]
    n = letters[letter]
    final = []
    final.append((" " * (letters[letter] - 1) + "A" + " " * (letters[letter] - 1)).ljust(2*n-1))
    r = n
    l = 0
    for i in range(2, n+1):
        right_up = " " * (r-2) + f"{rev[i]}"
        left_up = " " * (2 * l) + f"{rev[i]}"
        if i != n:
            line = right_up + " " + left_up + " "
        else:
            line = right_up + " " + left_up

        final.append(line.ljust(2*n-1))
        r -= 1   
        l += 1

    for i in range(2, n):
        left_down = " " * (r) + f"{rev[n - i + 1]}"
        right_down =  " " * (l * 2- 4) + f"{rev[n - i + 1]}" 
        line = left_down + " " + right_down
        if (n - i + 1) != n:
            line += " "
        final.append(line.ljust(2*n-1))
        r += 1
        l -= 1

    final.append((" " * (letters[letter] - 1) + "A" + " " * (letters[letter] - 1)).ljust(2*n-1))
    return final

