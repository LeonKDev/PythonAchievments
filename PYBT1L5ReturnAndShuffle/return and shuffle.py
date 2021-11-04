import random

def Shuffle(word):
    return ''.join(random.sample(word, len(word)))

print(Shuffle("random"))
print(Shuffle("random"))
print(Shuffle("random"))