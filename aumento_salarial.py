# 3 - Desafio Aumento Salarial
# A empresa que você trabalha resolveu conceder um aumento salarial a todos funcionários, de acordo com a tabela abaixo:

# Salário	                       Percentual de Reajuste
# 0 - 600.00			                17%
# 600.01 - 900.00			            13%
# 900.01 - 1500.00		            12%
# 1500.01 - 2000.00		            10%
# Acima de 2000.00		            5%

# Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

# A entrada contém apenas um valor de ponto flutuante, que pode ser maior ou igual a zero, com duas casas decimais, conforme exemplos abaixo.

# Exemplo 1
# Entrada
# 1000

# Saída
# Novo salario: 1120,00
# Reajuste ganho: 120,00
# Em percentual: 12 %

# Exemplo 2
# Entrada
# 2000
# Saída
# Novo salario: 2200,00
# Reajuste ganho: 200,00
# Em percentual: 10 %

# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário,
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas
# em cada parâmetro da função ou com os valores predefinidos por padrão;

faixa_salarial = int(input())


def calcular_reajuste(faixa_salarial):
    reajuste = 0
    if faixa_salarial <= 600:
        reajuste = 17
    elif faixa_salarial <= 900:
        reajuste = 13
    elif faixa_salarial <= 1500:
        reajuste = 12
    elif faixa_salarial <= 2000:
        reajuste = 10
    else:
        reajuste = 5

    return reajuste


reajuste = calcular_reajuste(faixa_salarial)
parcial = (faixa_salarial*reajuste) / 100
# print(f"Novo salario: {(faixa_salarial + parcial):.2f}\nReajuste ganho: {parcial:.2f}\nEm percentual: {reajuste} %"
#      .replace(".", ","))
print(f"Novo salario: {(faixa_salarial + parcial):.2f}\nReajuste ganho: {parcial:.2f}\nEm percentual: {reajuste} %".replace(".", "."))
