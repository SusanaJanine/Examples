def menu():
    print('CALCULADORA SIMPLE')
    print('1, Sumar')
    print('2, Restar')
    print('3, Multiplicar')
    print('4, Dividir')
    print('5, Salir')

def calculadora():
    while True:
        menu()
        opcion = input('ingrese una opcion:')

        if opcion == '5':
            print('Gracias por usar la calculadora')
            break

        try:
            num1 = float(input('Ingrese el primer número: '))
            num2 = float(input('Ingrese el segundo número: '))
        except ValueError:
            print('Ingrese números válidos')
            continue

        if opcion == '1':
            print(f'El resultado de la suma es: {num1 + num2}')
        elif opcion == '2':
            print(f'El resultado de la resta es: {num1 - num2}')
        elif opcion == '3':
            print(f'El resultado de la multiplicación es: {num1 * num2}')
        elif opcion == '4':
            if num2 != 0:
                print(f'El resultado de la división es: {num1 / num2}')
            else:
                print('Error: No se puede dividir por cero')
        else:
            print('Opción no válida, por favor intente de nuevo')

calculadora()