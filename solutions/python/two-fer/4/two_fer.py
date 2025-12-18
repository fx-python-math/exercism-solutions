"""
    Returns a string 'One for {name}, one for me.' if a name is given, otherwise returns
    'One for you, one for me.'
"""

def two_fer(name="you"):
    
    return f"One for {name}, one for me." if name != "you" else "One for you, one for me."
