# 1 Desafio Alfabeto
# Dada a letra N do alfabeto, nos diga qual a sua posição.

# Entrada
# Um único caracter N, uma letra maiúscula ('A'-'Z') do alfabeto (que contém 26 letras).

# Saída
# Um único inteiro, que representa a posição da letra no alfabeto.


# Exemplo de Entrada
# C
# Exemplo de Saída
# 3

# Exemplo de Entrada
# J
# Exemplo de Saída
# 10

# Exemplo de Entrada
# Z
# Exemplo de Saída
# 26

# Exemplo de Entrada
# A
# Exemplo de Saída
# 1

# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário,
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO ord(): Retorna o valor  ASCII de cada letra ou símbolo do teclado;

# Primeira Solução

letra = input("Por gentileza, digite uma letra do alfabeto: ")
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print(alfabeto.index(letra.upper())+1)


# Segunda Solução
digite_letra_tab_ascII = input("Por gentileza, digite uma letra..: ")
print(int(ord(digite_letra_tab_ascII.upper())-64))
