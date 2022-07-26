import random

def guess(x):
    randomNumber = random.randint(1, x)
    guess = 0
    while guess != randomNumber:
        guess = int(input(f'adivina un numero entre 1 y  {x}: '))
        if guess < randomNumber:
            print('intenta de nuevo, muy bajo.')
        elif guess > randomNumber:
            print('Intenta de nuevo, muy alto.')
    print(f'Yay, Adivinaste, el numero es {randomNumber}!!!')
guess(10)

print('\nMi turno...!\n')

def turnoComp(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'es el numero {guess} muy alto (H), muy bajo (L), o es el correcto (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay! adivine tu numero, {guess}!')
turnoComp(10)