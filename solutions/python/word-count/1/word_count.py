import re
from collections import Counter

def count_words(string: str) -> dict[str: int]:
    s = string
    r = re.findall(r"[a-zA-Z]+'[a-zA-Z]+|[a-zA-Z]+|\d+", s)
    r = map(str.lower, r)

    d = Counter(r)

    return {k: d[k] for k in sorted(d)}
