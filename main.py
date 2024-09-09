from DibujarCuadrado import DibujarCuadrado

N = int(input("Escribe la dimension N>= 2 del cuadrado a dibujar: "))
if N >= 2:
    cuadrado = DibujarCuadrado(N)
    cuadrado.dibujar_cuadrado()
else:
    print("La dimensión debe ser mayor o igual a 2.")