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

MAX_KEY_SIZE = 26

def getMode():
    while True:
        print('do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
    print('hello')
    return input()

def getKey():
    key = 0
    while True:
        print('enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedmessage(mode, message, key):
    if mode[0] =='d':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
                    elif symbol.i
