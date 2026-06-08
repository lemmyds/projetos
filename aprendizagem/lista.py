# Lista é uma coleção ordenada e mutável. Permite membros duplicados.
lista = ['carro', True, 2, 3.5]
print(lista)
print(type(lista))
print(lista[1])
print('-'*30)

# Tupla é uma coleção ordenada e imutável. Permite membros duplicados.
tupla = ('carro', True, 2, 3,5)
print(tupla)
print(type(tupla))
print(tupla[3])
print('-'*30)

# O dicíonario é uma coleção ordenada e mutável. Nenhum membro duplicado.
                #chave:   valor
dicionario = {'nome': 'carro', 'logica': True, 'numero': 2, 'outroNumero': 3.5}
print(dicionario)
print(type(dicionario))
print(dicionario['logica'])
print('-'*30)

# Set é uma coleção não ordenada e não indexada. Nenhum membro duplicado.
conjunto = {'carro', True, 2, 3.5}
print(conjunto)
print(type(conjunto))
print(conjunto[1])