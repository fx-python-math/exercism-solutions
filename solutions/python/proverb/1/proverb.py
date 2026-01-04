def proverb(*args, qualifier=None):
    if not args:
        return []
    final = []

    for i in range(1, len(args)):
        final.append(f"For want of a {args[i-1]} the {args[i]} was lost.")

    if qualifier:
        final.append(f"And all for the want of a {qualifier} {args[0]}.")
    else:
        final.append(f"And all for the want of a {args[0]}.")
        
    return final



