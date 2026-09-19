class Casa: # Definindo CLasse
    def __init__(self, cor, quartos, banheiros): # Definindo construtor 
        self.cor = cor 
        self.quartos = quartos
        self.banheiros = banheiros
    


    def mostrar_cor(self): # Funcao/Metodos
        print(f"A cor da casa e: {self.cor}")

    def mostrar_quartos(self):
        print(f"Essa casa tem {self.quartos} quartos")

    def mostrar_banheiros(self):
            print(f"Essa casa tem {self.banheiros} banheiros")

    def adicionar_quarto(self):
         self.quartos +=1
         print(f"Essa casa tem agora {self.quartos} quartos")

    def pintar_casa(self, nova_cor): # Metodo modificador
         print(f"Pintando a casa de {self.cor} para {nova_cor}")

casa1 = Casa('Azul', 4, 3) # Instancias
casa2 = Casa('Vermelho', 6, 4)


print("\nCasa1:\n")
casa1.mostrar_cor() # Chmando metodos
casa1.mostrar_quartos()
casa1.mostrar_banheiros()
casa1.adicionar_quarto()
casa1.pintar_casa('roxo') # Modificando

print("\nCasa2:\n")
casa2.mostrar_cor()
casa2.mostrar_quartos()
casa2.mostrar_banheiros()
casa2.adicionar_quarto()



