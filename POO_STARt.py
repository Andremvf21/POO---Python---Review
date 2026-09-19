class Casa:
    def __init__(self, cor):
        self.cor = cor

    def mostrar_cor(self):
        print(f"A cor da casa e: {self.cor}")

casa1 = Casa('Azul')
casa2 = Casa('Vermelho')

print("\nCasa1:\n")
casa1.mostrar_cor()
