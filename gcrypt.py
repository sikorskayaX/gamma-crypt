#gamma encryption
def encode(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    len_alphabet = len(alphabet)
    key = extend_key(text, key)
    encoded_text = ''
    text.lower() #making all letters lowercase
    #find the index of the current character in the alphabet and the index of the character in the key
    #find the remainder of the division by length because the sum can be greater than the length of the alphabet
    for i in range(len(text)):
        x = (alphabet.index(text[i]) + alphabet.index(key[i])) % len_alphabet
        encoded_text += alphabet[x]
    return encoded_text

#extending the key to the length of the source text if the key is shorter than the text
def extend_key(text, key):
    if len(text) <= len(key):
        return key
    else:
        #extension by repeating key characters
        for i in range(len(text) - len(key)):
            key += key[i % len(key)]
        return key