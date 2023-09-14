# task 01

def encrypt(chaine: str, key: int):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    chaine_encrypt = ''

    for i in range(len(chaine)):
        index = 0
        if chaine[i].upper() in alphabet:
            index = alphabet.index(chaine[i].upper())
            new_index = (index + key) % len(alphabet)
            chaine_encrypt += alphabet[new_index]
        else:
            chaine_encrypt += ' '

    return chaine_encrypt

# task 01.5

def decrypt(chaine: str, key: int):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    chaine_decrypt = ''

    for i in range(len(chaine)):
        index = 0
        if chaine[i].upper() in alphabet:
            index = alphabet.index(chaine[i].upper())
            new_index = (index - key) % len(alphabet)
            chaine_decrypt += alphabet[new_index]
        else:
            chaine_decrypt += ' '
    return chaine_decrypt.capitalize()


print(encrypt('Hello world', 4))
print(decrypt(encrypt('Hello world', 4), 4))

# task 02