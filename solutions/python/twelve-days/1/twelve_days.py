nums = {
    1: "and a",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve"
}

ordinals = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth"
}

things = {
    1: "Partridge in a Pear Tree.",
    2: "Turtle Doves, ",
    3: "French Hens, ",
    4: "Calling Birds, ",
    5: "Gold Rings, ",
    6: "Geese-a-Laying, ",
    7: "Swans-a-Swimming, ",
    8: "Maids-a-Milking, ",
    9: "Ladies Dancing, ",
    10: "Lords-a-Leaping, ",
    11: "Pipers Piping, ",
    12: "Drummers Drumming, "
}

def recite(start_verse, end_verse):
    res = []
    for v in range(start_verse, end_verse+1):
        begin = [f"On the {ordinals[v]} day of Christmas my true love gave to me: "]

        rest = [ 
            f"{nums[i]} {things[i]}"
            for i in range(v, 0, -1)
        ]

        new = begin + rest
        if v == 1:
            new = "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree."

        res.append(''.join(new))

    return res