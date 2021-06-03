nato_alphabet = {
    'a': "Alpha",
    'b': "Bravo",
    'c': "Charlie",
    'd': "Delta",
    'e': "Echo",
    'f': "Foxtrot",
    'g': "Golf",
    'h': "Hotel",
    'i': "India",
    'j': "Juliet",
    'k': "Kilo",
    'l': "Lima",
    'm': "Mike",
    'n': "November",
    'o': "Oscar",
    'p': "Papa",
    'q': "Quebec",
    'r': "Romeo",
    's': "Sierra",
    't': "Tango",
    'u': "Uniform",
    'v': "Victor",
    'w': "Whisky",
    'x': "XRay",
    'y': "Yankee",
    'z': "Zulu"
}

word = input("Enter a word: ").lower()
nato_word = [nato_alphabet[char] for char in word]
print(nato_word)
