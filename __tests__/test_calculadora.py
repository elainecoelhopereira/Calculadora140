# 1- bibliotecas, frameworks, e referencias externas
import pytest  # framework de teste de unidade

# funções q sewrão testadas
from calculadora.calculadora import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros

# 2- Testes

def test_somar_dois_numeros():

    # Padrão / Standart AAA (se diz Tiple A /3A) = Arrange, Act, Assert

    # Arrange / Prepara / Configura
    # Dados entrada e saída
    num1 = 5
    num2 = 7
    resultado_esperado = 12

    # Act / Executa
    resultado_obtido = somar_dois_numeros(num1, num2)

    # Asset / Valida
    assert resultado_esperado == resultado_obtido