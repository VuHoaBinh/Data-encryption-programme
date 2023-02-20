# ma thay the

substitution_table = {
    'a': 'x',
    'b': 'n',
    'c': 'y',
    'd': 'a',
    'e': 'h',
    'f': 'p',
    'g': 'o',
    'h': 'g',
    'i': 'z',
    'j': 'q',
    'k': 'w',
    'l': 'b',
    'm': 't',
    'n': 's',
    'o': 'f',
    'p': 'l',
    'q': 'r',
    'r': 'c',
    's': 'v',
    't': 'm',
    'u': 'u',
    'v': 'e',
    'w': 'k',
    'x': 'j',
    'y': 'd',
    'z': 'i'
}

substitution_table_back = {
    'a': 'd',
    'b': 'l',
    'c': 'r',
    'd': 'y',
    'e': 'v',
    'f': 'o',
    'g': 'h',
    'h': 'e',
    'i': 'z',
    'j': 'x',
    'k': 'w',
    'l': 'p',
    'm': 't',
    'n': 'b',
    'o': 'g',
    'p': 'f',
    'q': 'j',
    'r': 'q',
    's': 'n',
    't': 'm',
    'u': 'u',
    'v': 's',
    'w': 'k',
    'x': 'a',
    'y': 'c',
    'z': 'i'
}

def substitution_cipher(message):
    cipher_text = ''
    for char in message:
        if char in substitution_table:
            cipher_text += substitution_table[char]
        else:
            cipher_text += char
    return cipher_text

def substitution_cipher_back(message):
    cipher_text = ''
    for char in message:
        if char in substitution_table_back:
            cipher_text += substitution_table_back[char]
        else:
            cipher_text += char
    return cipher_text

def run():
    print(substitution_cipher("spriderman"))
run()

def run1():
    print(substitution_cipher_back("vlzahctxs"))
run1()