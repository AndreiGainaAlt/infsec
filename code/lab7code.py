from random import choice
import string


phrase = "С новым годом друзья!"
key_components = [str(i) for i in range(len(phrase))] + list(string.ascii_uppercase)

print(key_components)

key = ""

for i in range(len(phrase)):
    key = key + choice(key_components)

def cypher(key, text):
    _ = ""
    for i in range(len(text)):
        _ = _ + chr(ord(text[i]) ^ ord(key[i]))
    return _

print(f"Phrase: {phrase},\nKey: {key}")
cypher_ = cypher(key, phrase)
print(f"Cypher: {cypher_}")
decoded = cypher(key, cypher_)
print(f"DeCypher: {decoded}")