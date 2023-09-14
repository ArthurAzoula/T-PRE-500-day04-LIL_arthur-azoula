# task 00

def displayInteger():
    for i in range(1,1001):
        print(i)

print(displayInteger())

# task 01

def doubleLetter():

    word = input('A word please : ')

    double_word = ''

    for letter in word:
        double_word += letter*2

    return double_word

print(doubleLetter())

# task 02

def displayDivideBySeven():
    for i in range(10000,0,-1):
        if i%7 == 0:
            print(f'Can be divide : {i}')

print(displayDivideBySeven())

# task 03

def fizzBuzz():
    for i in range(-30,31,1):
        if i%3 == 0 and i%5 == 0:
            print(f"{i} : FizzBuzz")
        elif i%3 == 0:
            print(f"{i} : Fizz")
        elif i%5 == 0:
            print(f'{i} : Buzz')
        else:
            print(i)

print(fizzBuzz())

# task 04

def bottles():
    for i in range(99,1,-1):
        if i == 1:
            print(f"{i} bottle of age appropriate bottles on the wall")
        else:
            print(f"{i} bottles of age appropriate bottles on the wall")
    print('No more bottles of age appropriate bottles on the wall')

print(bottles())

# task 05

def listMultiple():
    nb = int(input('Number : '))

    for i in range(2, nb//2 + 1):
        multiples = []
        for j in range(nb):
            if j*i < nb and j*i != 0:
                multiples.append(j*i)
                multiples.sort(reverse=True)
        print(multiples)    

print(listMultiple())