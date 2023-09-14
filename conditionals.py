# task 0

# (42 > 12) 42 bigger than 12
# (12 = 12) 12 become 12
# (12 == 12) 12 egals 12
# (“hello” == “world” hello egals world 
# (218 >= 118) 218 bigger or egal to 119
# (“a”.upper() == “A”) a become A egals A
# (1 ∗ 2 ∗ 3 ∗ 4 <= 9) operation less than 9
# (“z” in “azerty”) z contains in azerty

# task 01

def f42():

    nb = int(input("Number : "))

    if(nb == 42):
        return 'Display correct'
    
    return 'Oops...'

print(f42())

# task 02

def ask_odd_even():
    nb = int(input('Odd or Even : '))

    odd_even = 'Even' if nb%2 == 0 else 'Odd'

    return odd_even

print(ask_odd_even())

# task 03 

def password():
    passw = input("Password ##%£µ : ")

    if passw == 'open sesame':
        return "access granted"
    elif passw == "will you open, you goddamn !¤*@":
        return "access fucking granted"
    else:
        return "access denied"

print(password())

# task 04

def OK():
    nb = int(input("Numbeeeeer plz : "))

    if nb == 42 or nb <= 21 or nb%2 == 0 or nb // 2 < 21 or (nb%2 == 0 and nb >= 45):
        return 'OK'
    else:
        return 'You got wrong my poor friend!'
    
print(OK())

# task 05

def correct():
    a = 42
    b = 41
    if a == b:
        print ( " A and B are the sames " )
    if b <= a:
        print ( " B is equal or lower as A " )
    if b != a:
        print ( " B his different from A " )

print(correct())