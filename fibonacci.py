Epsilon = input(('Esta aplicacion genera una sucecion de Fibonacci,\n Seleccione I para generar la sucesion por iteraciones o\n Seleccione L para una cantidad limite: ')).upper()

if Epsilon == 'L':
    def Alpha(Beta):
        Gamma, Delta = 0, 1
        while Gamma < Beta:
            print(Gamma, end = ' ')
            Gamma, Delta = Delta, Gamma + Delta
    print()
    Alpha(int(input('Digite el limite de la susecion: ')))

elif Epsilon == 'I':
    Gamma, Delta = 0, 1
    Beta = int(input('Digite canitdad de iteraciones: '))
    for Zeta in range(Beta):
        print(Zeta, Gamma)
        Gamma, Delta = Delta, Gamma + Delta 
else:
    print('Seleccione una opcion correcta I/L')