# -*- coding: utf-8 -*-
from calculadora import Calculadora

class CalculadoraController:
    def chooseOperation(self):
        print("\nCALCULADORA PYTHON")

        print("\nQual operação você quer fazer?")
        print("1- Soma")
        print("2- Subtração")

        self.operacao = input()

    def catValues(self):
        self.a = input("Primeiro valor: ")
        self.b = input("Segundo valor: ")

    def runOperation(self):
        classCalculadora = Calculadora()

        if (self.operacao == 1 ):
            result = classCalculadora.somar(self.a, self.b)
        if (self.operacao == 2 ):
            result = classCalculadora.subtrair(self.a, self.b)

        return "\nRespostado da operação é: " + str(result)