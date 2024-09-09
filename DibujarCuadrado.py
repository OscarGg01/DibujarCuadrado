class DibujarCuadrado:
    def __init__(self, dimension):
        self.dimension = dimension

    def dibujar_borde_superior_inferior(self):
        # Dibuja el borde superior o inferior del cuadrado
        for i in range(self.dimension + 1):
            print('* ', end='')
        print()

    def dibujar_lados(self):
        # Dibuja los lados del cuadrado, con espacios en el medio
        for j in range(self.dimension - 2):
            for k in range(self.dimension):
                if k == 0:
                    print('* ', end='')
                elif k == self.dimension - 1:
                    print('  *', end='')
                else:
                    print('  ', end='')
            print()

    def dibujar_cuadrado(self):
        self.dibujar_borde_superior_inferior()
        self.dibujar_lados()
        self.dibujar_borde_superior_inferior()