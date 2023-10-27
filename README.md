# Gamma encryption ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

This code implements a simple encryption algorithm called gamma encryption. The encode function takes a text and a key as input and returns the encrypted version of the text. The decode function takes an encrypted text and the same key used for encryption and returns the decrypted version of the text.
## clone repo

```bash
$ git clone https://github.com/sikorskayaX/gamma-crypt.git
```

## Encryption

The encode function converts the text to lowercase and removes any spaces.
It then iterates over each character in the text and calculates the encoded character using the formula: (alphabet.index(text[i]) + alphabet.index(key[i])) % len_alphabet. This formula finds the index of the current character in the alphabet and the index of the corresponding character in the key, adds them together, and takes the remainder when divided by the length of the alphabet. This ensures that the encoded character is within the range of the alphabet.
The encoded characters are concatenated to form the encoded_text, which is then returned.

## Decryption

The decode function converts the text to lowercase and removes any spaces.
It iterates over each character in the text and calculates the decoded character using the formula: (alphabet.index(text[i]) - alphabet.index(key[i])) % len_alphabet. This formula finds the index of the current character in the alphabet and the index of the corresponding character in the key, subtracts them, and takes the remainder when divided by the length of the alphabet. This ensures that the decoded character is within the range of the alphabet.
The decoded characters are concatenated to form the decoded_text, which is then returned.

## Additional function extend_key

The extend_key function extends the key to the length of the text if the key is shorter than the text. It does this by repeating the characters of the key until it reaches the desired length.

## Example

In the provided example, the word "hello" is encrypted using the key "world". The encrypted text is then decrypted using the same key, resulting in the original word "hello".

```bash
word = encode("hello", "world")
print('encrypted text: ', word)
print('decrypted text: ', decode(word, "world"))
```
Result :

```bash
encrypted text:  dscwr
decrypted text:  hello
```

