# Problem 5: Sparse Arrays
from collections import Counter

def matchingStrings(stringList, queries):
    counts = Counter(stringList)
    return [counts[q] for q in queries]