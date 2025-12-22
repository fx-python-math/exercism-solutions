import re

def is_paired(input_string):
    res = re.sub("[+*-/\\\d\w\s!?#$%&@^.]+", "", input_string)
    running = True
    
    
    if len(res) % 2 != 0:
        return False

    cur = ""  

    while running:
        cur += res
        res = re.sub("\(\)|\[\]|{}", "", res)
        if cur == res:
            running = False

        cur = ""

    if res != "":
        return False

    return True


        
