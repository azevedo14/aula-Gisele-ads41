class classe_idade():
    def idade(self):
        pergunta = int(input("quantos anos voce tem;\n"
                             "Colocar (0) encerra o programa;\n"
                             ": "))
        if pergunta <18:
            print("voce eh menor de 18 anos")
        elif pergunta >=18:
            print("voce eh maior de 18 anos")

pessoa = classe_idade()
pessoa.idade()
