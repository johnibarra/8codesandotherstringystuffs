def letterToIndex(letter):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '
    idx = alphabet.find(letter)
    if idx == -1:       # means that it wasn't in the alphabet
        print("error:", letter, "is not in the alphabet")
    return idx

def indexToletter(idx):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '
    letter = ' '
    if idx >= len(alphabet):
        print("error:", idx, "it's too large.")
    elif idx < 0:
        print('error', idx, "it's to small.")
    else:
        letter = alphabet[idx]
    return letter
