def cesar_cipher(word, shift):
    if len(word) == 0:
        return ''

    list_of_chars = [chr(ord(char) + shift) for char in word]

    return ''.join(list_of_chars)
