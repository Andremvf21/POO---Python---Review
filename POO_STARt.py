class Casa:
    def __init__(self, cor, quartos):
        self.cor = cor
        self.quartos = quartos

    def mostrar_cor(self):
        print(f"A cor da casa e: {self.cor}")

    def mostrar_quartos(self):
        print(f"Essa casa tem {self.quartos} quartos")

casa1 = Casa('Azul', 4)
casa2 = Casa('Vermelho', 6)


print("\nCasa1:\n")
casa1.mostrar_cor()
casa1.mostrar_quartos()

print("\nCasa2:\n")
casa2.mostrar_cor()
casa2.mostrar_quartos()


