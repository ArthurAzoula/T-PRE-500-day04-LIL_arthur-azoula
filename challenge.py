def challenge():
    word, nb = input('Enter a word: '), int(input('Enter a number: '))
    if nb == 0: return
    return nb if any(letter.lower() in 'aeiouy' for letter in word) or nb >= 42 else word

print(challenge())