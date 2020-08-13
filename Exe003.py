class calculadora():
    def mostrar_resultado(self):
        pergunta = float(input('informe o primeiro numero: '))
        numero1  = pergunta
        pergunta = float(input('informe o segundo numero: '))
        numero2 = pergunta

        print('soma = ', numero1 + numero2)
        print('subtracao = ', numero1 + numero2)
        print('multiplicacao = ', numero1 + numero2)
        print('divisao = ', numero1 + numero2)

conta = calculadora()
conta.mostrar_resultado()
