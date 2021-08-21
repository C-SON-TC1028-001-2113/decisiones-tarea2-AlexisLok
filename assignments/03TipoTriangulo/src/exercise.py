def main():
    #escribe tu código abajo de esta línea
    
    X = int(input("Ingresa la medida del lado 1: "))
    Y = int(input("Ingresa la medida del lado 2: "))
    Z = int(input("Ingresa la medida del lado 3: "))
    
    if X + Y > Z and X + Z > Y and Y + Z > X:
        if X == Y and Y == Z:
            print("ES UN TRIANGULO EQUILATERO")
            pass
        elif X != Y and X != Z and Y != Z:
            print("ES UN TRIANGULO ESCALENO")
            pass
        else:
            print("ES UN TRIANGULO ISOSCELES")
    else:
        print("NO ES TRIANGULO")
        pass


if __name__=='__main__':
    main()
