EXCEPTIONS = ("11", "12", "13")

def line_up(name, number):
    num = f"{number}th"
    
    if not any(str(number).endswith(exc) for exc in EXCEPTIONS):
        if str(number).endswith("1"):
            num = str(number) + "st"
        elif str(number).endswith("2"):
            num = str(number) + "nd"
        elif str(number).endswith("3"):
            num = str(number) + "rd"

    return f"{name}, you are the {num} customer we serve today. Thank you!"
